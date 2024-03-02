#Libraries called in.
import argparse
import socket
import sys
from datetime import datetime

#Main program contents.
def log_message(log_file, message, print_also=True):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  #Get live timestamp of when the scan was done.
    message = f"{timestamp} - {message}"  #Include live timestamp in the message.
    if log_file:
        try:
            with open(log_file, "r") as log:
                log_contents = log.read()
                needs_newline = not log_contents.endswith('\n')
        except FileNotFoundError:
            needs_newline = False

        with open(log_file, "a") as log:
            if needs_newline:
                log.write('\n')
            log.write(f"{message}\n\n")
    if print_also or not log_file:
        print(message)

def initialize_log_file(log_file):
    if log_file:
        try:
            with open(log_file, "r") as log:
                log_contents = log.read()
                needs_newline = not log_contents.endswith('\n')
        except FileNotFoundError:
            needs_newline = False

        with open(log_file, "a") as log:
            if needs_newline:
                log.write('\n')
            now = datetime.now()
            date_time_str = f"# Date: {now.strftime('%d/%m/%Y')} Time: {now.strftime('%H:%M')} #"
            border = '#' * len(date_time_str)
            log.write(f"{border}\n")
            log.write(f"{date_time_str}\n")
            log.write(f"{border}\n\n")

def scan_port(ip, port, log_file=None):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)  # Adjusted timeout for response rates.
            result = s.connect_ex((ip, port))
            status_message = "OPEN" if result == 0 else "Closed" #Message output aligned.
            log_message(log_file, f"Port {port} on {ip} is {status_message:>6}.", log_file is None if result == 0 else False) #Message output right-aligned.
    except Exception as e:
        log_message(log_file, f"Exception scanning port {port} on {ip}: {e}", log_file is None)

def print_custom_usage(prog_name):
    print(f"Usage {prog_name} (-H <target host> | -t <target or filename>)")
    print("\t\t      [-p <target port> | -r <start_port-end_port>]") #Assignment brief manual matching.
    print("\t\t     [-L <log file name>]") #Till the last minute detail.

def main():
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']):
        print_custom_usage(sys.argv[0])
        sys.exit(1)

    parser = argparse.ArgumentParser(description="A port scanner that supports scanning specified hosts or a list from a file.", add_help=False)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-H", "--host", help="Specify the target host IP.")
    group.add_argument("-t", "--targetfile", help="Path to a file listing target IPs, one per line.")
    parser.add_argument("-p", "--port", type=int, help="Target port number to scan. Optional if using --range.")
    parser.add_argument("-r", "--range", help="Custom port range to scan, formatted as start-end (e.g., 20-80).", metavar="RANGE")
    parser.add_argument("-L", "--logfile", help="File to log the scan results. Optional.")

    args = parser.parse_args()

    if args.logfile:
        initialize_log_file(args.logfile)

    targets = []
    if args.host:
        targets.append(args.host)
    elif args.targetfile:
        try:
            with open(args.targetfile, 'r') as file:
                targets = [line.split('#')[0].strip() for line in file if line.strip() and not line.startswith('#')] #Handling inline comments starting with "#" and keeping IP Address only from targeted file.
        except FileNotFoundError:
            print("The specified file could not be found. Please check the path and try again.")
            sys.exit(1)

    if args.range:
        try:
            start_port, end_port = map(int, args.range.split('-'))
        except ValueError:
            print("Invalid range format. Please use start-end (e.g., 20-80).")
            sys.exit(1)
    else:
        start_port, end_port = (1, 1024) if not args.port else (args.port, args.port)

    for target in targets:
        if target: #Check if targeted file is not empty after stripping comments and keeping IP address only.
            for port in range(start_port, end_port + 1):
                scan_port(target, port, args.logfile)

if __name__ == "__main__":
    main()

# Made by Stavros Vakouftsis (SV200) #
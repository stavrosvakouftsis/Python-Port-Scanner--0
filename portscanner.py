import argparse
import socket
import sys
from datetime import datetime

def log_message(log_file, message, print_also=True):
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

def scan_port(ip, port, log_file):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(10)  # Increased timeout for slow responses
            result = s.connect_ex((ip, port))
            if result == 0:
                log_message(log_file, f"Port {port} is open on {ip}.", log_file is None)
            else:
                log_message(log_file, f"Port {port} on {ip} is closed.", False)
    except Exception as e:
        log_message(log_file, f"Exception: {e}", log_file is None)

def print_custom_usage(prog_name):
    print(f"Usage {prog_name} (-H <target host> | -t <target or filename>)")
    print("\t\t      -p <target port>")  # Adjusted for tab indentation
    print("\t\t     [-L <log file name>]")  # Adjusted for tab indentation

def main():
    if len(sys.argv) == 1 or (len(sys.argv) == 2 and sys.argv[1] in ['-h', '--help']):
        print_custom_usage(sys.argv[0])
        sys.exit(1)

    parser = argparse.ArgumentParser(description="A port scanner that supports scanning specified hosts or a list from a file.", add_help=False)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-H", "--host", help="Specify the target host IP.")
    group.add_argument("-t", "--targetfile", help="Path to a file listing target IPs, one per line.")
    parser.add_argument("-p", "--port", type=int, required=True, help="Target port number to scan.")
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
                targets = file.read().splitlines()
        except FileNotFoundError:
            print("The specified file could not be found. Please check the path and try again.")
            sys.exit(1)

    for target in targets:
        scan_port(target, args.port, args.logfile)

if __name__ == "__main__":
    main()

# Made by Stavros Vakouftsis (SV200) #
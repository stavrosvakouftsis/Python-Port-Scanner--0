# Python Port Scanner
Assignment one for 2023-24 (Easter) Digital Forensics and Ethical Hacking (U10809) with Danny Werb...

A versatile tool for network security analysis, designed to identify open ports on both local and remote hosts. This utility simplifies the process of port scanning for security analysis and educational purposes.

## Features

- **Single and Multiple Host Scanning**: Target individual IPs or a list of IPs from a file.
- **Logging Capability**: Save your scan results to a file for further analysis.
- **Inline Comment Support**: Exclude specific targets or notes in your target files with comments.
- **Custom Usage Instructions**: Easily understand how to use the tool with built-in help.
- **Timestamped Logging**: All log entries are timestamped for better tracking and analysis.
- **Formatted Output**: Output is neatly aligned for readability, with OPEN ports highlighted for emphasis.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Installation

Clone the repository to get started with the Python Port Scanner:

```bash
git clone https://github.com/stavrosvakouftsis/Python-Port-Scanner--0.git
```

### Usage

To scan a single host:

```bash
python3 portscanner.py -H <host> -p <port>
```

To scan multiple hosts from a file:

```bash
python3 portscanner.py -t <file> -p <port>
```

To log scan results to a file:

```bash
python3 portscanner.py -H <host> -p <port> -L <log_file>
```

### Advanced Usage

- **Custom Port Range**: Specify a range of ports to scan on a target.

```bash
python3 portscanner.py -H <host> -r <start_port-end_port>
```

## Contributing

Your contributions are welcome! Please fork the repository, create your feature branch, commit your changes, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- Stavros Vakouftsis - [@vakouftsis_stavros](https://www.instagram.com/vakouftsis_stavros/)
- Project Link: [https://github.com/stavrosvakouftsis/Python-Port-Scanner--0](https://github.com/stavrosvakouftsis/Python-Port-Scanner--0)

## Acknowledgements

- [Python.org](https://python.org/)
- Canterbury Christ Church University (CCCU)

![CCCU](https://tinyurl.com/CCCU-Uni)
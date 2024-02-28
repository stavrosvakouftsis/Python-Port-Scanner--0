# Python Port Scanner
Assignment one for 2023-24 (Easter) Digital Forensics and Ethical Hacking (U10809) and Danny Werb...


A versatile tool for network security analysis, designed to identify open ports on both local and remote hosts.

## Features

- Single and Multiple Host Scanning
- Logging Capability
- Inline Comment Support for target files
- Custom Usage Instructions

## Getting Started

### Prerequisites

- Python 3.x

### Installation

```
git clone https://github.com/stavrosvakouftsis/Python-Port-Scanner--0.git
```

### Usage

Scan a host:
```
python3 portscanner.py -H <host> -p <port>
```

Scan hosts from a file:
```
python3 portscanner.py -t <file> -p <port>
```

Log results:
```
python3 portscanner.py -H <host> -p <port> -L <log_file>
```

## Contributing

Contributions are welcome! Please create a branch, add commits, and open a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

- Stavros Vakouftsis - [@vakouftsis_stavros](https://www.instagram.com/vakouftsis_stavros/)
- Project Link: https://github.com/stavrosvakouftsis/Python-Port-Scanner--0

## Acknowledgements

- [Python.org](https://python.org/)
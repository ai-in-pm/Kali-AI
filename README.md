# KaliAI 🛡️

AI-powered Ethical Hacking Assistant for Kali Linux

KaliAI is an advanced AI assistant designed to help security professionals and ethical hackers leverage Kali Linux tools effectively and safely. It provides guidance, explanations, and security insights while emphasizing ethical considerations and best practices.

│     |   < | | | | | |/ ___ \  | |  │
│     |_|\_\__,_|_|_/_/   \_\|___|   │
│                                    │
│     Ethical Hacking Assistant Demo │
│                                    │
╰────────────────────────────────────╯

Welcome to the KaliAI Demo!
This interactive demonstration showcases the key features of KaliAI,
an ethical hacking assistant specialized in Kali Linux.


Options:
1. Tool Explanation Demo
2. Command Analysis Demo
3. Interactive Chat Demo
4. Exit

Choose an option [1/2/3/4]: 


## Features

### 1. Expert Guidance
- Detailed explanations of Kali Linux tools
- Step-by-step usage instructions
- Security concept clarification
- Best practice recommendations

### 2. Command Analysis
- Command syntax explanation
- Parameter/flag breakdown
- Security implication assessment
- Ethical consideration reminders

### 3. Tool Knowledge
- Deep understanding of common security tools:
  - nmap, nikto, dirb/gobuster, wpscan
  - sqlmap, wireshark, metasploit
  - hydra, john, hashcat
  - burpsuite, aircrack-ng, maltego
  - beef, zaproxy, and more

### 4. Safe Command Execution
- Command validation
- Security checks
- Result interpretation
- Follow-up recommendations

## Installation

1. Create and activate a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install KaliAI:
```bash
pip install .
```

3. Configure your OpenAI API key:
```bash
kaliagent configure --api-key your-api-key-here
```

## Usage

### Interactive Mode
Start an interactive session with KaliAI:
```bash
kaliagent interactive
```

### Learn About Tools
Get detailed information about specific Kali tools:
```bash
kaliagent learn nmap
```

### Analyze Commands
Analyze Kali Linux commands without executing them:
```bash
kaliagent analyze "nmap -sS -T4 192.168.1.1"
```

## Configuration Options

```bash
# Set OpenAI API key
kaliagent configure --api-key your-api-key-here

# Disable safe mode (enable command execution)
kaliagent configure --no-safe-mode

# Disable command confirmation
kaliagent configure --no-confirm
```

## Ethical Guidelines

KaliAI is designed to promote ethical hacking practices:

1. **Always obtain proper authorization** before testing any system
2. **Document all activities** and maintain detailed logs
3. **Respect privacy** and data confidentiality
4. **Practice responsible disclosure** for any vulnerabilities found
5. **Stay within legal boundaries** at all times

## Security Features

- Command validation against allowed tools list
- Safe mode to prevent accidental command execution
- Confirmation prompts before running commands
- Detailed explanation of security implications
- Result analysis with security context

## Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

KaliAI is a tool for educational and professional security testing only. Users are responsible for ensuring all activities conducted with this tool are legal, authorized, and ethical.

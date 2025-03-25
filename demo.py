#!/usr/bin/env python3
"""
KaliAI Demo - Ethical Hacking Assistant
Real-time demonstration script that can be run anytime
"""

import os
import sys
import json
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
import subprocess
from pathlib import Path

console = Console()

# Sample data for the demo
SAMPLE_TOOLS = {
    "nmap": {
        "description": "Network scanning and mapping tool",
        "example": "nmap -sS -T4 192.168.1.1",
        "explanation": "This command performs a SYN scan (-sS) with aggressive timing (-T4) on the target IP."
    },
    "nikto": {
        "description": "Web server scanner for dangerous files/CGIs",
        "example": "nikto -h http://example.com",
        "explanation": "This scans the web server at example.com for known vulnerabilities and misconfigurations."
    },
    "dirb": {
        "description": "Web content scanner using dictionary files",
        "example": "dirb http://example.com",
        "explanation": "This attempts to find hidden directories and files on the web server using default wordlists."
    },
    "sqlmap": {
        "description": "Automated SQL injection tool",
        "example": "sqlmap -u 'http://example.com/page.php?id=1'",
        "explanation": "This tests the specified parameter for SQL injection vulnerabilities."
    },
    "metasploit": {
        "description": "Penetration testing framework",
        "example": "msfconsole",
        "explanation": "This starts the Metasploit Framework console for exploitation activities."
    }
}

def main():
    """Main demo function"""
    try:
        # Display welcome banner
        display_banner()
        
        while True:
            # Show options menu
            option = display_menu()
            
            if option == '1':
                # Tool explanation demo
                tool_explanation_demo()
            elif option == '2':
                # Command analysis demo
                command_analysis_demo()
            elif option == '3':
                # Interactive chat demo (simplified)
                interactive_chat_demo()
            elif option == '4':
                # Exit
                console.print("\n[bold blue]Thank you for trying KaliAI! Goodbye![/bold blue]")
                sys.exit(0)
            else:
                console.print("[red]Invalid option. Please try again.[/red]")
            
            # Prompt to continue
            console.print("\nPress Enter to continue...")
            input()
            
    except KeyboardInterrupt:
        console.print("\n[bold blue]Demo terminated. Goodbye![/bold blue]")
        sys.exit(0)

def display_banner():
    """Display welcome banner"""
    banner = """
     _   __      _ _    _    ___ 
    | | / /     | (_)  / \   |_ _|
    | |/ / _   _| |_  / _ \   | | 
    |   < | | | | | |/ ___ \  | | 
    |_|\_\\__,_|_|_/_/   \_\|___|
                              
    Ethical Hacking Assistant Demo
    """
    
    console.print(Panel.fit(banner, border_style="blue"))
    console.print("\n[bold]Welcome to the KaliAI Demo![/bold]")
    console.print("This interactive demonstration showcases the key features of KaliAI,")
    console.print("an ethical hacking assistant specialized in Kali Linux.\n")

def display_menu():
    """Display main menu and get user choice"""
    console.print("\n[bold blue]Options:[/bold blue]")
    console.print("1. Tool Explanation Demo")
    console.print("2. Command Analysis Demo")
    console.print("3. Interactive Chat Demo")
    console.print("4. Exit")
    
    return Prompt.ask("\nChoose an option", choices=["1", "2", "3", "4"])

def tool_explanation_demo():
    """Demo of tool explanation feature"""
    console.print("\n[bold blue]Tool Explanation Demo[/bold blue]")
    console.print("KaliAI can provide detailed explanations of security tools.")
    
    # Display available tools
    console.print("\n[bold]Available tools for this demo:[/bold]")
    for i, tool in enumerate(SAMPLE_TOOLS.keys(), 1):
        console.print(f"{i}. {tool}")
    
    # Get tool selection
    selection = Prompt.ask("\nSelect a tool to learn about", choices=[str(i) for i in range(1, len(SAMPLE_TOOLS) + 1)])
    
    # Show tool info
    tool_name = list(SAMPLE_TOOLS.keys())[int(selection) - 1]
    tool_info = SAMPLE_TOOLS[tool_name]
    
    # Display formatted tool information
    console.print(f"\n[bold green]{tool_name.upper()}[/bold green]")
    console.print(f"[bold]Description:[/bold] {tool_info['description']}")
    console.print(f"\n[bold]Example usage:[/bold] `{tool_info['example']}`")
    console.print(f"\n[bold]Explanation:[/bold] {tool_info['explanation']}")
    
    # Display ethical considerations (simulated AI response)
    console.print("\n[bold]Ethical considerations:[/bold]")
    ethical_md = f"""
    When using {tool_name}, always ensure:
    
    1. **Authorization** - Only scan/test systems you have explicit permission to test
    2. **Documentation** - Keep detailed records of all testing activities
    3. **Scope limitation** - Strictly adhere to the defined scope of testing
    4. **Minimal impact** - Use the least intrusive methods necessary
    5. **Responsible disclosure** - Report any findings to the appropriate parties
    
    Remember that unauthorized scanning/testing is illegal in most jurisdictions.
    """
    console.print(Markdown(ethical_md))

def command_analysis_demo():
    """Demo of command analysis feature"""
    console.print("\n[bold blue]Command Analysis Demo[/bold blue]")
    console.print("KaliAI can analyze security commands and explain what they do.")
    
    # Sample commands for analysis
    sample_commands = [
        "nmap -sS -T4 -p 1-1000 192.168.1.1",
        "nikto -h http://example.com -Tuning 123bde",
        "sqlmap -u 'http://example.com/page.php?id=1' --dbs --batch"
    ]
    
    # Display sample commands
    console.print("\n[bold]Sample commands for analysis:[/bold]")
    for i, cmd in enumerate(sample_commands, 1):
        console.print(f"{i}. `{cmd}`")
    
    # Get command selection
    selection = Prompt.ask("\nSelect a command to analyze", choices=[str(i) for i in range(1, len(sample_commands) + 1)])
    
    # Analyze selected command
    selected_cmd = sample_commands[int(selection) - 1]
    
    # Display analysis (simulated AI response)
    console.print(f"\n[bold]Analyzing:[/bold] `{selected_cmd}`")
    
    if "nmap" in selected_cmd:
        analysis = """
        This nmap command performs a network scan with the following parameters:
        
        - **-sS**: SYN Scan - A stealthy scan that doesn't complete TCP connections
        - **-T4**: Timing template - Sets scan to aggressive speed
        - **-p 1-1000**: Port range - Scans only ports 1-1000
        - **192.168.1.1**: Target IP address
        
        **Security implications**:
        - This scan is relatively stealthy but still detectable by intrusion detection systems
        - It will identify open ports and services on the target system
        - The aggressive timing could trigger alerts or cause service disruption
        
        **Ethical considerations**:
        - Only perform this scan against systems you're authorized to test
        - The scan could impact network performance
        - Document all findings and report appropriately
        """
    elif "nikto" in selected_cmd:
        analysis = """
        This nikto command performs a web vulnerability scan with these parameters:
        
        - **-h http://example.com**: Target host to scan
        - **-Tuning 123bde**: Enables specific test categories:
          - 1: File Upload
          - 2: Misconfiguration/Default Files
          - 3: Information Disclosure
          - b: Database Tests
          - d: WebServer misconfigurations
          - e: Common vulnerabilities
        
        **Security implications**:
        - This is a noisy scan that will be logged by the target server
        - It will test for multiple vulnerabilities and misconfigurations
        - It may generate significant log entries on the target system
        
        **Ethical considerations**:
        - Only use against systems you're authorized to test
        - Some tests might cause instability in vulnerable applications
        - Always document findings and report appropriately
        """
    else:
        analysis = """
        This sqlmap command attempts to perform SQL injection testing:
        
        - **-u 'http://example.com/page.php?id=1'**: Target URL with the parameter to test
        - **--dbs**: Enumerate databases if SQL injection is successful
        - **--batch**: Non-interactive mode, uses default answers
        
        **Security implications**:
        - This actively tests for SQL injection vulnerabilities
        - It will attempt to extract database information if successful
        - The scan could generate significant database/application traffic
        
        **Ethical considerations**:
        - Only use against systems you're authorized to test
        - Could potentially modify or corrupt database data
        - May trigger database security controls or denial of service
        - Always document findings and report appropriately
        """
    
    console.print(Markdown(analysis))

def interactive_chat_demo():
    """Demo of interactive chat feature"""
    console.print("\n[bold blue]Interactive Chat Demo[/bold blue]")
    console.print("In this demo, you can chat with a simulated version of KaliAI.")
    console.print("[yellow]This is a simplified demo with pre-programmed responses.[/yellow]")
    console.print("[yellow]Type 'exit' to return to the main menu.[/yellow]\n")
    
    # Sample responses for demo
    sample_responses = {
        "hello": "Hello! I'm KaliAI, your ethical hacking assistant. How can I help you today?",
        "help": "I can help you with Kali Linux tools, explain security concepts, or provide guidance on ethical hacking methodology. Just ask me anything related to cybersecurity!",
        "nmap": "Nmap is a powerful network scanning tool used for discovery and security auditing. It can identify open ports, detect operating systems, and discover services running on a network. Would you like to know about specific nmap commands or techniques?",
        "metasploit": "Metasploit is a penetration testing framework that provides tools for vulnerability development, testing, and exploitation. It's important to use it ethically and only against systems you have permission to test. Would you like to know about specific Metasploit modules or techniques?",
        "ethics": "Ethical hacking follows key principles: obtain proper authorization, respect privacy, minimize damage, document thoroughly, and practice responsible disclosure. Remember that the same skills used for security testing can be harmful if misused - always act within legal and ethical boundaries."
    }
    
    # Interactive chat loop
    while True:
        user_input = Prompt.ask("\nud83dudee1ufe0f ")
        
        if user_input.lower() == 'exit':
            break
        
        # Generate response (simplified for demo)
        response = None
        for key, value in sample_responses.items():
            if key in user_input.lower():
                response = value
                break
        
        if not response:
            response = "I understand you're asking about security or ethical hacking. In a full implementation, I would provide a detailed response about this topic, explaining relevant tools, techniques, and ethical considerations."
        
        console.print(Markdown(response))

if __name__ == "__main__":
    main()

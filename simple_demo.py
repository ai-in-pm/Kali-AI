#!/usr/bin/env python3
"""
KaliAI Demo - Simple Demonstration Script
"""

import os
import sys
import time
from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel

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
        
        # Run automated demo sequence
        automated_demo()
        
    except KeyboardInterrupt:
        console.print("\n[bold blue]Demo terminated. Goodbye![/bold blue]")
        sys.exit(0)

def display_banner():
    """Display welcome banner"""
    banner = """  
     __  __     _ _    _    ___ 
    |  \/  |   | (_)  / \   |_ _|
    | |\/| |_  | |_  / _ \   | | 
    | |  | | |_| | |/ ___ \  | | 
    |_|  |_|\___/|_/_/   \_\|___|
                              
    Ethical Hacking Assistant Demo
    """
    
    console.print(Panel.fit(banner, border_style="blue"))
    console.print("\n[bold]Welcome to the KaliAI Demo![/bold]")
    console.print("This is an automated demonstration of KaliAI,")
    console.print("an ethical hacking assistant specialized in Kali Linux.\n")
    console.print("[yellow]Press Ctrl+C at any time to exit.[/yellow]\n")
    time.sleep(2)

def automated_demo():
    """Run an automated demo sequence"""
    # Tool explanation demo
    console.print("\n[bold blue]DEMO PART 1: Tool Explanation[/bold blue]")
    console.print("KaliAI can provide detailed explanations of security tools.")
    time.sleep(2)
    
    # Show tool explanation for nmap
    console.print("\n[bold]Question:[/bold] Tell me about nmap")
    time.sleep(1)
    tool_name = "nmap"
    tool_info = SAMPLE_TOOLS[tool_name]
    
    console.print(f"\n[bold green]Response:[/bold green]")
    console.print(f"[bold]{tool_name.upper()}[/bold] is a {tool_info['description']}.")
    console.print(f"\nExample usage: `{tool_info['example']}`")
    console.print(f"\nThis command {tool_info['explanation']}")
    
    # Display ethical considerations
    ethical_md = f"""
    When using {tool_name}, always ensure:
    
    1. **Authorization** - Only scan systems you have explicit permission to test
    2. **Documentation** - Keep detailed records of all testing activities
    3. **Scope limitation** - Strictly adhere to the defined scope of testing
    4. **Minimal impact** - Use the least intrusive methods necessary
    
    Remember that unauthorized scanning is illegal in most jurisdictions.
    """
    console.print(Markdown(ethical_md))
    time.sleep(5)
    
    # Command analysis demo
    console.print("\n\n[bold blue]DEMO PART 2: Command Analysis[/bold blue]")
    console.print("KaliAI can analyze security commands and explain what they do.")
    time.sleep(2)
    
    # Sample command for analysis
    selected_cmd = "nmap -sS -T4 -p 1-1000 192.168.1.1"
    
    console.print(f"\n[bold]Question:[/bold] What does this command do: {selected_cmd}")
    time.sleep(1)
    
    console.print(f"\n[bold green]Response:[/bold green]")
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
    console.print(Markdown(analysis))
    time.sleep(5)
    
    # Interactive demo
    console.print("\n\n[bold blue]DEMO PART 3: Security Methodology[/bold blue]")
    console.print("KaliAI can guide users through security testing methodologies.")
    time.sleep(2)
    
    console.print(f"\n[bold]Question:[/bold] How should I approach a web application penetration test?")
    time.sleep(1)
    
    console.print(f"\n[bold green]Response:[/bold green]")
    methodology = """
    # Web Application Penetration Testing Methodology
    
    Here's a structured approach for web application penetration testing:
    
    ## 1. Reconnaissance & Planning
    - Define scope and boundaries
    - Obtain proper authorization
    - Gather public information (OSINT)
    - Identify technologies and frameworks
    
    ## 2. Scanning & Enumeration
    - Discover subdomains and related assets
    - Map application structure
    - Identify entry points
    - Scan for known vulnerabilities
    
    Useful tools: `nmap`, `nikto`, `dirb/gobuster`, `wpscan` (if WordPress)
    
    ## 3. Vulnerability Analysis
    - Test for OWASP Top 10 vulnerabilities
    - Check for misconfigurations
    - Test authentication mechanisms
    - Analyze business logic
    
    Useful tools: `sqlmap`, `burpsuite`, `zaproxy`
    
    ## 4. Exploitation
    - Attempt to exploit discovered vulnerabilities
    - Elevate privileges if possible
    - Test for lateral movement
    - Document impact and attack paths
    
    ## 5. Reporting
    - Document methodology and findings
    - Classify vulnerabilities by severity
    - Provide remediation recommendations
    - Present clear evidence and impact
    
    ## 6. Remediation Support
    - Assist with fixing vulnerabilities
    - Verify fixes and perform retesting
    - Provide guidance on security improvements
    
    Remember to always operate ethically and legally, with proper authorization for all testing activities.
    """
    console.print(Markdown(methodology))
    time.sleep(5)
    
    # Wrap-up
    console.print("\n\n[bold blue]Demo Complete![/bold blue]")
    console.print("\nThis was a simplified demonstration of KaliAI capabilities.")
    console.print("The full implementation provides more features:")
    console.print("- Real-time AI-powered responses")
    console.print("- Secure command execution with analysis")
    console.print("- Detailed tool knowledge for all Kali Linux tools")
    console.print("- Ethical hacking methodology guidance")
    console.print("- Security concept explanations")
    
    console.print("\n[bold green]You can run this demo anytime with:[/bold green]")
    console.print("[bold]python simple_demo.py[/bold]")
    
    console.print("\n[bold blue]Thank you for trying KaliAI![/bold blue]")

if __name__ == "__main__":
    main()

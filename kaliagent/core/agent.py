from typing import Dict, List, Optional, Any
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from ..config.settings import settings
from rich.console import Console
from rich.markdown import Markdown
from datetime import datetime
import subprocess
import json
import logging
from pathlib import Path
import shlex
import os

console = Console()

class KaliAgent:
    """KaliAI - Ethical Hacking Assistant for Kali Linux"""
    
    def __init__(self):
        """Initialize the Kali Linux Ethical Hacking Assistant"""
        self._setup_logging()
        self.agent = Agent(
            model=OpenAIChat(id=settings.MODEL_ID),
            markdown=True,
            introduction=self._load_agent_prompt()
        )
        self.logger.info(f"{settings.APP_NAME} initialized successfully")
        self.history = []
    
    def _setup_logging(self):
        """Configure logging"""
        self.logger = logging.getLogger("kaliagent")
        self.logger.setLevel(settings.LOG_LEVEL)
        
        # File handler
        fh = logging.FileHandler(settings.LOG_DIR / "kaliagent.log")
        fh.setLevel(settings.LOG_LEVEL)
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(settings.LOG_LEVEL)
        
        # Formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    
    def _load_agent_prompt(self) -> str:
        """Load the agent's system prompt"""
        return """You are KaliAI, an ethical hacking assistant specialized in Kali Linux.
        Your primary role is to:
        1. Provide guidance on ethical hacking tools and methodologies
        2. Help users understand and use Kali Linux tools safely
        3. Explain security concepts and best practices
        4. Ensure all activities follow ethical guidelines and legal requirements
        
        When a user asks about executing a command:
        1. Only provide guidance for ethical hacking tools
        2. Always explain what the command does before suggesting its use
        3. Emphasize the importance of having proper authorization
        4. Include safety precautions and best practices
        
        Key tools you can provide guidance on:
        - nmap: Network scanning and enumeration
        - nikto: Web server scanner
        - dirb/gobuster: Directory enumeration
        - wpscan: WordPress security scanner
        - sqlmap: SQL injection testing
        - wireshark: Network protocol analyzer
        - metasploit: Penetration testing framework
        - hydra: Password cracking
        - john: Password cracking
        - hashcat: Password recovery
        - burpsuite: Web application security testing
        - aircrack-ng: Wireless security assessment
        - maltego: Open source intelligence
        - beef: Browser exploitation framework
        - zaproxy: Web application scanning
        
        Always emphasize:
        - Legal and ethical considerations
        - Proper documentation and reporting
        - Safe testing environments
        - Responsible disclosure
        
        Tool usage guidelines:
        1. Always check if a tool is installed before suggesting its use
        2. Provide clear syntax and parameter explanations
        3. Suggest safer alternatives when appropriate
        4. Explain potential consequences and limitations
        5. Recommend appropriate follow-up actions
        
        When executing commands:
        1. Verify the command is related to ethical hacking
        2. Confirm it doesn't pose unintended risks
        3. Get user confirmation before execution
        4. Provide clear interpretation of results
        """
    
    def chat(self, message: str):
        """Process user input and generate responses"""
        try:
            self.logger.info(f"Processing user message: {message[:50]}...")
            
            # Check if this is a command execution request
            is_command, command = self._is_command_request(message)
            
            if is_command and command:
                # Process as command execution request
                self._handle_command_execution(command, message)
            else:
                # Process as normal chat
                response = self.agent.chat(message)
                console.print(Markdown(response))
                
                # Save to history
                self._save_interaction(message, response)
                
        except Exception as e:
            self.logger.error(f"Error during chat: {str(e)}")
            console.print(f"[red]Error: {str(e)}[/red]")
    
    def _is_command_request(self, message: str) -> tuple[bool, Optional[str]]:
        """Determine if the message is requesting command execution"""
        # Common command execution indicators
        indicators = [
            "run", "execute", "launch", "start", 
            "terminal", "command", "cmd", "shell"
        ]
        
        message_lower = message.lower()
        
        # Check if this appears to be a command request
        is_likely_command = any(ind in message_lower for ind in indicators)
        
        # If it looks like a command, ask the AI if it's a command and what it is
        if is_likely_command:
            prompt = f"""
            Is the following user message asking to execute a command? 
            If yes, extract just the command that should be executed.
            If no, reply with 'not a command'.
            
            User message: {message}
            
            Reply with only the command or 'not a command'.
            """
            
            response = self.agent.chat(prompt)
            
            if response.lower().strip() == "not a command":
                return False, None
            else:
                # Extract the command from the response
                return True, response.strip()
        
        return False, None
    
    def _handle_command_execution(self, command: str, original_message: str):
        """Handle execution of a Kali Linux command"""
        # First, validate if this is a security-related command
        is_security_command = self._validate_security_command(command)
        
        if not is_security_command:
            console.print("[red]⚠️ This does not appear to be a security-related command.[/red]")
            console.print("[yellow]KaliAI is designed to assist with ethical hacking tools only.[/yellow]")
            return
            
        # Get explanation of what the command does
        explanation = self._get_command_explanation(command)
        console.print("\n[bold blue]Command Analysis:[/bold blue]")
        console.print(Markdown(explanation))
        
        # Ask for confirmation if required
        if settings.REQUIRE_CONFIRMATION:
            console.print("\n[yellow]Do you want to execute this command? (y/n)[/yellow]")
            confirmation = input("> ").lower().strip()
            if confirmation != 'y':
                console.print("[yellow]Command execution cancelled.[/yellow]")
                return
        
        # Execute command if safe mode is disabled
        if not settings.SAFE_MODE:
            try:
                console.print("\n[bold]Executing command...[/bold]")
                result = subprocess.run(
                    command, 
                    shell=True, 
                    capture_output=True, 
                    text=True
                )
                
                if result.returncode == 0:
                    console.print("\n[green]Command executed successfully[/green]")
                    console.print("\n[bold]Output:[/bold]")
                    console.print(result.stdout)
                    
                    # Get interpretation of results
                    interpretation = self._get_result_interpretation(command, result.stdout)
                    console.print("\n[bold blue]Result Analysis:[/bold blue]")
                    console.print(Markdown(interpretation))
                else:
                    console.print("\n[red]Command execution failed[/red]")
                    console.print("\n[bold]Error:[/bold]")
                    console.print(result.stderr)
                
                # Save to history
                self._save_command_execution(original_message, command, result.stdout, result.stderr)
                
            except Exception as e:
                self.logger.error(f"Error executing command: {str(e)}")
                console.print(f"[red]Error executing command: {str(e)}[/red]")
        else:
            console.print("\n[yellow]Safe mode is enabled. Command will not be executed.[/yellow]")
            console.print(f"[bold]Command that would be executed:[/bold] {command}")
    
    def _validate_security_command(self, command: str) -> bool:
        """Validate if the command is related to security tools"""
        # Extract the base command (first word)
        base_cmd = shlex.split(command)[0] if command else ""
        
        # Check if it's in our allowed tools list
        return base_cmd in settings.ALLOWED_TOOLS
    
    def _get_command_explanation(self, command: str) -> str:
        """Get explanation of what the command does"""
        prompt = f"""
        Explain what the following Kali Linux command does in detail, including:
        1. The purpose of the command
        2. What each parameter/flag does
        3. Potential security implications
        4. Any ethical considerations
        
        Command: {command}
        """
        
        return self.agent.chat(prompt)
    
    def _get_result_interpretation(self, command: str, output: str) -> str:
        """Get interpretation of command results"""
        prompt = f"""
        Analyze the output of this Kali Linux command and explain what it means:
        
        Command: {command}
        
        Output:
        {output[:2000]}  # Limiting output length for token efficiency
        
        Provide:
        1. A summary of what was found
        2. Any security insights from this output
        3. Recommended next steps
        """
        
        return self.agent.chat(prompt)
    
    def _save_interaction(self, message: str, response: str):
        """Save interaction to history"""
        timestamp = datetime.now().isoformat()
        interaction = {
            "timestamp": timestamp,
            "type": "chat",
            "user_message": message,
            "agent_response": response
        }
        
        self.history.append(interaction)
        
        # Save to file
        history_file = settings.HISTORY_DIR / f"chat_{timestamp}.json"
        with open(history_file, 'w') as f:
            json.dump(interaction, f, indent=2)
    
    def _save_command_execution(self, message: str, command: str, output: str, error: str):
        """Save command execution to history"""
        timestamp = datetime.now().isoformat()
        interaction = {
            "timestamp": timestamp,
            "type": "command",
            "user_message": message,
            "command": command,
            "output": output,
            "error": error
        }
        
        self.history.append(interaction)
        
        # Save to file
        history_file = settings.HISTORY_DIR / f"command_{timestamp}.json"
        with open(history_file, 'w') as f:
            json.dump(interaction, f, indent=2)

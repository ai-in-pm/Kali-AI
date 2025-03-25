import click
from rich.console import Console
from .core.agent import KaliAgent
from .config.settings import settings
import os
import sys

console = Console()

@click.group()
def cli():
    """KaliAI - Ethical Hacking Assistant for Kali Linux"""
    pass

@cli.command()
@click.option('--api-key', help='OpenAI API key')
@click.option('--safe-mode/--no-safe-mode', default=True, help='Enable/disable safe mode (no command execution)')
@click.option('--confirm/--no-confirm', default=True, help='Require confirmation before executing commands')
def configure(api_key, safe_mode, confirm):
    """Configure KaliAI settings"""
    if api_key:
        os.environ['OPENAI_API_KEY'] = api_key
        console.print("[green]API key configured successfully[/green]")
    
    # Update settings
    settings.SAFE_MODE = safe_mode
    settings.REQUIRE_CONFIRMATION = confirm
    
    console.print(f"[green]Safe mode: {'Enabled' if safe_mode else 'Disabled'}[/green]")
    console.print(f"[green]Command confirmation: {'Required' if confirm else 'Not required'}[/green]")

@cli.command()
def interactive():
    """Start interactive ethical hacking assistant"""
    try:
        if not os.getenv('OPENAI_API_KEY'):
            console.print("[red]Error: OpenAI API key not found. Use 'kaliagent configure --api-key YOUR_KEY' to set it.[/red]")
            sys.exit(1)
            
        console.print("[bold blue]KaliAI - Ethical Hacking Assistant[/bold blue]")
        console.print("[italic]Type 'exit' to quit[/italic]\n")
        
        agent = KaliAgent()
        
        while True:
            try:
                user_input = input("🛡️ > ")
                if user_input.lower() == 'exit':
                    break
                
                agent.chat(user_input)
                print()
                
            except KeyboardInterrupt:
                break
            except Exception as e:
                console.print(f"[red]Error: {str(e)}[/red]")
        
        console.print("\n[bold blue]Goodbye! Happy ethical hacking![/bold blue]")
        
    except Exception as e:
        console.print(f"[red]Fatal error: {str(e)}[/red]")
        sys.exit(1)

@cli.command()
@click.argument('tool', type=click.Choice(settings.ALLOWED_TOOLS, case_sensitive=False))
def learn(tool):
    """Learn about a specific Kali Linux tool"""
    try:
        agent = KaliAgent()
        
        # Generate prompt to learn about the tool
        prompt = f"Teach me about the {tool} tool in Kali Linux, including its purpose, basic usage, common flags, and security considerations."
        
        # Process through the agent
        agent.chat(prompt)
        
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)

@cli.command()
@click.argument('command', type=str)
def analyze(command):
    """Analyze a Kali Linux command without executing it"""
    try:
        agent = KaliAgent()
        
        # Force safe mode for analysis
        settings.SAFE_MODE = True
        
        # Generate prompt to analyze the command
        prompt = f"Analyze this Kali Linux command: {command}"
        
        # Process through the agent
        agent.chat(prompt)
        
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        sys.exit(1)

def main():
    """Main entry point for the CLI"""
    cli()

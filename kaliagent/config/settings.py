from pydantic_settings import BaseSettings
from typing import Optional, Dict, Any, List
from pathlib import Path
import os

class Settings(BaseSettings):
    """KaliAgent Configuration Settings"""
    
    # API Configuration
    OPENAI_API_KEY: Optional[str] = None
    MODEL_ID: str = "gpt-4"
    
    # Application Settings
    APP_NAME: str = "KaliAI"
    APP_VERSION: str = "1.0.0"
    
    # Storage Settings
    DATA_DIR: Path = Path.home() / ".kaliagent"
    LOG_DIR: Path = DATA_DIR / "logs"
    HISTORY_DIR: Path = DATA_DIR / "history"
    
    # Logging Settings
    ENABLE_LOGGING: bool = True
    LOG_LEVEL: str = "INFO"
    
    # Security Settings
    ALLOWED_TOOLS: List[str] = [
        "nmap", "nikto", "dirb", "gobuster", "wpscan", "sqlmap", 
        "wireshark", "metasploit", "hydra", "john", "hashcat",
        "burpsuite", "aircrack-ng", "maltego", "beef", "zaproxy"
    ]
    
    # Command Execution
    SAFE_MODE: bool = True  # If True, will only display commands but not execute them
    REQUIRE_CONFIRMATION: bool = True  # If True, requires user confirmation before executing commands
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Create necessary directories
        self.DATA_DIR.mkdir(parents=True, exist_ok=True)
        self.LOG_DIR.mkdir(parents=True, exist_ok=True)
        self.HISTORY_DIR.mkdir(parents=True, exist_ok=True)

# Create global settings instance
settings = Settings()

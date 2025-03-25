"""
KaliAgent - Ethical Hacking Assistant for Kali Linux
"""

from .core.agent import KaliAgent
from .config.settings import settings

__version__ = "1.0.0"
__all__ = ['KaliAgent', 'settings']

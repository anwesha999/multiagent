"""
Core framework for simple multi-agent communication.
"""

from agent_framework.bus import MessageBus, Message
from agent_framework.agent import BaseAgent

__all__ = [
    "MessageBus",
    "Message",
    "BaseAgent",
]


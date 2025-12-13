"""
BaseAgent: provides common structure for agents.
Each agent runs an asyncio task loop, consumes messages, and can send via bus.
"""
import asyncio
from typing import Optional, Any
from agent_framework.bus import MessageBus, Message

class BaseAgent:
    def __init__(self, agent_id: str, bus: MessageBus):
        self.agent_id = agent_id
        self.bus = bus
        self.queue: Optional[asyncio.Queue] = None
        self._task: Optional[asyncio.Task] = None
        self.running = False

    async def start(self):
        self.queue = await self.bus.register(self.agent_id)
        self.running = True
        self._task = asyncio.create_task(self._run_loop())
        print(f"[{self.agent_id}] started")

    async def stop(self):
        self.running = False
        if self._task:
            await self._task
        await self.bus.unregister(self.agent_id)
        print(f"[{self.agent_id}] stopped")

    async def _run_loop(self):
        while self.running:
            try:
                if self.queue is not None:
                    msg: Message = await self.queue.get()
                    await self.handle_message(msg)
            except Exception as e:
                print(f"[{self.agent_id}] error in run loop: {e}")

    async def handle_message(self, msg: Message):
        """Override in subclass"""
        print(f"[{self.agent_id}] received: {msg}")

    async def send(self, to: str, type: str, payload: Any):
        msg = Message(sender=self.agent_id, to=to, type=type, payload=payload)
        await self.bus.send(msg)


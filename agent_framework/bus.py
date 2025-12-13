"""
A very small message bus based on asyncio. Agents send messages to the bus
which routes them to recipient queues (or broadcasts).
"""
import asyncio
from typing import Dict, Any, Callable, List

class Message:
    def __init__(self, sender: str, to: str, type: str, payload: Any):
        self.sender = sender
        self.to = to  # recipient agent id or '*' for broadcast
        self.type = type
        self.payload = payload

    def __repr__(self):
        return f"Message(from={self.sender}, to={self.to}, type={self.type}, payload={self.payload})"

class MessageBus:
    def __init__(self):
        self.queues: Dict[str, asyncio.Queue] = {}
        self.lock = asyncio.Lock()

    async def register(self, agent_id: str) -> asyncio.Queue:
        async with self.lock:
            q = asyncio.Queue()
            self.queues[agent_id] = q
            return q

    async def unregister(self, agent_id: str):
        async with self.lock:
            q = self.queues.pop(agent_id, None)
            if q:
                # drain queue
                while not q.empty():
                    _ = q.get_nowait()

    async def send(self, msg: Message):
        """Route message to the recipient(s)."""
        async with self.lock:
            if msg.to == "*":
                for q in self.queues.values():
                    await q.put(msg)
            else:
                q = self.queues.get(msg.to)
                if q is None:
                    # unknown recipient — drop or log
                    # for demo, print
                    print(f"[bus] unknown recipient: {msg.to}")
                else:
                    await q.put(msg)


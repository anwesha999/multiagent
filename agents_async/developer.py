"""
Developer agent: takes tasks and produces "artifacts" then notifies tester.
"""
import asyncio
import random
from agent_framework.agent import BaseAgent

class DeveloperAgent(BaseAgent):
    async def handle_message(self, msg):
        print(f"[Developer] got {msg}")
        if msg.type == "task":
            task = msg.payload
            # simulate work
            await asyncio.sleep(random.uniform(0.2, 0.8))
            artifact = {"task_id": task["task_id"], "artifact": f"code-for-{task['task_id']}"}
            # send artifact to integrator/tester
            await self.send(to="tester", type="artifact", payload=artifact)


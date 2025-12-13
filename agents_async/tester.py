"""
Tester agent: runs simple verification on artifacts and responds pass/fail.
"""
import asyncio
from agent_framework.agent import BaseAgent

class TesterAgent(BaseAgent):
    async def handle_message(self, msg):
        print(f"[Tester] received {msg}")
        if msg.type == "artifact":
            art = msg.payload
            # trivial check
            passed = "code" in art.get("artifact", "")
            result = {"task_id": art["task_id"], "passed": passed}
            # notify planner (or manager)
            await self.send(to="planner", type="test_result", payload=result)


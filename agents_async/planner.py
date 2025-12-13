"""
Planner agent: receives high-level goals and emits tasks for developer agents.
"""
import asyncio
from agent_framework.agent import BaseAgent

class PlannerAgent(BaseAgent):
    async def handle_message(self, msg):
        print(f"[Planner] handling {msg}")
        if msg.type == "goal":
            goal = msg.payload
            # very naive decomposition: split goal into subtasks
            subtasks = self.decompose(goal)
            # send tasks to developer(s)
            for i, t in enumerate(subtasks, start=1):
                task_id = f"{goal['id']}-task-{i}"
                payload = {"task_id": task_id, "spec": t}
                await self.send(to="developer", type="task", payload=payload)

    def decompose(self, goal):
        # demo: if goal asks for 'website', produce tasks
        if goal.get("type") == "build_website":
            return [
                {"role": "ui", "desc": "create landing page"},
                {"role": "api", "desc": "create orders API"},
                {"role": "ci", "desc": "add CI pipeline"},
            ]
        return [{"role": "misc", "desc": goal.get("desc", "task")}]


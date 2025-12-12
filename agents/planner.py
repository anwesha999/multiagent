from agents.base_agent import BaseAgent

class PlannerAgent(BaseAgent):
    def plan(self, goal: str):
        prompt = f"""
        As a Planner Agent, break the following goal into 3–7 clear steps:

        Goal: {goal}
        """
        return self.think(prompt)


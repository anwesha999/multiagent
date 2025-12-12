from agents.base_agent import BaseAgent

class WorkerAgent(BaseAgent):
    def work(self, task: str):
        prompt = f"""
        As a Worker Agent, execute this task and return the result:

        Task: {task}
        """
        return self.think(prompt)


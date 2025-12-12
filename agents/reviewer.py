from agents.base_agent import BaseAgent

class ReviewerAgent(BaseAgent):
    def review(self, output: str):
        prompt = f"""
        As a Reviewer Agent, improve and correct the following output:

        {output}
        """
        return self.think(prompt)


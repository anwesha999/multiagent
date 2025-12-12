from llm_client import ask_llm

class BaseAgent:
    def __init__(self, name):
        self.name = name

    def think(self, task: str):
        prompt = f"You are {self.name}. Your task is: {task}. Return only useful output."
        return ask_llm(prompt)


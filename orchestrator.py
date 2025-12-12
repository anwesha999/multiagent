from agents.planner import PlannerAgent
from agents.worker import WorkerAgent
from agents.reviewer import ReviewerAgent

class Orchestrator:
    def __init__(self):
        self.planner = PlannerAgent("Planner")
        self.worker = WorkerAgent("Worker")
        self.reviewer = ReviewerAgent("Reviewer")

    def execute(self, goal: str):
        print("\n🧠 Planning...")
        plan = self.planner.plan(goal)
        print(plan)

        print("\n⚡ Executing...")
        result = self.worker.work(plan)
        print(result)

        print("\n🔍 Reviewing...")
        reviewed = self.reviewer.review(result)
        print(reviewed)

        return reviewed


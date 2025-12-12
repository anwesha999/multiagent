from orchestrator import Orchestrator

if __name__ == "__main__":
    goal = "Create a summary on why multi-agent systems are useful."
    orchestrator = Orchestrator()
    output = orchestrator.execute(goal)

    print("\n\nFinal Output:")
    print(output)


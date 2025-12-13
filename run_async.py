"""
Run an example multi-agent scenario using async message bus.
"""
import asyncio
from agent_framework.bus import MessageBus, Message
from agents_async.planner import PlannerAgent
from agents_async.developer import DeveloperAgent
from agents_async.tester import TesterAgent

async def main():
    bus = MessageBus()

    planner = PlannerAgent("planner", bus)
    developer = DeveloperAgent("developer", bus)
    tester = TesterAgent("tester", bus)

    # start agents
    await planner.start()
    await developer.start()
    await tester.start()

    # send a goal to planner
    goal = {"id": "g-001", "type": "build_website", "desc": "simple hotel booking site"}
    await bus.send(Message(sender='user', to='planner', type='goal', payload=goal))

    # run for a short while
    await asyncio.sleep(3)

    # stop agents
    await planner.stop()
    await developer.stop()
    await tester.stop()

if __name__ == '__main__':
    asyncio.run(main())


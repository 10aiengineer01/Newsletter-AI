from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class EmailComposerAgent(Agent):
    def __init__(self):
        super().__init__(
            name="EmailComposerAgent",
            description="Compiles AI news content and images into a newsletter and manages its distribution for AINewsletterAgency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )

from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class ImageGeneratorAgent(Agent):
    def __init__(self):
        super().__init__(
            name="ImageGeneratorAgent",
            description="Generates visually appealing images corresponding to AI news topics for AINewsletterAgency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )

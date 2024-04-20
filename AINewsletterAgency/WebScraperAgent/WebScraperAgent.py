from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class WebScraperAgent(Agent):
    def __init__(self):
        super().__init__(
            name="WebScraperAgent",
            description="Searches and extracts AI news from the web for AINewsletterAgency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )

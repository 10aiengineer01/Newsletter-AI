from agency_swarm.agents import Agent
from agency_swarm.tools import CodeInterpreter

class EmailFormater(Agent):
    def __init__(self):
        super().__init__(
            name="EmailFormater",
            description="Formats the newsletter content provided by the webscraper",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[CodeInterpreter],
            tools_folder="./tools"
        )

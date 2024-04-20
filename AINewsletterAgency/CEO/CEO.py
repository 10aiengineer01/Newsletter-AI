from agency_swarm.agents import Agent


class CEO(Agent):
    def __init__(self):
        super().__init__(
            name="CEO",
            description="Coordinates the entire newsletter creation process for AINewsletterAgency.",
            instructions="./instructions.md",
            files_folder="./files",
            schemas_folder="./schemas",
            tools=[],
            tools_folder="./tools"
        )

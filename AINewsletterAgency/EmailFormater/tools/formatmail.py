from agency_swarm.tools import BaseTool
from pydantic import Field

class formatmail(BaseTool):
    """
    Saves the text for the newsletter
    """

    subject: str = Field(
        ..., description="Select the Section you are currently writing: TITLE, INTRODUCTION, SUBTITLE, SUBTITLE-TEXT, CONCLUSION"
    )

    content: str = Field(
        ..., description="The content for this section"
    )
    
    def run(self) -> str:
        """
        Updates the shared state with the provided subject and content.
        """
        valid_subjects = {"TITLE", "INTRODUCTION", "SUBTITLE", "SUBTITLE-TEXT", "CONCLUSION"}
        
        if self.subject in valid_subjects:
            p_content = self.shared_state.get("content", {})
            
            if self.subject in p_content:
                if self.subject == "SUBTITLE" or self.subject == "SUBTITLE-TEXT":
                    if isinstance(p_content[self.subject], list):
                        p_content[self.subject].append(self.content)
                    else:
                        p_content[self.subject] = [self.content]
                else:
                    p_content[self.subject] = self.content
            else:
                if self.subject == "SUBTITLE" or self.subject == "SUBTITLE-TEXT":
                    p_content[self.subject] = [self.content]
                else:
                    p_content[self.subject] = self.content
            
            self.shared_state.set("content", p_content)
        else:
            return "Please select one of these keywords to continue: TITLE, INTRODUCTION, SUBTITLE, SUBTITLE-TEXT, CONCLUSION"

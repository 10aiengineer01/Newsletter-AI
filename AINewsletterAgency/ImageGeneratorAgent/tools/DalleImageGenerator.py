from agency_swarm.tools import BaseTool
from pydantic import Field
from openai import OpenAI
from datetime import datetime
import base64
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
grandparent_dir = os.path.dirname(parent_dir)
sys.path.append(grandparent_dir)

from agency import openai_api_key

class DalleImageGenerator(BaseTool):
    """
    Generates images based on a prompt using OpenAI's DALL·E.
    """
    prompt: str = Field(
        ..., description="The prompt to generate an image for."
    )
    
    def run(self) -> str:
        """
        Generates an image based on the provided prompt and returns the URL of the generated image.
        """
        client = OpenAI(api_key=openai_api_key)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"bild_{timestamp}.png"
        save_path = "."
        save_path = f"{save_path}/{file_name}"
        response = client.images.generate(
        model="dall-e-3",
        prompt=self.prompt,
        size="1024x1024",
        quality="standard",
        n=1,
        response_format="b64_json"
        )

        try:
            self.save_image(response.data[0].b64_json, save_path)
            return "Image was created and saved. Report back that you can continue with the next image"
        except:
            return "Issue while creating image"
        
    def save_image(self, image_data, file_name):
        paths = []
        with open(file_name, "wb") as f:
            f.write(base64.b64decode(image_data))
            f.close()
        self.shared_state.set(file_name, os.path.abspath(file_name))
        old_paths = self.shared_state.get("image_paths")
        paths.append(file_name)
        if isinstance(old_paths, list):
            paths = paths+old_paths
            self.shared_state.set("image_paths", paths)
        else:
            self.shared_state.set("image_paths", paths)

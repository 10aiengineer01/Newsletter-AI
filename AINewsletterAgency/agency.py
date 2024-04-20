from agency_swarm import Agency
from agency_swarm import set_openai_key
from EmailComposerAgent import EmailComposerAgent
from ImageGeneratorAgent import ImageGeneratorAgent
from WebScraperAgent import WebScraperAgent
from EmailFormater import EmailFormater
from CEO import CEO
from agency_swarm.util.oai import set_openai_client
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv('OPENAIAK')
browserless_api = os.getenv('BROWSERLESS')
# uses outlook smtp server
email = os.getenv('EMAIL')
password = os.getenv('EMAIL_PASSWORD')

client = OpenAI(
    timeout=300.0,
)

set_openai_client(client)

set_openai_key(openai_api_key)

ceo = CEO()
webScraperAgent = WebScraperAgent()
imageGeneratorAgent = ImageGeneratorAgent()
emailComposerAgent = EmailComposerAgent()
emailFormater = EmailFormater()

agency = Agency([ceo, [ceo, webScraperAgent],
                 [webScraperAgent, imageGeneratorAgent],
                 [webScraperAgent, emailFormater],
                 [webScraperAgent, ceo],
                 [ceo, emailComposerAgent]],
                shared_instructions='./agency_manifesto.md')

if __name__ == '__main__':
    agency.demo_gradio()

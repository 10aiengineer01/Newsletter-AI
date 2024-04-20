# AI-Newsletter

## About the Project

The AI-Newsletter project is an advanced AI agency capable of automatically creating newsletters based on textual input. Utilizing cutting-edge AI technology, the agency can gather relevant information from the internet, create images for each topic, appropriately format the content, and then dispatch it as a finished newsletter directly to one's own email address. The result is a fully automated newsletter process.

## Features

- **Automated Creation:** Generation of newsletters based on specified topics or interests.
- **Content Search:** Automatic collection of information using DuckDuckGo and Browserless API.
- **Image Generation:** Creation of topic-related images for each newsletter.
- **Formatting and Dispatch:** Professional formatting of the newsletter and dispatch via an Outlook SMTP server.

## Technologies and Tools

- **Agency-Swarm Python Library:** For the creation of the agent workflow.
- **OpenAI Assistants API:** Utilization of OpenAI technology for generated content.
- **DuckDuckGo and Browserless API:** For internet information retrieval.
- **Outlook SMTP Server:** For email dispatch.
- **Gradio:** For the web ui

## Installation and Setup

To use the AI-Newsletter project, follow these steps:

1. **Create a virtual Python environment:**

```bash
python -m venv venv
source venv/bin/activate  # For Unix/Linux/MacOS
venv\\Scripts\\activate     # For Windows
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Configure environment variables:**

Create a .env file in the project's root directory with the following contents:

```bash
OPENAIAK="YOUR_OPENAI_API_KEY"
BROWSERLESS="YOUR_BROWSERLESS_API_KEY"
EMAIL="YOUR_OUTLOOK_EMAIL"
EMAIL_PASSWORD="YOUR_OUTLOOK_PASSWORD"
```

Replace the placeholders accordingly.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

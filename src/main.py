from dotenv import load_dotenv
from os import getenv

from chat import ChatApp
from model import SQLAgent


# Load API Key
load_dotenv()
api_key = getenv("API_KEY")
model_name = getenv("MODEL")

# Call agent and app
agent = SQLAgent(api_key=api_key, model_name=model_name)
chat_app = ChatApp(agent.app)
# Run app
chat_app.run()

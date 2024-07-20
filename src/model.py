from os import getenv
from dotenv import load_dotenv

from langgraph.checkpoint import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase

from prompts import system_message


# Load API Key
load_dotenv()
api_key = getenv("API_KEY")


# Model setup
model = ChatOpenAI(openai_api_key=api_key)

# Add database and tools to interact with sql databases
db = SQLDatabase.from_uri("sqlite:///../data/form_d_database.db")
toolkit = SQLDatabaseToolkit(db=db, llm=model)
tools = toolkit.get_tools()

# Memory for chatbot
memory = MemorySaver()

# Applies memory and tools to model
app = create_react_agent(
    model, tools, state_modifier=system_message, checkpointer=memory
)

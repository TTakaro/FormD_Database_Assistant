from os import getenv
from dotenv import load_dotenv

from langgraph.checkpoint import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase

from prompts import system_message


class SQLAgent:
    def __init__(self, api_key, model_name):
        # Model setup
        self.model = ChatOpenAI(openai_api_key=api_key, model=model_name)

        # Add database and tools to interact with sql databases
        self.db = SQLDatabase.from_uri("sqlite:///../data/form_d_database.db")
        toolkit = SQLDatabaseToolkit(db=self.db, llm=self.model)
        self.tools = toolkit.get_tools()

        # Memory for chatbot
        self.memory = MemorySaver()

        # Applies memory and tools to model
        self.app = create_react_agent(
            self.model, self.tools, state_modifier=system_message, checkpointer=self.memory
        )

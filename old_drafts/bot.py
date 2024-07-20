from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.checkpoint import MemorySaver
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
from os import getenv
import streamlit as st

#db = SQLDatabase.from_uri("sqlite:///../data/form_d_database.db") #"sqlite:///Chinook.db")
#print(db.dialect)
#print(db.get_usable_table_names())
#response = db.run("SELECT * FROM issuers LIMIT 10;")
#print(response)

# Model setup
load_dotenv()
api_key = getenv("API_KEY")
model = ChatOpenAI(openai_api_key=api_key)

#tools = [db_tool]
db = SQLDatabase.from_uri("sqlite:///../data/form_d_database.db")
#db = "../data/form_d_database.db"
toolkit = SQLDatabaseToolkit(db=db, llm=model)
tools = toolkit.get_tools()



#chain = create_sql_query_chain(model, db)
#response = chain.invoke({"question": "How many employees are there"})
#resp_db = db.run(response)
#print(resp_db)


#from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool

#execute_query = QuerySQLDataBaseTool(db=db)
#write_query = create_sql_query_chain(model, db)
#chain = write_query | execute_query
#response = chain.invoke({"question": "How many employees are there"})
#print(response)


from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

#answer_prompt = PromptTemplate.from_template(
#    """Given the following user question, corresponding SQL query, and SQL result, answer the user question.
#
#Question: {question}
#SQL Query: {query}
#SQL Result: {result}
#Answer: """
#)

#chain = (
#    RunnablePassthrough.assign(query=write_query).assign(
#        result=itemgetter("query") | execute_query
#    )
#    | answer_prompt
#    | model
#    | StrOutputParser()
#)

#response = chain.invoke({"question": "How many employees are there"})
#print(response)


SQL_PREFIX = """You are an agent designed to interact with a SQL database.
Given an input question, create a syntactically correct SQLite query to run, then look at the results of the query and return the answer.
Unless the user specifies a specific number of examples they wish to obtain, always limit your query to at most 5 results.
You can order the results by a relevant column to return the most interesting examples in the database.
Never query for all the columns from a specific table, only ask for the relevant columns given the question.
You have access to tools for interacting with the database.
Only use the below tools. Only use the information returned by the below tools to construct your final answer.
You MUST double check your query before executing it. If you get an error while executing a query, rewrite the query and try again.

DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.

To start you should ALWAYS look at the tables in the database to see what you can query.
Do NOT skip this step.
Then you should query the schema of the most relevant tables."""

system_message = SystemMessage(content=SQL_PREFIX)

#agent_executor = create_react_agent(model, tools, messages_modifier=system_message)


# Streamlit setup
st.set_page_config(page_title="Chat Prototype")
st.title("Chat Prototype")

@st.cache_resource
def memory_func():
    return MemorySaver()

# Create a button to reset chat history
if ("messages" not in st.session_state) or (st.sidebar.button("Reset chat history")):
    st.session_state["messages"] = []
    st.session_state["messages"].append({"role": "assistant", "content": "How can I help you?"})

# Applies memory and tools to model
memory = memory_func()
app = create_react_agent(
    model, tools, messages_modifier=system_message, checkpointer=memory
)

config = {"configurable": {"thread_id": "test-thread"}}


#for s in agent_executor.stream(
#    {"messages": [HumanMessage(content="Where are offerings originating from geographically? How has this changed over time?")]}
	#{"messages": [HumanMessage(content="What are the most prevalent industry sectors represented?")]}
    #{"messages": [HumanMessage(content="What were the most frequently used federal exemptions?")]}
#):
#    print(s)
#    print("----")




# Streamlit rendering
# Display old messages
for message in st.session_state["messages"]:
    role = message["role"]
    content = message["content"]
    with st.chat_message(role):
        st.markdown(content)

if prompt := st.chat_input(placeholder="Ask me about the database"):
    st.session_state["messages"].append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)


    response = app.stream({"messages": [("user", prompt)]}, config, stream_mode="updates")
    #response = app.invoke({"messages": [("user", prompt)]}, config)

    with st.chat_message("assistant"):
        tool_use = False

        st.markdown(response)
        for step in response:
            #st.write_stream(step)

            key = next(iter(step))
            msg = step[key]["messages"][0]

            # Displays tool name and message in a dropdown
            if tool_use:
                with st.status(f'**{name}**: {query}', state="complete"):
                    st.write(msg.content.replace("$", "\\$"))
                    st.session_state["messages"].append({"role": "assistant", "content": msg.content.replace("$", "\\$")})
                    tool_use = False

            # Displays message in main window
            #else:
            st.write(msg.content.replace("$", "\\$"))
            st.session_state["messages"].append({"role": "assistant", "content": msg.content.replace("$", "\\$")})

            # When a message is blank, the next one is the tool message
            if msg.content == "":
                name = msg.tool_calls[0]["name"]
                try:
                    query = msg.tool_calls[0]["args"]["__arg1"]
                except KeyError as err:
                    print(err)
                    query = msg.tool_calls[0]["args"]
                tool_use = True



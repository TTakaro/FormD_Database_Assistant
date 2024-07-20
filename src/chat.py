import streamlit as st
from model import app


# Streamlit setup
st.set_page_config(page_title="Chat Prototype")
st.title("Chat Prototype")


# Defines a thread id for the checkpointer
config = {"configurable": {"thread_id": "test-thread"}}


# Streamlit rendering
# Create a button to reset chat history
if ("messages" not in st.session_state) or (st.sidebar.button("Reset chat history")):
    st.session_state["messages"] = []
    # Starts the chat with a first message from the assistant
    st.session_state["messages"].append({"role": "assistant", "content": "How can I help you?"})

# Display old messages
for message in st.session_state["messages"]:
    role = message["role"]
    content = message["content"]
    with st.chat_message(role):
        st.markdown(content)

# Creates a window for user to type and start conversation
if prompt := st.chat_input(placeholder="Ask me about the database"):
    # Saves user message to streamlit message history
    st.session_state["messages"].append({"role": "user", "content": prompt})
    # Renders user message
    st.chat_message("user").write(prompt)

    # Generates response from model as a stream
    response = app.stream({"messages": [("user", prompt)]}, config, stream_mode="updates")

    # Assumes streamlit user avatar "assistant"
    with st.chat_message("assistant"):
        # Initializes as false, will set to true when tools are called
        tool_use = False

        for step in response:
            # Extracts message info
            key = next(iter(step))
            msg = step[key]["messages"][0]

            # Displays tool name and message in a dropdown
            if tool_use:
                # Writes message in dropdown
                with st.status(f'**{name}**: {query}', state="complete"):
                    # Fixes an annoyance with rendering $ without triggering latex
                    st.write(msg.content.replace("$", "\\$"))
                    # Saves message to streamlit history
                    st.session_state["messages"].append({"role": "assistant", "content": msg.content.replace("$", "\\$")})
                    tool_use = False

            # Displays message in main window
            else:
                st.write(msg.content.replace("$", "\\$"))
                st.session_state["messages"].append({"role": "assistant", "content": msg.content.replace("$", "\\$")})

            # When a message is blank, the next one is the tool message
            if msg.content == "":
                # Save the name of the tool called to render on dropdown bar
                name = msg.tool_calls[0]["name"]
                # Save the query sent to the tool (and handle exceptions from weird tools)
                try:
                    query = msg.tool_calls[0]["args"]
                except KeyError as err:
                    print(err)
                    query = msg.tool_calls[0]["args"]["__arg1"]
                # Next message will be from tool call, so we want to render in dropdown
                tool_use = True

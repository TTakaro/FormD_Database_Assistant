from langchain_core.runnables.base import Runnable
from langchain_core.messages.ai import AIMessage
import streamlit as st


class ChatApp:
    def __init__(self, model: Runnable):
        # Assigns model to app
        self.model = model
        # Streamlit setup
        st.set_page_config(page_title="Database Assistant")
        st.title("Database Assistant")
        self.reset()

    def reset(self) -> None:
        st.session_state["messages"] = []
        st.session_state["messages"].append({"role": "assistant", "content": "How can I help you?"})

    def display_old_messages(self) -> None:
        # This doesn't work yet
        for message in st.session_state["messages"]:
            role = message["role"]
            content = message["content"]
            with st.chat_message(role):
                st.markdown(content)

    def handle_user_input(self, prompt: str) -> None:
        # Saves user message to streamlit state and displays
        st.session_state["messages"].append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        #response = self.analyzer.process_query(prompt)

        # Defines a thread id for the checkpointer
        config = {"configurable": {"thread_id": "test-thread"}}

        # Generates response from model as a stream
        response = self.model.stream({"messages": [("user", prompt)]}, config, stream_mode="updates")

        # Assumes streamlit user avatar "assistant"
        with st.chat_message("assistant"):
            for step in response:
                # Extracts message info
                key = next(iter(step))
                msg = step[key]["messages"][0]
                # Fixes an annoyance with rendering $ without triggering latex
                content = msg.content.replace("$", "\\$")

                # Avoids interacting with non-AIMessage type calls
                if type(msg) == AIMessage:
                    # If theres a toolcall, create a dropdown for the tool message
                    if msg.tool_calls:
                        # Writes message in dropdown
                        name = msg.tool_calls[0]["name"]
                        query = msg.tool_calls[0]["args"]
                        with st.status(f'**{name}**: {query}', state="complete"):
                            st.write(content)
                            # Saves message to streamlit history
                            st.session_state["messages"].append(
                                {"role": "assistant", "content": content})
                    # Otherwise, display in main body
                    else:
                        st.write(content)
                        st.session_state["messages"].append({"role": "assistant", "content": content})


    def run(self) -> None:
        # Reset chat history
        if "messages" not in st.session_state or st.sidebar.button("Reset chat history"):
            self.reset()

        # Display old messages
        self.display_old_messages()

        # Respond to user input
        if prompt := st.chat_input(placeholder="Ask me about the database"):
            self.handle_user_input(prompt)

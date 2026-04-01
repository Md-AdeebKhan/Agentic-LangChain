import streamlit as st
from agents.agent import agent

st.set_page_config(page_title="Agentic AI Assistant", layout="wide")

st.title("🤖 Agentic AI Assistant")
st.caption("AI assistant with tool usage (Search + Weather)")

# ---------- CHAT HISTORY ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- DISPLAY OLD MESSAGES ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- USER INPUT ----------
prompt = st.chat_input("Ask something...")

if prompt:

    # show user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # assistant response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            response = agent.invoke(
                {
                    "messages": st.session_state.messages
                }
            )

            answer = response["messages"][-1].content

            st.markdown(answer)

    # save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )
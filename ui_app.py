"""
Streamlit Web UI for Multi-Agentic AI (Ollama + Llama3)
Run with: streamlit run ui_app.py
"""

import streamlit as st
from orchestrator import Orchestrator

st.set_page_config(page_title="Multi-Agent AI", layout="centered")

st.title("🤖 Multi‑Agentic AI (Ollama + Llama3)")
st.markdown("Fully local multi-agent system with Planner → Worker → Reviewer")

# Input goal
goal = st.text_area(
    "Enter your goal",
    placeholder="Example: Design a hotel booking system architecture"
)

if "orchestrator" not in st.session_state:
    st.session_state.orchestrator = Orchestrator()

if st.button("Run Agents"):
    if not goal.strip():
        st.warning("Please enter a goal")
    else:
        with st.spinner("Planner is thinking..."):
            plan = st.session_state.orchestrator.planner.plan(goal)
        st.subheader("🧠 Planner Output")
        st.code(plan)

        with st.spinner("Worker is executing..."):
            result = st.session_state.orchestrator.worker.work(plan)
        st.subheader("⚙️ Worker Output")
        st.code(result)

        with st.spinner("Reviewer is reviewing..."):
            reviewed = st.session_state.orchestrator.reviewer.review(result)
        st.subheader("🔍 Reviewer Output (Final)")
        st.success(reviewed)


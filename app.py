import streamlit as st

st.set_page_config(page_title="Needle Movers", layout="wide")
st.title("Needle Movers")

# Day-type toggle
day_type = st.radio("Day type", ["Normal", "Low-capacity", "High-capacity"], horizontal=True)

buckets = ["Survive & Stabilize", "Build & Grow", "Create & Share", "Family & Self"]
tabs = st.tabs(buckets + ["Wins"])

# Temporary in-memory storage just to test the UI
if "tasks" not in st.session_state:
    st.session_state.tasks = {b: [] for b in buckets}

for i, bucket in enumerate(buckets):
    with tabs[i]:
        st.subheader(bucket)
        new_task = st.text_input(f"Add a task to {bucket}", key=f"input_{bucket}")
        if st.button("Add", key=f"add_{bucket}"):
            if new_task:
                st.session_state.tasks[bucket].append(new_task)
        for task in st.session_state.tasks[bucket]:
            st.checkbox(task, key=f"{bucket}_{task}")

with tabs[-1]:
    st.subheader("Wins")
    win = st.text_area("Log a win")
    if st.button("Save win"):
        st.success("Win logged (not yet saved permanently — that's Phase 2.3)")
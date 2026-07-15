import streamlit as st
from database import get_tasks, add_task, toggle_task, add_win, get_wins

st.set_page_config(page_title="Needle Movers", layout="wide")
st.title("Needle Movers")

day_type = st.radio("Day type", ["Normal", "Low-capacity", "High-capacity"], horizontal=True)

buckets = ["Survive & Stabilize", "Build & Grow", "Create & Share", "Family & Self"]
tabs = st.tabs(buckets + ["Wins"])

for i, bucket in enumerate(buckets):
    with tabs[i]:
        st.subheader(bucket)
        new_task = st.text_input(f"Add a task to {bucket}", key=f"input_{bucket}")
        if st.button("Add", key=f"add_{bucket}"):
            if new_task:
                add_task(bucket, day_type, new_task)
                st.rerun()
        for task in get_tasks(bucket):
            checked = st.checkbox(task["task_text"], value=task["is_done"], key=f"task_{task['id']}")
            if checked != task["is_done"]:
                toggle_task(task["id"], checked)

with tabs[-1]:
    st.subheader("Wins")
    win = st.text_area("Log a win")
    if st.button("Save win"):
        if win:
            add_win(win)
            st.success("Win logged!")
    for w in get_wins():
        st.write(f"• {w['note']}")
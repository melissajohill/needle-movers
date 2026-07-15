import streamlit as st
from database import get_tasks, add_task, toggle_task, toggle_blocked, add_win, get_wins

st.set_page_config(page_title="Needle Movers", layout="wide")
st.title("Needle Movers")

day_type = st.radio("Day type", ["Normal", "Low-capacity", "High-capacity"], horizontal=True)

buckets = ["Survive & Stabilize", "Build & Grow", "Create & Share", "Family & Self"]
tabs = st.tabs(buckets + ["Wins"])

for i, bucket in enumerate(buckets):
    with tabs[i]:
        st.subheader(bucket)

        with st.form(key=f"form_{bucket}", clear_on_submit=True):
            new_task = st.text_input("Add a task", key=f"input_{bucket}")
            submitted = st.form_submit_button("Add")
            if submitted and new_task:
                add_task(bucket, day_type, new_task)
                st.rerun()

        for task in get_tasks(bucket, day_type):
            col1, col2 = st.columns([4, 1])
            with col1:
                checked = st.checkbox(task["task_text"], value=task["is_done"], key=f"task_{task['id']}")
                if checked != task["is_done"]:
                    toggle_task(task["id"], checked)
                    if checked:
                         add_win(f"Completed: {task['task_text']}")
                    st.rerun()
            with col2:
                blocked = st.checkbox("🚧 Blocked", value=task.get("is_blocked", False), key=f"blocked_{task['id']}")
                if blocked != task.get("is_blocked", False):
                    toggle_blocked(task["id"], blocked)

with tabs[-1]:
    st.subheader("Wins")
    win = st.text_area("Log a win")
    if st.button("Save win"):
        if win:
            add_win(win)
            st.success("Win logged!")
    for w in get_wins():
        st.write(f"• {w['note']}")
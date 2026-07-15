import streamlit as st
from supabase import create_client

@st.cache_resource
def get_client():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

def get_tasks(bucket, day_type):
    client = get_client()
    result = client.table("tasks").select("*").eq("bucket", bucket).eq("day_type", day_type).execute()
    return result.data

def add_task(bucket, day_type, text):
    client = get_client()
    client.table("tasks").insert({
        "bucket": bucket, "day_type": day_type, "task_text": text,
        "is_pinned": False, "is_done": False
    }).execute()

def toggle_task(task_id, is_done):
    client = get_client()
    client.table("tasks").update({"is_done": is_done}).eq("id", task_id).execute()

def add_win(note):
    client = get_client()
    client.table("wins").insert({"note": note}).execute()

def get_wins():
    client = get_client()
    result = client.table("wins").select("*").order("created_at", desc=True).execute()
    return result.data

def toggle_blocked(task_id, is_blocked):
    client = get_client()
    client.table("tasks").update({"is_blocked": is_blocked}).eq("id", task_id).execute()
    
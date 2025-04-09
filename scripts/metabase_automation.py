import os
import requests
from dotenv import load_dotenv

load_dotenv()

def create_metabase_dashboard(**kwargs):
    session = requests.post(
        f"{os.getenv('METABASE_HOST')}/api/session",
        json={
            "username": os.getenv("METABASE_USER"),
            "password": os.getenv("METABASE_PASSWORD")
        }
    )
    session.raise_for_status()
    token = session.json()["id"]
    headers = {"X-Metabase-Session": token}

    # Create a dashboard
    response = requests.post(
        f"{os.getenv('METABASE_HOST')}/api/dashboard",
        json={"name": "DOB Dashboard (Airflow)"},
        headers=headers
    )
    response.raise_for_status()
    dashboard = response.json()

    print(f" Dashboard created: {dashboard['name']} (id: {dashboard['id']})")

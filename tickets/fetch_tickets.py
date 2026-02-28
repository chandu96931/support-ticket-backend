import requests
import sys
import os

# Add backend folder to sys.path so we can import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import TICKETS_API_URL, API_TOKEN

def get_tickets():
    """
    Fetch tickets from the API using JWT token for authorization.
    Returns the tickets JSON if successful, otherwise prints error.
    """
    headers = {
        "Authorization": f"Bearer {API_TOKEN.strip()}"  # removes invisible spaces
    }

    response = requests.get(TICKETS_API_URL, headers=headers)

    if response.status_code == 200:
        return response.json()  # returns tickets data
    else:
        print("Error:", response.status_code, response.text)
        return None
import sys
import os
import requests

# ---- Fix Python import path ----
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# ---- Now import your config ----
from config.config import TICKETS_API_URL, API_TOKEN

# ---- Authorization header ----
headers = {"Authorization": f"Bearer {API_TOKEN.strip()}"}

# ---- 1️⃣ GET all tickets ----
response = requests.get(TICKETS_API_URL, headers=headers)
if response.status_code == 200:
    print("All Tickets:")
    print(response.json())
else:
    print("Error:", response.status_code, response.text)

# ---- 2️⃣ POST create a new ticket ----
new_ticket_data = {
    "title": "Test Ticket",
    "description": "Created via API",
    "category": "technical",
    "priority": "medium"
}
response = requests.post(TICKETS_API_URL, json=new_ticket_data, headers=headers)
if response.status_code == 201:
    new_ticket = response.json()
    print("Created Ticket:")
    print(new_ticket)
    new_ticket_id = new_ticket['id']
else:
    print("Error creating ticket:", response.status_code, response.text)
    new_ticket_id = None

# ---- 3️⃣ PATCH update the new ticket ----
if new_ticket_id:
    update_data = {"status": "closed", "priority": "high"}
    url = f"{TICKETS_API_URL}{new_ticket_id}/"
    response = requests.patch(url, json=update_data, headers=headers)
    if response.status_code == 200:
        print("Updated Ticket:")
        print(response.json())
    else:
        print("Error updating ticket:", response.status_code, response.text)

# ---- 4️⃣ DELETE the new ticket ----
if new_ticket_id:
    url = f"{TICKETS_API_URL}{new_ticket_id}/"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Ticket {new_ticket_id} deleted successfully")
    else:
        print("Error deleting ticket:", response.status_code, response.text)
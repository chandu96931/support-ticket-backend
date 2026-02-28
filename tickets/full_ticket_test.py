import requests

# ---- Configuration ----
TICKETS_API_URL = "http://127.0.0.1:8000/api/tickets/"  # Your backend tickets endpoint
API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcxODEwMzEwLCJpYXQiOjE3NzE4MDY3MTAsImp0aSI6ImFiNDZmZmFjZWE3ZjQzYTNhOTIzY2UxNTU0NzE1MzUyIiwidXNlcl9pZCI6IjEifQ.fsvST7MYcZjZKF2qltmkXOl8BeQrw1GO8XjKhqTAjtU"

# ---- Headers for Authorization ----
headers = {
    "Authorization": f"Bearer {API_TOKEN.strip()}"  # Exactly one space
}

# ---- 1️⃣ GET all tickets ----
response = requests.get(TICKETS_API_URL, headers=headers)
if response.status_code == 200:
    print("All Tickets:")
    print(response.json())
else:
    print("Error fetching tickets:", response.status_code, response.text)

# ---- 2️⃣ POST create a new ticket ----
new_ticket_data = {
    "title": "Test Ticket",
    "description": "Created via Python script",
    "category": "technical",
    "priority": "medium"
}

response = requests.post(TICKETS_API_URL, json=new_ticket_data, headers=headers)
if response.status_code == 201:
    new_ticket = response.json()
    print("\nCreated Ticket:")
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
        print("\nUpdated Ticket:")
        print(response.json())
    else:
        print("Error updating ticket:", response.status_code, response.text)

# ---- 4️⃣ DELETE the new ticket ----
if new_ticket_id:
    url = f"{TICKETS_API_URL}{new_ticket_id}/"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"\nTicket {new_ticket_id} deleted successfully")
    else:
        print("Error deleting ticket:", response.status_code, response.text)
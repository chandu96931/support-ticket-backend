import requests

TICKETS_API_URL = "http://127.0.0.1:8000/api/tickets/"
API_TOKEN ="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzcxODEwMzEwLCJpYXQiOjE3NzE4MDY3MTAsImp0aSI6ImFiNDZmZmFjZWE3ZjQzYTNhOTIzY2UxNTU0NzE1MzUyIiwidXNlcl9pZCI6IjEifQ.fsvST7MYcZjZKF2qltmkXOl8BeQrw1GO8XjKhqTAjtU"

headers = {
    "Authorization": f"Bearer {API_TOKEN.strip()}"  # Make sure there is exactly one space
}

response = requests.get(TICKETS_API_URL, headers=headers)
print(response.status_code)
print(response.text)
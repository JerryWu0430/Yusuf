import requests
import json

url = "https://api.coresignal.com/cdapi/v1/professional_network/job/search/filter"

payload = json.dumps(
    {"application_active":"True","deleted":"False","employment_type":"Internship","industry":"(Information Technology & Services)","country":"(United Kingdom)"}
)
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJFZERTQSIsImtpZCI6ImMxYzBjNTY3LWU3YjAtZTJiNS04MGY5LWMyNzE1MjQ1OTlkMCJ9.eyJhdWQiOiJ1Y2wiLCJleHAiOjE3NjAzODIwMjgsImlhdCI6MTcyODgyNTA3NiwiaXNzIjoiaHR0cHM6Ly9vcHMuY29yZXNpZ25hbC5jb206ODMwMC92MS9pZGVudGl0eS9vaWRjIiwibmFtZXNwYWNlIjoicm9vdCIsInByZWZlcnJlZF91c2VybmFtZSI6InVjbCIsInN1YiI6ImZhMGM0YzljLWMyMWMtZmZkZi1jMGI5LTQ4YWVkNWFmOWMxNiIsInVzZXJpbmZvIjp7InNjb3BlcyI6ImNkYXBpIn19.IiCJVTJTCr9BQ3_C1jkNpJ3mkBDOLWt4qr5pumVp_RmtXcuRzdRoaVqQ2L-tQtAoKnznox-v4qUMqo_thn3_CA'
}

response = requests.request("POST", url, headers=headers, data=payload)
job_ids = json.loads(response.text)

for job_id in job_ids:
    url = f"https://api.coresignal.com/cdapi/v1/professional_network/job/collect/{job_id}"
    print(url)
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    break
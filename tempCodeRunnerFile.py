import requests
import json

url = "https://api.coresignal.com/cdapi/v1/professional_network/job/search/filter"
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJFZERTQSIsImtpZCI6ImMxYzBjNTY3LWU3YjAtZTJiNS04MGY5LWMyNzE1MjQ1OTlkMCJ9.eyJhdWQiOiJ1Y2wiLCJleHAiOjE3NjAzODIwMjgsImlhdCI6MTcyODgyNTA3NiwiaXNzIjoiaHR0cHM6Ly9vcHMuY29yZXNpZ25hbC5jb206ODMwMC92MS9pZGVudGl0eS9vaWRjIiwibmFtZXNwYWNlIjoicm9vdCIsInByZWZlcnJlZF91c2VybmFtZSI6InVjbCIsInN1YiI6ImZhMGM0YzljLWMyMWMtZmZkZi1jMGI5LTQ4YWVkNWFmOWMxNiIsInVzZXJpbmZvIjp7InNjb3BlcyI6ImNkYXBpIn19.IiCJVTJTCr9BQ3_C1jkNpJ3mkBDOLWt4qr5pumVp_RmtXcuRzdRoaVqQ2L-tQtAoKnznox-v4qUMqo_thn3_CA'
}

def get_job_ids():
    payload = json.dumps({
        "employment_type": "Internship OR Part-time OR Contract",
        "industry": "(Information Technology & Services) OR Telecommunications OR Internet OR Accounting OR Nanotechnology OR (Computer Hardware) OR (Computer Software) OR (Computer & Network Security) OR (Information Services) OR (Computer Networking) OR (Computer Games)",
        "country": "(United Kingdom) OR Italy",
        "application_active": "True",
        "deleted": "False"
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)
    job_ids = json.loads(response.text)
    return job_ids

def get_job_details(job_id):
    url = f"https://api.coresignal.com/cdapi/v1/professional_network/job/collect/{job_id}"
    response = requests.request("GET", url, headers=headers)
    return json.loads(response.text)
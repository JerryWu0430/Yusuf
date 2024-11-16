import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

url = "https://api.coresignal.com/cdapi/v1/professional_network/job/search/filter"
headers = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {os.getenv('BEARER_TOKEN')}"
}

def get_job_ids():
    payload = json.dumps({
        "employment_type": "Internship OR Part-time OR Contract",
        "industry": "(Information Technology & Services) OR Telecommunications OR Internet OR Accounting OR Nanotechnology OR (Computer Hardware) OR (Computer Software) OR (Computer & Network Security) OR (Information Services) OR (Computer Networking) OR (Computer Games)",
        "country": "(United Kingdom)",
        "application_active": "True",
        "deleted": "False"
    })
    
    response = requests.request("POST", url, headers=headers, data=payload)
    
    # Debugging information
    print("Response Status Code:", response.status_code)
    print("Response Text:", response.text)
    
    try:
        job_ids = response.json()
    except json.JSONDecodeError:
        print("Error decoding JSON response:")
        print(response.text)
        return []
    return job_ids

def get_job_details(job_id):
    url = f"https://api.coresignal.com/cdapi/v1/professional_network/job/collect/{job_id}"
    response = requests.request("GET", url, headers=headers)
    try:
        return response.json()
    except json.JSONDecodeError:
        print("Error decoding JSON response:")
        print(response.text)
        return {}

# Example usage
job_ids = get_job_ids()
if job_ids:
    print(get_job_details(job_ids[0]))
else:
    print("No job IDs found.")
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

def get_job_ids(employment_type, industry, country):
    payload = json.dumps({
        "employment_type": employment_type,
        "industry": industry,
        "country": country,
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
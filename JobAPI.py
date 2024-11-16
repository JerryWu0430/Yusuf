import requests
import json

url = "https://api.coresignal.com/cdapi/v1/professional_network/job/search/filter"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer eyJhbGciOiJFZERTQSIsImtpZCI6ImMxYzBjNTY3LWU3YjAtZTJiNS04MGY5LWMyNzE1MjQ1OTlkMCJ9.eyJhdWQiOiJ1Y2wiLCJleHAiOjE3NjAzODIwMjgsImlhdCI6MTcyODgyNTA3NiwiaXNzIjoiaHR0cHM6Ly9vcHMuY29yZXNpZ25hbC5jb206ODMwMC92MS9pZGVudGl0eS9vaWRjIiwibmFtZXNwYWNlIjoicm9vdCIsInByZWZlcnJlZF91c2VybmFtZSI6InVjbCIsInN1YiI6ImZhMGM0YzljLWMyMWMtZmZkZi1jMGI5LTQ4YWVkNWFmOWMxNiIsInVzZXJpbmZvIjp7InNjb3BlcyI6ImNkYXBpIn19.IiCJVTJTCr9BQ3_C1jkNpJ3mkBDOLWt4qr5pumVp_RmtXcuRzdRoaVqQ2L-tQtAoKnznox-v4qUMqo_thn3_CA'
}

def get_job_ids(country, application_active, deleted, created_at_gte, created_at_lte, company_linkedin_url, keyword_description, company_domain, title, company_name, location, last_updated_gte, employment_type, industry, last_updated_lte, company_exact_website):
    # Payload is the search criteria for the job
    payload = json.dumps(
        {
            "keyword_description": keyword_description,
            "title": title,
            "location": location,
            "industry": industry,
            "employment_type": employment_type,
            "application_active": "True",
            "deleted": "False",

            #"country": country,
            #"created_at_gte": created_at_gte,
            #"created_at_lte": created_at_lte,
            #"last_updated_gte": last_updated_gte,
            #"last_updated_lte": last_updated_lte,
            #"company_exact_website": company_exact_website
            #"company_name": company_name,
            #"company_domain": company_domain,
            #"company_linkedin_url": company_linkedin_url,
        }
    )
    response = requests.request("POST", url, headers=headers, data=payload)
    job_ids = json.loads(response.text)
    return job_ids

def get_job_details(job_id):
    url = f"https://api.coresignal.com/cdapi/v1/professional_network/job/{job_id}"
    response = requests.request("GET", url, headers=headers)
    return json.loads(response.text)

# Example usage
job_ids = get_job_ids(
    country="United States",
    application_active="True",
    deleted="False",
    created_at_gte="2023-01-01 00:00:00",
    created_at_lte="2023-12-31 23:59:59",
    company_linkedin_url="",
    keyword_description="Software Engineer",
    company_domain="",
    title="Software Engineer",
    company_name="",
    location="San Francisco",
    last_updated_gte="2023-01-01 00:00:00",
    employment_type="Full Time",
    industry="Information Technology",
    last_updated_lte="2023-12-31 23:59:59",
    company_exact_website=""
)

for job_id in job_ids:
    job_details = get_job_details(job_id)
    print(f"Job ID: {job_id}")
    print(f"Description: {job_details.get('description', 'No description available')}")
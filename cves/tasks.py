import requests
from .models import CVE

API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

def fetch_and_store_cves(offset=0, limit=2000):
    params = {
        "startIndex": offset,
        "resultsPerPage": limit,
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json().get('vulnerabilities', [])
        for item in data:
            cve_data = item['cve']
            CVE.objects.update_or_create(
                cve_id=cve_data['id'],
                defaults={
                    "description": cve_data.get('description', {}).get('description_data', [{}])[0].get('value', ''),
                    "base_score_v2": cve_data.get('metrics', {}).get('cvssMetricV2', {}).get('baseScore'),
                    "base_score_v3": cve_data.get('metrics', {}).get('cvssMetricV3', {}).get('baseScore'),
                    "last_modified": cve_data.get('lastModified'),
                    "published_date": cve_data.get('publishedDate'),
                }
            )

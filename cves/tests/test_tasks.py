from django.test import TestCase
from cves.models import CVE
from cves.tasks import fetch_and_store_cves

class TaskTest(TestCase):
    def test_fetch_and_store_cves(self):
        # Mock API Response
        from unittest.mock import patch
        mock_response = {
            "vulnerabilities": [
                {
                    "cve": {
                        "id": "CVE-2023-0002",
                        "description": {"description_data": [{"value": "Test description"}]},
                        "metrics": {
                            "cvssMetricV2": {"baseScore": 4.0},
                            "cvssMetricV3": {"baseScore": 6.0}
                        },
                        "lastModified": "2023-12-01T00:00:00Z",
                        "publishedDate": "2023-11-01T00:00:00Z"
                    }
                }
            ]
        }
        with patch('requests.get') as mock_get:
            mock_get.return_value.status_code = 200
            mock_get.return_value.json.return_value = mock_response

            fetch_and_store_cves()

        # Verify data is saved
        cve = CVE.objects.get(cve_id="CVE-2023-0002")
        self.assertEqual(cve.description, "Test description")
        self.assertEqual(cve.base_score_v3, 6.0)

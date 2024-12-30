from django.test import TestCase
from django.urls import reverse
from cves.models import CVE

class CVEViewTest(TestCase):
    def setUp(self):
        self.cve = CVE.objects.create(
            cve_id="CVE-2023-0001",  # Ensure this matches the URL used in the test
            description="Sample CVE for testing",
            base_score_v3=7.5,
            last_modified="2024-01-01T12:00:00Z",
            published_date="2024-01-01T10:00:00Z",
        )

    def test_detail_view(self):
        response = self.client.get(reverse('cve_detail', args=[self.cve.cve_id]))
        self.assertEqual(response.status_code, 200)

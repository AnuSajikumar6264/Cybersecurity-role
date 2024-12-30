from django.test import TestCase
from cves.models import CVE

class CVEModelTest(TestCase):
    def setUp(self):
        self.cve = CVE.objects.create(
            cve_id="CVE-2023-0001",
            description="Sample vulnerability description",
            base_score_v2=5.0,
            base_score_v3=7.5,
            last_modified="2023-12-01T00:00:00Z",
            published_date="2023-11-01T00:00:00Z"
        )

    def test_cve_creation(self):
        self.assertEqual(self.cve.cve_id, "CVE-2023-0001")
        self.assertEqual(self.cve.description, "Sample vulnerability description")
        self.assertEqual(self.cve.base_score_v3, 7.5)

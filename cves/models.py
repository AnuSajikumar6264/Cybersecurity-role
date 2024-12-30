from django.db import models

class CVE(models.Model):
    cve_id = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    base_score_v2 = models.FloatField(null=True, blank=True)
    base_score_v3 = models.FloatField(null=True, blank=True)
    last_modified = models.DateTimeField()
    published_date = models.DateTimeField()

    def __str__(self):
        return self.cve_id

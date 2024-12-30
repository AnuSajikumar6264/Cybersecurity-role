from rest_framework.generics import RetrieveAPIView
from .models import CVE
from .serializers import CVESerializer

class CVEDetailView(RetrieveAPIView):
    queryset = CVE.objects.all()
    serializer_class = CVESerializer
    lookup_field = "cve_id"  # Match this with your model field

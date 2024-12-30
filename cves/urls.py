from django.urls import path
from .views import CVEDetailView

urlpatterns = [
    path('<str:cve_id>/', CVEDetailView.as_view(), name='cve_detail'),
]

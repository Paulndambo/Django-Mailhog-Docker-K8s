from django.urls import path
from .views import EmailTestAPIView

urlpatterns = [
    path("", EmailTestAPIView.as_view(), name="send-test-email"),
]
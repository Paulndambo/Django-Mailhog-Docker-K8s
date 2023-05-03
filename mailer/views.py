from django.shortcuts import render
from django.conf import settings
from .serializers import EmailTestSerializer
from rest_framework import status, generics
from rest_framework.response import Response
from django.core.mail import EmailMessage
# Create your views here.
class EmailTestAPIView(generics.CreateAPIView):
    serializer_class = EmailTestSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            message = data.get('message')
            to_email = data.get('to_email')
            try:
                m = EmailMessage(
                    'Testing Mailhog',
                    message,
                    settings.SITE_EMAIL,
                    [to_email,]
                )
                m.send(fail_silently=False)
            except Exception as e:
                raise e
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
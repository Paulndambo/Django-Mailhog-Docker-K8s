from rest_framework import serializers

class EmailTestSerializer(serializers.Serializer):
    to_email = serializers.EmailField()
    message = serializers.CharField(max_length=500)
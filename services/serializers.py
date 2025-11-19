from rest_framework import serializers
from .models import Service


class Serviceserializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'provider', 'title', 'cost', 'image', ]
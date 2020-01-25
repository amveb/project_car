from rest_framework.serializers import ModelSerializer

from orders.models import Service


class ServiceSerializer(ModelSerializer):
    class Meta:
        model = Service
        fields = ['name', 'price']
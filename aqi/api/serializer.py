from rest_framework.serializers import ModelSerializer
from .models import AQI

class AQIDataSerializer(ModelSerializer):
    class Meta:
        model = AQI
        fields = '__all__'
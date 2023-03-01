from rest_framework.serializers import ModelSerializer
from servicios.models import *


class AreaSerializer(ModelSerializer):
    class Meta:
        model = Areas
        fields = '__all__'


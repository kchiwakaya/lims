from rest_framework import serializers
from .models import FarmRegister

class FarmRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmRegister
        fields = '__all__'
from rest_framework import serializers
from .models import FarmRegister

class FarmRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmRegister
        fields = ( 'farm_id', 
            'farm_name',
            'size',
            'unit_of_measure',
            'size_in_hectares',
            'ownership',
            'owner_name',
            'company_name',
            'nationality',
            'gazette_status',
            'diagram_no',
            'title_type',
            'deed_no',
            'province',
            'previous_district',
            'current_district',
            'farm_activity',
            'remarks'
            )
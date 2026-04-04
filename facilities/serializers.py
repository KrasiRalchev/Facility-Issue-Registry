from rest_framework import serializers

from facilities.models import Facility


class FacilityListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'



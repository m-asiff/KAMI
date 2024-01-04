from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from airplane.models import Airplane


class AirplaneSerializer(serializers.ModelSerializer):

    fuel_tank_capacity = serializers.SerializerMethodField()
    fuel_consumption_per_minute = serializers.SerializerMethodField()
    max_minutes_to_fly = serializers.SerializerMethodField()

    @classmethod
    def get_fuel_tank_capacity(cls, obj):
        return obj.fuel_tank_capacity()

    @classmethod
    def get_fuel_consumption_per_minute(cls, obj):
        return obj.fuel_consumption_per_minute()

    @classmethod
    def get_max_minutes_to_fly(cls, obj):
        return obj.max_minutes_to_fly()

    class Meta:
        model = Airplane
        fields = "__all__"

    def validate_plane_id(self, value):
        """
        Check that the plane_id is greater than 0, as it will make everything 0 so no point of doing that.
        """
        if value == 0:
            raise ValidationError("Plane ID must be greater than 0")

        return value

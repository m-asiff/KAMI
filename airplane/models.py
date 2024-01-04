import math

from django.db import models


# Create your models here.
class Airplane(models.Model):

    # plane_id is unique as it is for 10 different planes
    plane_id = models.PositiveIntegerField(unique=True)
    passengers = models.PositiveIntegerField()

    # below implemented functions calculate the required data of planes
    def fuel_tank_capacity(self) -> float:
        return self.plane_id * 200.00

    def fuel_consumption_per_minute(self) -> float:
        return round((math.log(self.plane_id) * 0.80) + (self.passengers * 0.02), 2)

    def max_minutes_to_fly(self) -> float:
        return round(self.fuel_tank_capacity() / self.fuel_consumption_per_minute(), 2)

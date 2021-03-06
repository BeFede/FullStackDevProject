from django.db import models
import re
from api.exceptions import InvalidDataException


class Car(models.Model):
    PLATE_REGEX = [
        "^[A-Z]{3}[ ]{1}\d{3}$",
        "^[A-Z]{2}[ ]{1}\d{3}[ ]{1}[A-Z]{2}$",
    ]

    name = models.CharField(max_length=50)
    plate = models.CharField(max_length=9, unique=True)

    class Meta:
        db_table = 'cars'
        verbose_name = "car"
        verbose_name_plural = "cars"
        indexes = [
            models.Index(fields=['plate']),
        ]

    def __str__(self):
        return "Name: {} - Plate: {}".format(self.name, self.plate)

    def save(self, *args, **kwargs):

        # Valid car data 
        if not self.name or not self.plate:
            raise InvalidDataException("Plate and name are required")

        if len(self.name) > 50:
            error_message = "The name car is too long. Max lenght: 50"
            raise InvalidDataException(error_message)

        if not isinstance(self.name, str):
            raise InvalidDataException("The name parameter is not a string")

        if not isinstance(self.name, str):
            raise InvalidDataException("The plate parameter is not a string")

        # Check if the plate has valid format
        for regex in self.PLATE_REGEX:
            if re.match(regex, self.plate):
                super().save(*args, **kwargs)
                return

        error_message = "The plate format is incorrect. \
            Possibles formats: ABC 123 | AA 111 AA"
        raise InvalidDataException(error_message)

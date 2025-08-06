from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    country = models.CharField(max_length=100, blank=True, help_text="Country of origin for the car make")

    def __str__(self):
        return self.name

class CarModel(models.Model):
    # Choices for car type
    CAR_TYPES = (
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
    )

    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SEDAN')
    year = models.IntegerField(
        validators=[
            MinValueValidator(2015, message="Year must be 2015 or later"),
            MaxValueValidator(2023, message="Year must be 2023 or earlier")
        ]
    )
    fuel_type = models.CharField(max_length=50, blank=True, help_text="e.g., Petrol, Diesel, Electric")

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"
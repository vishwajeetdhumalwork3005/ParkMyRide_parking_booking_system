from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return self.name

VEHICLE_CHOICES = (
    ('Car', 'Car'),
    ('Bike', 'Bike'),
    ('Cycle', 'Cycle'),
)

class ParkingSlot(models.Model):
    slot_name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_CHOICES)
    hourly_price = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.slot_name} - {self.location.name}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact from {self.name} <{self.email}>"

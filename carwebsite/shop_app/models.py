from django.db import models

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/', blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.name} {self.brand} {self.price}"
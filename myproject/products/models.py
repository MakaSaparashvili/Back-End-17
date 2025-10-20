from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True, null=True)  # <-- არჩევითი ველი
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name


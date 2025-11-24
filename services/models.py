from django.db import models
from django.contrib.auth.models import User

class Service(models.Model):
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    SERVICE_TYPE =(
        ('house_cleaning', 'House_cleaning'),
        ('laundry', 'Laundry'),
        ('gardening', 'Gardening')
    )
    service = models.CharField(max_length=100, choices=SERVICE_TYPE, default='laundry')
    image = models.ImageField(upload_to='service_images/', null=True, blank=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.provider.name} - {self.cost}"
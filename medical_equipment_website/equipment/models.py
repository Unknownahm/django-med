from django.db import models

class MedicalEquipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='equipment_images/', default='download.jfif')
    url = models.URLField(max_length=200, null=True, blank=True)
    # Add more fields as needed

    def __str__(self):
        return self.name
    


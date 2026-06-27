from django.db import models

# Create your models here.
class Competitions(models.Model):
    class Type(models.TextChoices):
        Indoor = 'Indoor', 'Indoor'
        Outdoor = 'Outdoor', 'Outdoor'
        Field_Archery = 'Field Archery', 'Field Archery'
        Three_D_Archery = '3D Archery', '3D Archery'
    name = models.CharField(max_length=100)
    description = models.TextField()
    type = models.CharField(max_length=100, choices=Type.choices)
    date = models.DateField()
    position = models.CharField(max_length=100, blank=True, null=True)
    mark = models.CharField(max_length=100, blank=True, null=True)
    competition_link = models.URLField(blank=True, null=True)
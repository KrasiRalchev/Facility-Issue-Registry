from cloudinary.models import CloudinaryField
from django.core.validators import FileExtensionValidator
from django.db import models

from common.validators import validate_file_size_2mb


class Unit(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Facility(models.Model):
    name = models.CharField(
        max_length=100,
    )
    unit = models.ForeignKey(
        Unit,
        on_delete=models.PROTECT,
        related_name='facilities',
    )
    location = models.CharField(
        max_length=150,
    )
    cost_center = models.CharField(
        max_length=10
    )
    cc_manager = models.CharField(
        max_length=30
    )
    inventory_number = (models.CharField(
        max_length=10,
        unique=True,
        blank=True,
        null=True,
    ))
    description = models.TextField(
        blank=True,
    )
    installed_on = models.DateField()
    is_active = models.BooleanField(
        default=True,
    )
    facility_image = CloudinaryField('image',
        validators=[validate_file_size_2mb,
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
    ])

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name





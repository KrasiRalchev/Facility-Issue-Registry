from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models

from common.validators import validate_file_size_1mb


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        primary_key=True
    )
    phone_number = models.CharField(
        max_length=20, null=True, blank=True
    )
    birth_date = models.DateField(
        null=True, blank=True
    )
    company_position = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    manager = models.CharField(
        max_length=30
    )
    photo = CloudinaryField('image',

        validators=[validate_file_size_1mb,
                    FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
                    ])

    def __str__(self):
        return f'{self.user.username} Profile'
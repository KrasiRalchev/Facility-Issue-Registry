
from django.core.validators import FileExtensionValidator
from django.db import models

from common.validators import validate_file_size
from facilities.models import Facility
from issues.choices import Priority_choices, Status_choices


class Tag(models.Model):
    name = models.CharField(
        max_length=40,
        unique=True,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Issue(models.Model):
    location = models.CharField(
        max_length=50,
    )
    description = models.TextField()

    requester = models.CharField(max_length=30)

    priority = models.CharField(
        max_length=10,
        choices=Priority_choices.choices,
        default= Priority_choices.MEDIUM
    )
    status = models.CharField(
        max_length=15,
        choices=Status_choices.choices,
        default= Status_choices.OPEN
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='issues',
    )
    is_critical = models.BooleanField(
        default=False,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    resolved_at = models.DateTimeField(
        null=True,
        blank=True,
    )
    issue_image = models.ImageField(
        upload_to='issue_images/',
        blank=True,
        null=True,
        validators=[validate_file_size,
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']),
        ])
    facility = models.ForeignKey(
        Facility,
        on_delete=models.CASCADE,
        related_name='issues',)

    class Meta:
        ordering = ['-created_at']


    def __str__(self):
        return f'{self.location} ({self.get_status_display()})'

    def is_open(self):
        return self.status in [Status_choices.OPEN,
                               Status_choices.IN_PROGRESS,
                               ]

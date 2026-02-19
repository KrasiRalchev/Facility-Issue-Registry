from django.core.validators import MinValueValidator
from django.db import models

from issues.models import Issue
from maintenance.choices import Service_choices


class MaintenanceAction(models.Model):
    action_description = models.TextField()
    started_on = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    edited_on = models.DateTimeField(auto_now=True)
    resolved_on = models.DateTimeField(
        null=True,
        blank=True
    )
    performer = models.CharField(
        max_length=40,
        choices=Service_choices.choices,
        default=Service_choices.INTERNAL_SERVICE
    )
    performer_name = models.CharField(max_length=50, null=True, blank=True)
    delivery_request = models.BooleanField(default=False)
    cost = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        default=0,
        validators=[MinValueValidator(
            limit_value=0,
        )
      ]
    )
    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name='actions',
    )

    class Meta:
        ordering = ['-started_on']

    def __str__(self):
        return f'Action for {self.issue.location}'
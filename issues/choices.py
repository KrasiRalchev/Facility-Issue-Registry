from django.db import models


class Priority_choices (models.TextChoices):
       LOW = 'LOW', 'low'
       MEDIUM = 'MED', 'medium'
       HIGH = 'HIGH', 'high'


class Status_choices (models.TextChoices):
        OPEN = 'OPEN', 'open'
        IN_PROGRESS = 'IN_PROGRESS', 'in_progress'
        RESOLVED = 'RESOLVED', 'resolved'
        CLOSED = 'CLOSED', 'closed'

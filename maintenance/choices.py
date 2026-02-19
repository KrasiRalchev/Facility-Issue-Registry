from django.db import models


class Service_choices (models.TextChoices):
        INTERNAL_SERVICE = 'INTERNAL_SERVICE', 'internal service'
        EXTERNAL_SERVICE = 'EXTERNAL+SERVICE', 'external service'
        EXTERNAL_DELIVERER = 'EXTERNAL_DELIVERER', 'external deliverer'
        TENDER_PROCEDURE = 'TENDER_PROCEDURE', 'tender procedure'

from django.db import models


class Service_choices (models.TextChoices):
        INTERNAL_SERVICE = 'INTERNAL_SERVICE', 'internal service'
        EXTERNAL_SERVICE = 'EXTERNAL_SERVICE', 'external service'
        EXTERNAL_DELIVERER = 'EXTERNAL_DELIVERER', 'external deliverer'
        TENDER_PROCEDURE = 'TENDER_PROCEDURE', 'tender procedure'

class Required_parts_choices (models.TextChoices):
        NO_NEED = 'NO_NEED', 'no need'
        FROM_WAREHOUSE = 'FROM_WAREHOUSE', 'from warehouse'
        IN_STOCK = 'IN_STOCK', 'in stock'
        DELIVERY_WAITING = 'DELIVERY_WAITING', 'delivery waiting'
        TENDER_PROCEDURE = 'TENDER_PROCEDURE', 'tender procedure'


from django.db import models


class Service_choices (models.TextChoices):
        INTERNAL_SERVICE = 'INTERNAL_SERVICE', 'Internal service'
        EXTERNAL_SERVICE = 'EXTERNAL_SERVICE', 'External service'
        EXTERNAL_DELIVERER = 'EXTERNAL_SUPPLIER', 'External supplier'
        TENDER_PROCEDURE = 'TENDER_PROCEDURE', 'Tender procedure'

class Required_parts_choices (models.TextChoices):
        NO_NEED = 'NO_NEED', 'No need'
        FROM_WAREHOUSE = 'FROM_WAREHOUSE', 'From warehouse'
        DELIVERY_WAITING = 'DELIVERY_WAITING', 'Delivery waiting'
        TENDER_PROCEDURE = 'TENDER_PROCEDURE', 'Tender procedure'


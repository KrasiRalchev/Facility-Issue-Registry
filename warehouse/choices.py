from django.db import models


class Unit_choices(models.TextChoices):
    KG = 'kg', 'kg'
    METER = 'm', 'm'
    SQUARE_METER = 'm2', 'm2'
    CUBIC_METER = 'm3', 'm3'
    PIECE = 'pcs', 'pcs'
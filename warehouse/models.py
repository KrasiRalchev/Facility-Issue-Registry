from django.core.validators import MinValueValidator
from django.db import models

from facilities.models import Unit
from warehouse.choices import Unit_choices


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8,
                                decimal_places=2,
                                default=0,
                                validators=[MinValueValidator(0.01),]
                                )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
    )
    internal_code = models.CharField(max_length=8, unique=True)
    barcode = models.CharField(max_length=13,
                               unique=True,
                               blank=True,
                               null=True
    )
    unit = models.CharField(max_length=10,
                            choices=Unit_choices.choices,
                            default=Unit_choices.PIECE
                            )
    quantity = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    min_quantity = models.IntegerField(validators=[MinValueValidator(0)])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name




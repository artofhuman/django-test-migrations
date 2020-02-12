# -*- coding: utf-8 -*-

from django.db import models

_SomeItemStringFieldLength = 50


class SomeItem(models.Model):
    """We use this model for testing migrations."""

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(amount__gt=0), name="check_amount")
        ]

    string_field = models.CharField(max_length=_SomeItemStringFieldLength)
    is_clean = models.BooleanField()
    amount = models.DecimalField(max_digits=19, decimal_places=4, default=0)

from django.db import models
from django.contrib.auth import get_user_model

"""
item_name: string, indexed, should be unique
item_location: string, indexed
item_class: string (could change to enumeration in version 2)
"""

class Item(models.Model):
    item_name = models.CharField(max_length=50, db_index=True)
    item_location = models.CharField(max_length=10, blank=True, db_index=True)
    item_class = models.CharField(max_length=20, blank=True)
    shopper_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"item_name: {self.item_name}, item_location: {self.item_location}, shopper_id: {self.shopper_id}"
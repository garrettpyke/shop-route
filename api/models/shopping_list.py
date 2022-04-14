from django.db import models
from django.contrib.auth import get_user_model
from .item import Item

"""
item_num: string (foreign key)
shopper_id: integer (foreign key)
item_qty: integer
item_complete: boolean
added_on: date
list_num: integer, used to differentiate different trips to the store
# Combination of item_name and list_num should be unique. 
"""     

class ShoppingList(models.Model):
    item_num = models.ForeignKey(
        'Item',
        on_delete=models.DO_NOTHING # we don't want to delete the item from the "master" item list, just from this shopping list
    )
    shopper_id = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE # ...but we do want to delete the item if the user goes away as Items are user-specific
    )
    item_qty = models.PositiveIntegerField()
    item_complete = models.BooleanField(default=False)
    added_on = models.DateField(auto_now=True)
    # setting list_num to blank=True for testing
    list_num = models.PositiveIntegerField(blank=True)

    def __str__(self):
        return f"item_num: {self.item_num}, shopper_id: {self.shopper_id}, item_qty: {self.item_qty}, item_complete: {self.item_complete}"    
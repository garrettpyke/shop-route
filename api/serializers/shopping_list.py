from rest_framework import serializers
from ..models.shopping_list import ShoppingList

class ShoppingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingList
        fields = ('id', 'item_num', 'shopper_id', 'item_qty', 'item_complete', 'added_on', 'list_num')
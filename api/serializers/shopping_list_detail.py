from rest_framework import serializers
from ..models.shopping_list import ShoppingList
from ..serializers.item import ItemSerializer
from rest_framework.serializers import ModelSerializer

class ShoppingListDetailSerializer(serializers.ModelSerializer):    
    # item = ItemSerializer(many=False, read_only=True)
    # item_desc = serializers.ReadOnlyField(source='item_name')
    item_name = serializers.CharField(read_only=True, source="item_name.item_name")

    class Meta:
        model = ShoppingList
        fields = ('id', 'item_num', 'shopper_id', 'item_qty', 'item_complete', 'added_on', 'list_num', 'item_name')
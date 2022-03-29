from rest_framework import serializers
from ..models.item import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'item_name', 'item_location', 'item_class', 'shopper_id')


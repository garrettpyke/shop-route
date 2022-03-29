from rest_framework import serializers
from ..models.item import item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'item_name', 'item_location')

        
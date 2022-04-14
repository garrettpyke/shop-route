from rest_framework import serializers
from ..models.shopping_list import ShoppingList

class ShoppingListSerializer(serializers.ModelSerializer):
    # SerializerMethodField calls get_<fieldVariable> by default
    item_name = serializers.SerializerMethodField()
    item_location = serializers.SerializerMethodField()

    class Meta:
        model = ShoppingList
        fields = ('id', 'item_name', 'item_location', 'item_num', 'shopper_id', 'item_qty', 'item_complete', 'added_on', 'list_num')

    def get_item_name(self, instance):
        return instance.item_num.item_name if instance.item_num else ''
  
    def get_item_location(self, instance):
        return instance.item_num.item_location if instance.item_num else ''

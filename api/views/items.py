from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from ..models.item import Item
from ..serializers.item import ItemSerializer

class ItemsView(APIView):
    def get(self, request):
        items = Item.objects.filter(shopper_id=request.user.id)
        data = ItemSerializer(items, many=True).data
        return Response(data)

    
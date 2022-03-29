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

    def post(self, request):
        request.data['shopper_id'] = request.user.id
        item = ItemSerializer(data=request.data)
        if item.is_valid():
            item.save()
            return Response(item.data, status=status.HTTP_201_CREATED)
        else:
            return Response(item.errors, status=status.HTTP_400_BAD_REQUEST)


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

class ItemView(APIView):
    def get(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        if request.user != item.shopper_id:
            raise PermissionDenied('Unauthorized, this item belongs to another shopper')
        else:
            data = ItemSerializer(item).data
            return Response(data)

    def delete(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        if request.user != item.shopper_id:
            raise PermissionDenied('Unauthorized, this item belongs to another shopper')
        else:
            item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        item = get_object_or_404(Item, pk=pk)
        if request.user != item.shopper_id:
            raise PermissionDenied('Unauthorized, this item belongs to another shopper')
        else:
            request.data['shopper_id'] = request.user.id
            updated_item = ItemSerializer(item, data=request.data, partial=True)
            if updated_item.is_valid():
                updated_item.save()
                return Response(updated_item.data)
            else:
                return Response(updated_item.errors, status=status.HTTP_400_BAD_REQUEST)
            
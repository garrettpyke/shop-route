from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from ..models.shopping_list import ShoppingList
from ..serializers.shopping_list import ShoppingListSerializer

class ShoppingListsView(APIView):
    def get(self, request):
        list_items = ShoppingList.objects.filter(shopper_id=request.user.id)
        data = ShoppingListSerializer(list_items, many=True).data
        return Response(data)

    def post(self, request):
        request.data['shopper_id'] = request.user.id
        list_item = ShoppingListSerializer(data=request.data, partial=True)
        if list_item.is_valid():
            list_item.save()
            return Response(list_item.data, status=status.HTTP_201_CREATED)
        else:
            return Response(list_item.errors, status=status.HTTP_400_BAD_REQUEST)

class ShoppingListView(APIView):
    def get(self, request, pk):
        list_item = get_object_or_404(ShoppingList, pk=pk)
               
        
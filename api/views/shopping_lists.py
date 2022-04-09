from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from ..models.shopping_list import ShoppingList
from ..serializers.shopping_list import ShoppingListSerializer

class ShoppingListsView(APIView):
    def get(self, request, list_num):
        shopping_items = ShoppingList.objects.filter(shopper_id=request.user.id)
        shopping_list_items = shopping_items.filter(list_num=list_num)
        data = ShoppingListSerializer(shopping_list_items, many=True).data
        return Response(data)

    def post(self, request):
        request.data['shopper_id'] = request.user.id
        list_item = ShoppingListSerializer(data=request.data, partial=True)
        if list_item.is_valid():
            list_item.save()
            return Response(list_item.data, status=status.HTTP_201_CREATED)
        else:
            return Response(list_item.errors, status=status.HTTP_400_BAD_REQUEST)

    # Deletes 1 entire shopping list for 1 user
    def delete(self, request, list_num):
        shopping_items = ShoppingList.objects.filter(shopper_id=request.user.id)
        shopping_list_items = shopping_items.filter(list_num=list_num)
        response_data = shopping_list_items.delete()
        return Response(response_data, status=status.HTTP_204_NO_CONTENT)

class ShoppingListsAllView(APIView):
    def get(self, request):
        shopping_items = ShoppingList.objects.filter(shopper_id=request.user.id)
        data = ShoppingListSerializer(shopping_items, many=True).data
        return Response(data)

class ShoppingListItemView(APIView):
    def get(self, request, pk):
        list_item = get_object_or_404(ShoppingList, pk=pk)
        if request.user != list_item.shopper_id:
            raise PermissionDenied('Unauthorized, this item belongs to another shopper')
        else:
            data = ShoppingListSerializer(list_item).data
            return Response(data)

    def delete(self, request, pk):
        list_item = get_object_or_404(ShoppingList, pk=pk)
        if request.user != list_item.shopper_id:
            raise PermissionDenied('Unauthorized, this item belongs to another shopper')
        else:
            list_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        list_item = get_object_or_404(ShoppingList, pk=pk)
        if request.user != list_item.shopper_id:
            raise PermissionDenied('Unauthorized, this item belongs to another shopper')
        else:
            request.data['shopper_id'] = request.user.id
            updated_list_item = ShoppingListSerializer(list_item, data=request.data, partial=True)
            if updated_list_item.is_valid():
                updated_list_item.save()
                return Response(updated_list_item.data)
            else:
                return Response(updated_item.errors, status=status.HTTP_400_BAD_REQUEST)
        
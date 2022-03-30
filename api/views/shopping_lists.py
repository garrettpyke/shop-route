from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from ..models.shopping_list import ShoppingList
from ..serializers.shopping_list import ShoppingListSerializer

class ShoppingListsView(APIView):
    def get(self, request):
        items = ShoppingList.objects.filter(shopper_id=request.user.id)
        data = ShoppingListSerializer(items, many=True).data
        return Response(data)

        
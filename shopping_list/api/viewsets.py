from rest_framework.viewsets import ModelViewSet

from shopping_list.api.serializers import ShopiingItemSerializer
from shopping_list.models import ShoppingItem

class ShoppingItemViewset(ModelViewSet):
    queryset = ShoppingItem.objects.all()
    serializer_class = ShopiingItemSerializer
    
from rest_framework import serializers

from shopping_list.models import ShoppingItem


class ShopiingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingItem
        fields = ["id", "name", "purchased"]

            
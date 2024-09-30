from pos.models import *
from rest_framework import serializers

# Stock Type Serializer
class StockTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockType
        fields = ["stock_type_code", "name"]

# Stock in Hand
class StockInHandSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockInHand
        fields = "__all__"


# Units
class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model= Units
        fields = "__all__"
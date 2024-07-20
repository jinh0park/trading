from rest_framework import serializers
from .models import Pressure, TradePrice


class PressureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pressure
        fields = '__all__'


class TradePriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradePrice
        fields = '__all__'

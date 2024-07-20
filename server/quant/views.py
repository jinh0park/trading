from rest_framework import generics
from .models import Pressure, TradePrice
from .serializers import PressureSerializer, TradePriceSerializer


class PressureListCreate(generics.ListCreateAPIView):
    queryset = Pressure.objects.all()
    serializer_class = PressureSerializer


class PressureRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pressure.objects.all()
    serializer_class = PressureSerializer


class TradePriceListCreate(generics.ListCreateAPIView):
    queryset = TradePrice.objects.all()
    serializer_class = TradePriceSerializer


class TradePriceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = TradePrice.objects.all()
    serializer_class = TradePriceSerializer

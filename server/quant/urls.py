from django.urls import path
from .views import PressureListCreate, PressureRetrieveUpdateDestroy, TradePriceRetrieveUpdateDestroy, TradePriceListCreate

urlpatterns = [
    path('pressures/', PressureListCreate.as_view(), name='pressure-list'),
    path('pressures/<int:pk>/', PressureRetrieveUpdateDestroy.as_view(),
         name='pressure-detail'),
    path('trade-prices/', TradePriceListCreate.as_view(), name='trade-price-list'),
    path('trade-prices/<int:pk>/', TradePriceRetrieveUpdateDestroy.as_view(),
         name='trade-price-detail'),
]

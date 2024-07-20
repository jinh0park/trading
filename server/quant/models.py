from django.db import models


class Pressure(models.Model):
    timestamp = models.IntegerField()
    ask_pressure = models.FloatField()
    bid_pressure = models.FloatField()
    pressure_ratio = models.FloatField()


class TradePrice(models.Model):
    timestamp = models.IntegerField()
    price = models.FloatField()

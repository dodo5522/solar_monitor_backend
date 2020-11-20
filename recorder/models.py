from django.conf import settings
from django.db import models
from django.utils import timezone


class Location(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    zip_code = models.CharField(
        verbose_name='郵便番号', max_length=8, blank=True,
    )
    country = models.CharField(
        verbose_name='国', max_length=40, blank=True, default='日本',
    )
    prefecture = models.CharField(
        verbose_name='都道府県', max_length=40, blank=True,
    )
    city = models.CharField(
        verbose_name='市区町村番地', max_length=40, blank=True,
    )
    building = models.CharField(
        verbose_name='建物名', max_length=40, blank=True,
    )

    def __str__(self):
        return self.__class__.__name__


class Group(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    group = models.CharField(default='', max_length=32)

    def __str__(self):
        return self.__class__.__name__


class Source(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    source = models.CharField(default='', max_length=32)

    def __str__(self):
        return self.__class__.__name__


class Label(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    label = models.CharField(default='', max_length=16)

    def __str__(self):
        return self.__class__.__name__


class Unit(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    unit = models.CharField(default='', max_length=16)

    def __str__(self):
        return self.__class__.__name__


class Record(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    recorded_at = models.DateTimeField(default=timezone.now)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=10, decimal_places=1)

    def __str__(self):
        return self.__class__.__name__

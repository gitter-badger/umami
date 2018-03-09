# -*- coding: utf-8 -*-
import uuid

from concurrency.fields import IntegerVersionField
from django.db import models
from timezone_field import TimeZoneField


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = IntegerVersionField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Game(BaseModel):
    slug = models.SlugField(max_length=8, unique=True)
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Faction(BaseModel):
    name = models.CharField(max_length=32)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)

    def __str__(self):
        return '{}:{}'.format(self.game.slug, self.name)


class Server(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, null=True, blank=True)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    timezone = TimeZoneField(default='UTC')

    def __str__(self):
        return '{}:{}'.format(self.game.slug, self.name)


class Organization(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True, null=True, blank=True)
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    server = models.ForeignKey('Server', on_delete=models.CASCADE, null=True, blank=True)
    faction = models.ForeignKey('Faction', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{}:{}'.format(self.game.slug, self.name)

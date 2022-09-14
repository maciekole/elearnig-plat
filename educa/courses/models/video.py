from django.db import models
from .item_base import ItemBase


class Video(ItemBase):
    url = models.URLField()

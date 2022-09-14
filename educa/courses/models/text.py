from django.db import models
from .item_base import ItemBase


class Text(ItemBase):
    content = models.TextField()

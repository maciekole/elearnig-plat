from django.db import models
from .item_base import ItemBase


class Image(ItemBase):
    file = models.FileField(upload_to='images')

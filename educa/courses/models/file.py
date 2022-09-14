from django.db import models
from .item_base import ItemBase


class File(ItemBase):
    file = models.FileField(upload_to='files')

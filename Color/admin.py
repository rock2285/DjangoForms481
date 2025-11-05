""" Register the models  """

from django.contrib import admin
from .models import Color, Thing

admin.site.register(Thing)
admin.site.register(Color)
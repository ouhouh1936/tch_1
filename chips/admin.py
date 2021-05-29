from django.contrib import admin
from . import models


@admin.register(models.Chips)
class ChipAdmin(admin.ModelAdmin):
    pass

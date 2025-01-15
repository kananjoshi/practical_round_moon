from django.contrib import admin

from core.models import Animal


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ["name", "species", "breed", "status"]
    search_fields = ["name"]


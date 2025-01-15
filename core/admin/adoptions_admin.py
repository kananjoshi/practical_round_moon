from django.contrib import admin

from core.models import AnimalAdoptions


@admin.register(AnimalAdoptions)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ["get_user_name", "status"]
    search_fields = ["get_user_name"]

    def get_user_name(self, obj):
        if obj.user:
            return obj.user.name if obj.user.name else ""


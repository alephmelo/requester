from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Client, FeatureRequest


admin.site.unregister(Group)


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'client', 'priority', 'target_date', 'url', 'product_area']
    search_fields = ['title', 'client__name']

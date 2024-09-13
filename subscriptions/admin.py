from django.contrib import admin

from .models import *

# Register your models here.

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ['title', 'sku', 'is_enable', 'price', 'duration']
    

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'package', 'created_time', 'expire_time']
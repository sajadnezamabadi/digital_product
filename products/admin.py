from django.contrib import admin
from django.contrib.auth.admin import  UserAdmin
from django.contrib.auth.models import  Group
from django.utils.translation import  gettext_lazy as _

from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['parent','title' , 'is_enable' , 'created_time']
    list_filter = ['is_enable','parent']
    search_fields = ['title']
    

class FileInlineAdmin(admin.StackedInline):
    model = File
    fields = ['title', 'file', 'is_enable' , 'file_type']
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):    
    list_display = ['title' , 'is_enable' , 'created_time']
    list_filter = ['is_enable']
    filter_horizontal = ['categories']
    search_fields = ['title']
    inlines = [FileInlineAdmin]
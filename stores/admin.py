from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin # <-- Đã sửa thành tên mới

from .models import Shop

@admin.register(Shop)
class ShopAdmin(GISModelAdmin): # <-- Kế thừa từ class mới
    list_display = ('name', 'address', 'location')
    search_fields = ['name', 'address']
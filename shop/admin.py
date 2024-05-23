from django.contrib import admin
from .models import Product, Order
# Register your models here.

admin.site.site_header = 'E-Commerce Site'
admin.site.site_title = 'Shpoio Shopping'
admin.site.index_title = 'Manage Shopio'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount_price', 'category')
    def product_Custom_Field(self, request, queryset):
        queryset.update(category = 'default')

    search_fields = ('title',)
    action = ('product_Custom_Field',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
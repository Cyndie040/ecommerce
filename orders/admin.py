from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
# admin.site.register(Order)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'paid', 'placed_at']
    list_filter = ['pending_status', 'placed_at']
    search_fields = ['first_name', 'last_name', 'address']
    inlines = [OrderItemInline]
    readonly_fields = ['placed_at']
    list_display_links = ['owner', 'placed_at']
    
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
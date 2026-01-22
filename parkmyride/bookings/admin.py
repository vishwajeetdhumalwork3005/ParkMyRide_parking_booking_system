from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'slot', 'start_time', 'end_time', 'status', 'total_price')
    list_filter = ('status',)
    search_fields = ('user__username', 'slot__slot_name')

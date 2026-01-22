from django.contrib import admin
from .models import Location, ParkingSlot, ContactMessage


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')


@admin.register(ParkingSlot)
class ParkingSlotAdmin(admin.ModelAdmin):
    list_display = ('slot_name', 'location', 'vehicle_type', 'hourly_price', 'is_available')
    list_filter = ('vehicle_type', 'is_available')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    readonly_fields = ('created_at',)

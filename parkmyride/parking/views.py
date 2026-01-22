from django.shortcuts import render, get_object_or_404, redirect
from .models import ParkingSlot, Location
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models import Min

# Home page: show parking cards
def home(request):
    slots = ParkingSlot.objects.select_related('location').all()
    return render(request, 'home.html', {'slots': slots})

# Search page: filter by location, date/time, vehicle type
def search_slots(request):
    locations = Location.objects.all()
    slots = ParkingSlot.objects.select_related('location').filter(is_available=True)
    if request.method == 'GET':
        location_id = request.GET.get('location')
        vehicle = request.GET.get('vehicle_type')
        if location_id:
            slots = slots.filter(location_id=location_id)
        if vehicle:
            slots = slots.filter(vehicle_type=vehicle)
    return render(request, 'search.html', {'slots': slots, 'locations': locations})

# Admin: simple manage slots page
@login_required
def manage_slots(request):
    # In a real app, restrict to staff/superusers. Here we assume logged-in admin.
    locations = Location.objects.all()
    slots = ParkingSlot.objects.select_related('location').all()
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'add':
            loc_name = request.POST.get('location_name')
            slot_name = request.POST.get('slot_name')
            vehicle = request.POST.get('vehicle_type')
            price = request.POST.get('hourly_price')
            loc, _ = Location.objects.get_or_create(name=loc_name, defaults={'address': ''})
            ParkingSlot.objects.create(slot_name=slot_name, location=loc, vehicle_type=vehicle, hourly_price=price)
            return redirect('manage-slots')
        if action == 'delete':
            slot_id = request.POST.get('slot_id')
            ParkingSlot.objects.filter(id=slot_id).delete()
            return redirect('manage-slots')
    return render(request, 'manage_slots.html', {'slots': slots, 'locations': locations})


def pricing(request):
    """Show pricing information grouped by vehicle type."""
    prices = ParkingSlot.objects.values('vehicle_type').annotate(min_price=Min('hourly_price'))
    slots = ParkingSlot.objects.select_related('location').all()
    return render(request, 'pricing.html', {'prices': prices, 'slots': slots})


def contact(request):
    """Contact page: store messages and show a thank-you notice."""
    from .models import ContactMessage
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            return render(request, 'contact.html', {'sent': True})
        return render(request, 'contact.html', {'error': 'Please fill all fields.'})
    return render(request, 'contact.html')

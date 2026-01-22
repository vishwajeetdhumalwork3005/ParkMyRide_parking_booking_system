from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Booking
from parking.models import ParkingSlot
from django.utils import timezone
from django.contrib import messages
from django.db.models import Q
from datetime import timedelta
from django.urls import reverse

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def book_index(request):
    """Handle requests to /book/ without a slot ID.

    Redirect users to the search page where they can pick a slot.
    """
    return redirect('search')

@login_required
def book_slot(request, slot_id):
    slot = get_object_or_404(ParkingSlot, id=slot_id)
    if request.method == 'POST':
        # parse posted date/time strings (client JS should ensure proper format)
        from django.utils.dateparse import parse_datetime
        start = parse_datetime(request.POST.get('start_time'))
        end = parse_datetime(request.POST.get('end_time'))
        vehicle_number = request.POST.get('vehicle_number')
        payment_method = request.POST.get('payment_method')
        # Prevent double booking: check overlapping confirmed/pending bookings
        overlapping = Booking.objects.filter(slot=slot).filter(
            Q(start_time__lt=end) & Q(end_time__gt=start)
        ).exclude(status='Cancelled')
        if overlapping.exists():
            messages.error(request, 'This slot is already booked for the selected time range.')
            return redirect('book', slot_id=slot.id)
        # calculate price: hours * hourly_price
        duration = (end - start).total_seconds() / 3600.0
        total = round(duration * float(slot.hourly_price), 2)
        booking = Booking.objects.create(
            user=request.user,
            slot=slot,
            start_time=start,
            end_time=end,
            vehicle_number=vehicle_number,
            payment_method=payment_method,
            status='Confirmed',
            total_price=total
        )
        # Optionally mark slot unavailable
        slot.is_available = False
        slot.save()
        messages.success(request, 'Booking confirmed')
        # Redirect to a confirmation page showing booking details
        return redirect(reverse('booking-confirm', args=[booking.id]))
    return render(request, 'book.html', {'slot': slot})


@login_required
def booking_confirmation(request, booking_id):
    """Show booking confirmation details after successful booking."""
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    return render(request, 'booking_confirmation.html', {'booking': booking})

@login_required
def history(request):
    bookings = Booking.objects.filter(user=request.user).select_related('slot', 'slot__location')
    return render(request, 'history.html', {'bookings': bookings})

@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.status = 'Cancelled'
    booking.save()
    # free slot if no other active bookings overlap
    slot = booking.slot
    active = Booking.objects.filter(slot=slot).exclude(status='Cancelled')
    if not active.exists():
        slot.is_available = True
        slot.save()
    return redirect('history')

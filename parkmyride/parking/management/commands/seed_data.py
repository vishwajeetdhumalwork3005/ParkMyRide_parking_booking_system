from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    help = 'Seed sample locations, parking slots, test user, booking and contact message.'

    def handle(self, *args, **options):
        from parking.models import Location, ParkingSlot, ContactMessage
        from django.contrib.auth import get_user_model
        from bookings.models import Booking

        User = get_user_model()

        # Pune Locations
        pune_locations = [
            {"name": "Shivaji Nagar", "address": "Shivaji Nagar, Pune, Maharashtra 411005"},
            {"name": "Hinjewadi Phase 1", "address": "Hinjewadi Phase 1, Rajiv Gandhi Infotech Park, Pune, Maharashtra 411057"},
            {"name": "Wakad", "address": "Wakad, Pimpri-Chinchwad, Pune, Maharashtra 411057"},
            {"name": "Baner", "address": "Baner, Pune, Maharashtra 411045"},
            {"name": "Aundh", "address": "Aundh, Pune, Maharashtra 411007"},
            {"name": "Kothrud", "address": "Kothrud, Pune, Maharashtra 411038"},
            {"name": "Swargate", "address": "Swargate, Pune, Maharashtra 411042"},
            {"name": "Hadapsar", "address": "Hadapsar, Pune, Maharashtra 411028"},
            {"name": "Viman Nagar", "address": "Viman Nagar, Pune, Maharashtra 411014"},
            {"name": "Koregaon Park", "address": "Koregaon Park, Pune, Maharashtra 411001"},
        ]
        location_objs = {}
        for loc in pune_locations:
            obj, _ = Location.objects.get_or_create(name=loc["name"], defaults={"address": loc["address"]})
            location_objs[loc["name"]] = obj

        # Parking slots data
        slots = [
            # Shivaji Nagar
            {"slot_name": "A1", "location": location_objs["Shivaji Nagar"], "vehicle_type": "Car", "hourly_price": 60, "is_available": True, "description": "Covered parking near metro station"},
            {"slot_name": "A2", "location": location_objs["Shivaji Nagar"], "vehicle_type": "Bike", "hourly_price": 30, "is_available": True, "description": "Open bike parking near bus stop"},
            # Hinjewadi Phase 1
            {"slot_name": "B1", "location": location_objs["Hinjewadi Phase 1"], "vehicle_type": "Car", "hourly_price": 50, "is_available": True, "description": "Basement parking in IT park"},
            {"slot_name": "B2", "location": location_objs["Hinjewadi Phase 1"], "vehicle_type": "Car", "hourly_price": 70, "is_available": False, "description": "Premium covered parking"},
            # Wakad
            {"slot_name": "C1", "location": location_objs["Wakad"], "vehicle_type": "Bike", "hourly_price": 25, "is_available": True, "description": "Bike parking near market"},
            {"slot_name": "C2", "location": location_objs["Wakad"], "vehicle_type": "Car", "hourly_price": 55, "is_available": True, "description": "Car parking near residential area"},
            # Baner
            {"slot_name": "D1", "location": location_objs["Baner"], "vehicle_type": "Car", "hourly_price": 65, "is_available": True, "description": "Covered parking near shopping mall"},
            {"slot_name": "D2", "location": location_objs["Baner"], "vehicle_type": "Cycle", "hourly_price": 100, "is_available": True, "description": "Cycle parking for delivery vehicles"},
            # Aundh
            {"slot_name": "E1", "location": location_objs["Aundh"], "vehicle_type": "Bike", "hourly_price": 20, "is_available": True, "description": "Bike parking near hospital"},
            # Kothrud
            {"slot_name": "F1", "location": location_objs["Kothrud"], "vehicle_type": "Car", "hourly_price": 50, "is_available": True, "description": "Car parking near college"},
            {"slot_name": "F2", "location": location_objs["Kothrud"], "vehicle_type": "Bike", "hourly_price": 25, "is_available": False, "description": "Bike parking near gym"},
            # Swargate
            {"slot_name": "G1", "location": location_objs["Swargate"], "vehicle_type": "Car", "hourly_price": 60, "is_available": True, "description": "Covered parking near bus terminal"},
            # Hadapsar
            {"slot_name": "H1", "location": location_objs["Hadapsar"], "vehicle_type": "Car", "hourly_price": 55, "is_available": True, "description": "Open parking near railway station"},
            # Viman Nagar
            {"slot_name": "I1", "location": location_objs["Viman Nagar"], "vehicle_type": "Bike", "hourly_price": 30, "is_available": True, "description": "Bike parking near airport"},
            # Koregaon Park
            {"slot_name": "J1", "location": location_objs["Koregaon Park"], "vehicle_type": "Car", "hourly_price": 80, "is_available": True, "description": "Premium car parking near restaurants"},
        ]
        created_slots = []
        for s in slots:
            obj, _ = ParkingSlot.objects.get_or_create(
                slot_name=s["slot_name"],
                location=s["location"],
                defaults={
                    "vehicle_type": s["vehicle_type"],
                    "hourly_price": s["hourly_price"],
                    "is_available": s["is_available"],
                    "description": s["description"],
                }
            )
            created_slots.append(obj)

        # Test user
        if not User.objects.filter(username='testuser@example.com').exists():
            user = User.objects.create_user(username='testuser@example.com', email='testuser@example.com', password='testpass', first_name='Test', last_name='User')
            self.stdout.write(self.style.SUCCESS('Created test user: testuser@example.com / testpass'))
        else:
            user = User.objects.get(username='testuser@example.com')

        # Sample booking for first slot
        if created_slots:
            slot = created_slots[0]
            start = timezone.now() + timedelta(hours=1)
            end = start + timedelta(hours=2)
            overlapping = Booking.objects.filter(slot=slot).filter(start_time__lt=end, end_time__gt=start).exclude(status='Cancelled')
            if not overlapping.exists():
                Booking.objects.create(user=user, slot=slot, start_time=start, end_time=end, vehicle_number='ABC-1234', payment_method='Card', status='Confirmed', total_price=round(((end-start).total_seconds()/3600.0)*float(slot.hourly_price),2))
                slot.is_available = False
                slot.save()
                self.stdout.write(self.style.SUCCESS(f'Created booking for slot {slot.slot_name}'))

        # Contact message
        ContactMessage.objects.get_or_create(email='visitor@example.com', defaults={'name': 'Visitor', 'message': 'This is a sample contact message.'})

        self.stdout.write(self.style.SUCCESS('Seeding complete.'))

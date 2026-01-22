from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book_index, name='book-index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('book/<int:slot_id>/', views.book_slot, name='book'),
    path('book/confirm/<int:booking_id>/', views.booking_confirmation, name='booking-confirm'),
    path('history/', views.history, name='history'),
    path('cancel/<int:booking_id>/', views.cancel_booking, name='cancel-booking'),
]

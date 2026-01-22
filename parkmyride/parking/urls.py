from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pricing/', views.pricing, name='pricing'),
    path('search/', views.search_slots, name='search'),
    path('contact/', views.contact, name='contact'),
    path('manage-slots/', views.manage_slots, name='manage-slots'),
]

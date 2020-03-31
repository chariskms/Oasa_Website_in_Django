from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('directions', views.directions, name='directions'),
    path('itineraries', views.itineraries, name='itineraries'),
    path('maps', views.maps, name='maps'),
    path('tickets', views.tickets, name='tickets'),
    path('login', views.login, name='login'),
    path('editProfile', views.editProfile, name='editProfile'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('tickets/ticketCart', views.ticketCart, name='ticketCart'),
    path('tickets/loadCard', views.loadCard, name='loadCard'),
    path('amea', views.amea, name='amea'),
    path('contact', views.contact, name='contact'),
    path('org_oasa', views.org_oasa, name='org_oasa'),
    path('searchStations', views.searchStations, name='searchStations'),
    path('searchAStation', views.searchAStation, name='searchAStation'),
    path('metroStations', views.metroStations, name='metroStations'),
    path('busStations', views.busStations, name='busStations'),
    path('tramStations', views.tramStations, name='tramStations')

]

from django.urls import path
from .views import *

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('raffle_entry/', raffle_entry, name='raffle_entry'),
    path('raffle_result/', raffle_result, name='raffle_result'),
]

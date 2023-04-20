from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import RaffleEntry
import random

def landing_page(request):
    return render(request, 'landing.html')

def raffle_entry(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        existing_entry = RaffleEntry.objects.filter(email=email).first()
        if existing_entry:
            return render(request, 'raffle_entry.html', {'error': 'Email already registered!'})
        else:
            entry = RaffleEntry(name=name, email=email)
            entry.save()
            return HttpResponseRedirect('/raffle_result/')
    else:
       return render(request, 'raffle_entry.html')

# def raffle_result(request):
#     winners = Entry.objects.order_by('?')[:3]
#     return render(request, 'raffle_result.html', {'winners': winners})

def raffle_result(request):
    entries = RaffleEntry.objects.all()
    winners = random.sample(list(entries), 1) if len(entries) >= 10 else []
    return render(request, 'raffle_result.html', {'winners': winners})
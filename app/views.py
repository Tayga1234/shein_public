from django.shortcuts import render
from .models import *


def index(request):
    countdown_event = Countdown.objects.last() 
    accueil = Accueil.objects.first() 
    topbar = Topbar.objects.first() 
    about = About.objects.first() 
    footer = Footer.objects.first()
    evaluation = Evaluation.objects.first() 

    context = {
        'date': countdown_event.date,
        'vague_name': countdown_event.vague_name,
        'accueil': accueil,
        'topbar': topbar,
        'about': about,
        'footer': footer, 
        'evaluation': evaluation,
         # Add more context variables as needed to populate the template with the necessary data.
    }
    return render(request, 'index.html', context)
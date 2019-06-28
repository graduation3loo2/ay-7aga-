from django.shortcuts import render
from .models import Vote, Response, Agencies

def votes(request):

    agencies = Agencies.objects.all()
    votes_all = Vote.objects.all()
    responses = Response.objects.all()

    context = {
        'votes_all': votes_all,
        'responses': responses,
        'agencies': agencies,
    }

    return render(request, 'votes.html', context)

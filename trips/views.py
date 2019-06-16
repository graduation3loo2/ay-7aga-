from django.shortcuts import render



def trips(request):
    return render(request, 'trips.html')

import datetime
from django.shortcuts import render
from .models import *


def agency(request, agency_name):
    agency_id = Agencies.objects.get(name__icontains=agency_name).agency_id

    q = request.GET.get('button')

    if q == 'available':
        obj = available(agency_id)
        return render(request, "agency_trips.html", obj)

    elif q == 'votes':
        obj = agency_votes(agency_id)
        return render(request, 'agency_votes.html', obj)

    elif q == 'account':
        obj = agency_info(agency_id)
        return render(request, 'agency_info.html', obj)

    else:
        obj = history(agency_id)
        return render(request, "agency_trips.html", obj)


def available(agency_id):
    company = Agencies.objects.get(agency_id=agency_id)
    trip = Trips.objects.filter(agency_id=agency_id, deadline__gt=datetime.date.today())
    for t in trip:
        t.duration = t.date_to.date() - t.date_from.date()

    active = 'active'
    inactive = 'inactive'
    obj = {
        "agency": company,
        "trips": trip,
        "history": inactive,
        "available": active,
    }
    return obj


def history(agency_id):
    company = Agencies.objects.get(agency_id=agency_id)
    trip = Trips.objects.filter(agency_id=agency_id, deadline__lt=datetime.date.today()).order_by('deadline')
    for t in trip:
        t.duration = t.date_to.date() - t.date_from.date()

    active = 'active'
    inactive = 'inactive'
    obj = {
        "agency": company,
        "trips": trip,
        "history": active,
        "available": inactive,
    }
    return obj


def agency_votes(agency_id):
    company = Agencies.objects.filter(agency_id=agency_id)[0]
    votes = Vote.objects.filter(agency_id=agency_id)
    obj = {
        "votes": votes,
        "agency": company,
    }
    return obj


def agency_info(agency_id):
    company = Agencies.objects.get(agency_id=agency_id)
    obj = {
        "agency": company,
    }
    return obj

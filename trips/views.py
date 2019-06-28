from django.shortcuts import render
from .models import *
from .forms import SearchForm
from django.db.models import Q


def trips_main(request):
    return render(request, 'trips_main.html')


def trips(request):
    trip = Trips.objects.all()
    form = SearchForm()

    if request.POST.get('select', None):
        sort_option = request.POST.get('select')
        trip = trip.order_by(sort_option)

    for t in trip:
        t.duration = t.date_to.date() - t.date_from.date()

    obj = {
        'trips': trip,
        'form': form,
    }

    return render(request, 'trips.html', obj)


def trips_form(request):
    if request.method == 'GET':
            form = SearchForm(request.GET)
            if form.is_valid():
                city = form.cleaned_data['Destination']
                date_from = form.cleaned_data['Date']
                date_to = form.cleaned_data['Date2']
                price = form.cleaned_data['price']
                meals = form.cleaned_data['meals']
                agency = form.cleaned_data['agency']
                filters = []
                if agency != '':
                    agencyiesIDS = Agencies.objects.filter(name__icontains=agency)
                    ids = []
                    for agencyID in agencyiesIDS:
                        idd = agencyID.agency_id
                        ids.append(idd)
                    agencyfilter = Trips.objects.filter(agency_id__in=ids)
                    filters.append(agencyfilter)
                if date_from is not None and date_to is not None:
                    datefilter = Trips.objects.filter(Q(date_from__gte=date_from) & Q(date_to__lte=date_to))
                    filters.append(datefilter)
                elif date_from is not None:
                    date_fromfilter = Trips.objects.filter(date_from__gte=date_from)
                    filters.append(date_fromfilter)
                elif date_to is not None:
                    date_tofilter = Trips.objects.filter(date_to__lte=date_to)
                    filters.append(date_tofilter)
                if price is not None:
                    price_filter = Trips.objects.filter(price__lte=price)
                    filters.append(price_filter)

                if city is not '':
                    cityfilter = Trips.objects.filter(to_location__icontains=city)
                    filters.append(cityfilter)
                if meals in ['fullboard', 'halfboard']:
                    mealfilter=Trips.objects.filter(meals__exact=meals)
                    filters.append(mealfilter)
                if len(filters) > 0:
                    trips = filters[0]
                    for Filter in filters:
                        trips = trips | Filter

                    context = {
                        'trips': trips,
                        'form': form,
                    }
                    return render(request, 'trips.html', context)

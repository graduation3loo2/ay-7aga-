from django.shortcuts import render, get_object_or_404
from .models import *



def agencies(request):
    agens = Agencies.objects.all()
    follow = Follows.objects.filter(user_id__exact=1)
    query = request.GET.get("q")
    if query:
        agens = Agencies.objects.filter(name__icontains=query)
    obj = {
        'agens': agens,
        'follow': follow,
    }
    btnQuery = request.GET.get("btnFollow")
    if btnQuery:
        Follows.objects.create(user_id=1, agency_id=btnQuery)
    return render(request, 'agencies.html', obj)





from django.shortcuts import render, redirect
from .models import *


def agencies(request):
    company = Agencies.objects.all()
    query = request.GET.get("q")
    if query:
        company = Agencies.objects.filter(name__icontains=query)
    if "user_id" in request.session != None:
        user_id = request.session['user_id']
        follows = Follows.objects.filter(user_id=user_id)
        followed = get_follow(company, follows)
        obj = {
            "agency": company,
            "follow": followed,
        }

    else:

        obj = {
            "agency": company,
        }
    return render(request, "agencies.html", obj)


def main(request):
    agencies(request)
    return render(request, 'main.html')


def follow(request):
    if request.method == "POST":
        user_id = request.session['user_id']
        agency_id = request.POST['btnFollow']
        Follows.objects.create(user_id=user_id, agency_id=agency_id)
    return redirect(agencies)


def un_follow(request):
    if request.method == "POST":
        user_id = request.session['user_id']
        agency_id = request.POST['btnUnfollow']
        Follows.objects.filter(user_id=user_id, agency_id=agency_id).delete()
    return redirect(agencies)


def get_follow(agencies_follow, follows):
    agency_follow = []
    for a in agencies_follow:
        followed = False
        if follows.filter(agency_id=a.agency_id).exists():
            followed = True
        following = {
                'agency': a.agency_id,
                'follow': followed
            }
        agency_follow.append(following)
    return agency_follow

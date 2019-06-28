from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from home import views



def users(request):

        if "user_id" in request.session != None:
            user_id = request.session['user_id']
            user = Users.objects.filter(user_id=user_id)[0]
            going_trips = GoingTo.objects.filter(user_id=user_id)
            agencies = Follows.objects.filter(user_id=user_id)

            obj = {
                'user': user,
                'trips': going_trips,
                'agencies': agencies,
            }
            return render(request, 'user.html', obj)
        else:
            return HttpResponse("ERROR USER NOT SIGNED IN")
def signout(request):
    del request.session['user_id']
    return redirect(views.home)

import datetime
from django.shortcuts import render ,redirect
from .models import *
from cryptography.fernet import Fernet
import base64
from Exoduss import settings
from django.http import HttpResponse


def home(request):
    votes = Vote.objects.all().order_by('vote_id').reverse()[:0]

    trips = Trips.objects.raw('SELECT t.*, COUNT(g.`User_id`) AS going_to '
                              'FROM `Exodus`.`Trips` t '
                              'LEFT JOIN `Exodus`.`going_to` g ON t.`trip_id` = g.`Trip_id` '
                              'Where t.`Deadline` > CURDATE() GROUP BY t.`Trip_id` '
                              'ORDER BY going_to DESC '
                              'LIMIT 4;')

    agencies = Agencies.objects.raw('SELECT a.*, COUNT(f.`agency_id`) AS followers '
                                    'FROM `Exodus`.`Agencies` a '
                                    'LEFT JOIN `Exodus`.`Follows` f ON a.`Agency_id` = f.`agency_id` '
                                    'GROUP BY a.`Agency_id` '
                                    'ORDER BY followers DESC '
                                    'LIMIT 4;')
    most_trips = Trips.objects.filter(deadline__gt=datetime.datetime.today()).order_by('trip_id').reverse()[:4]
    if "user_id" in request.session != None:
        user_id = request.session['user_id']
        user = Users.objects.filter(user_id=user_id)[0]
        obj = {
            'votes': votes,
            'most_going': trips,
            'agencies': agencies,
            'most_trips': most_trips,
            'user': user

        }
    else:
        user = 0
        obj = {
            'votes': votes,
            'most_going': trips,
            'agencies': agencies,
            'most_trips': most_trips,
            'user': user

        }
    return render(request, 'home.html', obj)


def sign_up(request):
    name = request.POST["username"]
    email=request.POST["email"]
    phone=request.POST["number"]
    city = request.POST["city"]
    password = request.POST["psw"]
    re_password = request.POST["repsw"]

    unique_mail = Users.objects.filter(e_mail__iexact=email)
    print(unique_mail)
    if not unique_mail:
        if password == re_password:
            # get the key from settings
            cipher_suite = Fernet(settings.ENCRYPT_KEY)  # key should be byte
            # #input should be byte, so convert the text to byte
            encrypted_text = cipher_suite.encrypt(password.encode('ascii'))
            # encode to urlsafe base64 format
            encrypted_text = base64.urlsafe_b64encode(encrypted_text).decode("ascii")
            Users.objects.create(name=name, e_mail=email, password=encrypted_text, phone=phone, city=city)
            return redirect(home)
        else:
            return HttpResponse("PASSWORD NOT COMPATIBLE")
    else:
        return HttpResponse("EMAIL ALREADY EXISTS")


def sign_in(request):
    if request.method == "POST":
        if request.method == "POST":
            email = request.POST["email"]
            psw = request.POST["psw"]
            insure = Users.objects.filter(e_mail__iexact=email)
            if not insure:
                return HttpResponse("WRONG E-MAIL OR PASSWORD")



            else:

                user = Users.objects.get(e_mail__iexact=email)
                passw = user.password
                txt = base64.urlsafe_b64decode(passw)
                cipher_suite = Fernet(settings.ENCRYPT_KEY)
                decoded_text = cipher_suite.decrypt(txt).decode("ascii")
                if decoded_text == psw:
                    request.session['user_id'] = user.user_id

                    return redirect(home)
                else:
                    return HttpResponse("WRONG E-MAIL OR PASSWORD")
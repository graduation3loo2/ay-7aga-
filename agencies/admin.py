from django.contrib import admin

from .models import *

admin.site.register(Agencies)
admin.site.register(Phones)
admin.site.register(Users)
admin.site.register(Follows)
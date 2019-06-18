
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agencies/', include('agencies.urls')),
    path('', include('home.urls')),
    path('trips/', include('trips.urls')),
    path('votes/', include('votes.urls')),
    path('user/', include('user.urls'))

]
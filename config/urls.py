
from django.contrib import admin
from django.urls import path
from events.urls import urlpatterns as events_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += events_urlpatterns

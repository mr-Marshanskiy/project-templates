from django.urls import path, include
from rest_framework.routers import DefaultRouter

from events.views import birthday

app_name = 'events'
router = DefaultRouter()

router.register(r'birthdays', birthday.EventsClientsBirthdayView, basename='birthdays')


urlpatterns = [
    path('events/', include(router.urls)),
]

from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from events.factory.birthday import BirthdayFactory
from events.serializers.api.birthday import BirthdaySeriallizer


class EventsClientsBirthdayView(ListModelMixin, GenericViewSet):
    queryset = BirthdayFactory.birthdays_list()
    serializer_class = BirthdaySeriallizer

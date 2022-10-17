import datetime

from django.db.models import F, Func, IntegerField, Case, When, Q
from django.db.models.functions import ExtractYear, Extract, Cast

from events.models.events import Event


class BirthdayFactory:

    @staticmethod
    def birthdays_list():
        queryset = Event.objects.annotate(
            event_id=F('id'),
            event_name=F('name'),
            event_start=F('date_start'),
            event_end=F('date_end'),
            client_id=F('clients__id'),
            client_first_name=F('clients__first_name'),
            client_last_name=F('clients__last_name'),
            client_dob=F('clients__dob'),
            age=Extract(
                Func(F('date_end'), F('clients__dob'), function='age'), 'year'
            ),

            # dob
            dob_year=Extract(F('clients__dob'), 'year'),
            dob_year_div_4=Cast(F('dob_year'), IntegerField()) % 4,
            dob_year_div_100=Cast(F('dob_year'), IntegerField()) % 100,
            dob_year_div_400=Cast(F('dob_year'), IntegerField()) % 400,
            is_dob_leap_year=Case(
                When(
                    Q(Q(dob_year_div_4=0) & ~Q(dob_year_div_100=0))
                    | Q(dob_year_div_400=0), then=True
                ),
                default=False
            ),
            doy_dob_base=Extract(F('clients__dob'), 'doy'),
            doy_dob=Case(
                When(
                    Q(is_dob_leap_year=True, doy_dob_base__gt=60),
                    then=F('doy_dob_base') - 1),
                default=F('doy_dob_base'),
            ),

            # date start
            date_start_year=Extract(F('date_start'), 'year'),
            date_start_year_div_4=Cast(F('date_start_year'), IntegerField()) % 4,
            date_start_year_div_100=Cast(F('date_start_year'), IntegerField()) % 100,
            date_start_year_div_400=Cast(F('date_start_year'), IntegerField()) % 400,
            is_date_start_leap_year=Case(
                When(
                    Q(Q(date_start_year_div_4=0) & ~Q(date_start_year_div_100=0))
                    | Q(date_start_year_div_400=0), then=True
                ),
                default=False
            ),
            doy_date_start_base=Extract(F('date_start'), 'doy'),
            doy_date_start=Case(
                When(
                    Q(is_date_start_leap_year=True, doy_date_start_base__gt=60),
                    then=F('doy_date_start_base') - 1),
                default=F('doy_date_start_base'),
            ),

            # date end
            date_end_year=Extract(F('date_end'), 'year'),
            date_end_year_div_4=Cast(F('date_end_year'), IntegerField()) % 4,
            date_end_year_div_100=Cast(F('date_end_year'), IntegerField()) % 100,
            date_end_year_div_400=Cast(F('date_end_year'), IntegerField()) % 400,
            is_date_end_leap_year=Case(
                When(
                    Q(Q(date_end_year_div_4=0) & ~Q(
                        date_end_year_div_100=0))
                    | Q(date_end_year_div_400=0), then=True
                ),
                default=False
            ),
            doy_date_end_base=Extract(F('date_end'), 'doy'),
            doy_date_end=Case(
                When(
                    Q(is_date_end_leap_year=True, doy_date_end_base__gt=60),
                    then=F('doy_date_end_base') - 1),
                default=F('doy_date_end_base'),
            ),

        ).filter(
            Q(
                Q(date_start_year=F('date_end_year'))
                & Q(doy_dob__gte=F('doy_date_start'))
                & Q(doy_dob__lte=F('doy_date_end'))
            )

            | Q(
                Q(date_end_year__gt=F('date_start_year'))
                & (
                    Q(doy_dob__gte=F('doy_date_start'))
                    | Q(doy_dob__lte=F('doy_date_end'))
                )
            )
        )
        return queryset

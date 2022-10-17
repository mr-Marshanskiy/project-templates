from rest_framework import serializers


class BirthdaySeriallizer(serializers.Serializer):
    event_id = serializers.IntegerField()
    event_name = serializers.CharField()
    event_start = serializers.DateField()
    event_end = serializers.DateField()
    client_id = serializers.IntegerField()
    client_first_name = serializers.CharField()
    client_last_name = serializers.CharField()
    client_dob = serializers.DateField()
    age = serializers.IntegerField()
    doy_dob = serializers.IntegerField()
    doy_date_start = serializers.IntegerField()
    doy_date_end = serializers.IntegerField()

    class Meta:
        fields = (
            'event_id',
            'event_name',
            'event_start',
            'event_end',
            'client_id',
            'client_first_name',
            'client_last_name',
            'client_dob',
            'age',
            'doy_dob',
            'doy_date_start',
            'doy_date_end',

        )

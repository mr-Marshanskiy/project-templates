from django.db import models


class Client(models.Model):
    """
        events - events.Event.clients
    """
    first_name = models.CharField('First name', max_length=32)
    last_name = models.CharField('Last name', max_length=32)
    dob = models.DateField('Day of Birthday')

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return f'Client #{self.pk}. {self.first_name} {self.last_name}'

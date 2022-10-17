from django.db import models


class Event(models.Model):
    date_start = models.DateField('Date start')
    date_end = models.DateField('Date end')
    name = models.CharField('Event name', max_length=127)
    clients = models.ManyToManyField(
        'clients.Client', 'events', verbose_name='Clients'
    )

    class Meta:
        verbose_name = 'Events'
        verbose_name_plural = 'Events'

    def __str__(self):
        return f'Event #{self.pk}. {self.name} ({self.date_start} - {self.date_end})'

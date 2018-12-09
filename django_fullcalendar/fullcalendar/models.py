from django.db import models
from django.utils.translation import ugettext_lazy as _


class CalendarEvent(models.Model):
    """
    The event set a record for an activity that will
    be scheduled at a specified date and time.
    
    It could be on a date and time to start and end,
    but can also be all day.
    """
    title = models.CharField(_('Title'), blank=True, max_length=200)
    start = models.DateTimeField(_('Start'))
    end = models.DateTimeField(_('End'))
    all_day = models.BooleanField(_('All day'), default=False)

    class Meta:
        verbose_name = _('Event')
        verbose_name_plural = _('Events')

    def __str__(self):
        return self.title

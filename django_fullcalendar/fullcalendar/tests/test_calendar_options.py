from django.test import TestCase

from ..util import calendar_options


class CalendarOptions(TestCase):
    def test_options_string(self):
        s = ('{timeFormat: "H:mm",'
             ' header: {left: "prev,next today", center: '
             '"title", right: "month,agendaWeek,agendaDay",}')
        self.assertEqual(calendar_options('all_events/', s),
                         ('{events: "all_events/", '
                          'timeFormat: "H:mm", '
                          'header: {left: "prev,'
                          'next today", '
                          'center: "title", '
                          'right: "month,agendaWeek,agendaDay",}'))

    def test_options_string_with_whitespaces(self):
        s = ('   {timeFormat: "H:mm", '
             'header: {left: "prev,next today", center: "title", '
             'right: "month,agendaWeek,agendaDay",}    ')
        self.assertEqual(calendar_options('all_events/', s),
                         ('{events: "all_events/", '
                          'timeFormat: "H:mm", '
                          'header: {left: "prev,'
                          'next today", center: "title", '
                          'right: "month,agendaWeek,agendaDay",}'))

    def test_options_empty_string(self):
        s = ''
        self.assertEqual(calendar_options('all_events/', s),
                         '{events: "all_events/"}')

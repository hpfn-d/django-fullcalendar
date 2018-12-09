from django.test import TestCase

from ..util import convert_field_names


class ConvertFieldNames(TestCase):
    def test_conversion(self):
        list_param = [
            {'start': '2013-11-27',
             'end': '2013-11-29',
             'all_day': 'true',
             '__size__': 1,
             '__to_string__': 'false'},
            {'start': '2013-11-27',
             'end': '2013-11-29',
             'all_day': 'true',
             '__size__': 1,
             '__to_string__': 'false'},
        ]

        expected = [
            {'start': '2013-11-27', 'end': '2013-11-29',
             'allDay': 'true', '__size__': 1, '__toString__': 'false'},
            {'start': '2013-11-27', 'end': '2013-11-29',
             'allDay': 'true', '__size__': 1, '__toString__': 'false'}
        ]
        self.assertEqual(convert_field_names(list_param), expected)

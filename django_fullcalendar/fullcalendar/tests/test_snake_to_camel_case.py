from django.test import TestCase

from ..util import snake_to_camel_case


class CamelCaseTest(TestCase):
    def test_one_word_variable(self):
        s = 'one'
        self.assertEqual(snake_to_camel_case(s), 'one')

    def test_two_word_variable(self):
        s = 'two_word'
        self.assertEqual(snake_to_camel_case(s), 'twoWord')

    def test_three_word_variable(self):
        s = 'three_word_variable'
        self.assertEqual(snake_to_camel_case(s), 'threeWordVariable')

    def test_startswith_one_underscore(self):
        s = '_one_under'
        self.assertEqual(snake_to_camel_case(s), '_oneUnder')

    def test_startswith_two_underscores(self):
        s = '__two_under'
        self.assertEqual(snake_to_camel_case(s), '__twoUnder')

    def test_starts_ends_with_one_underscore(self):
        s = '_one_under_'
        self.assertEqual(snake_to_camel_case(s), '_oneUnder_')

    def test_starts_ends_with_two_underscores(self):
        s = '__two_under__'
        self.assertEqual(snake_to_camel_case(s), '__twoUnder__')

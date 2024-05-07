import unittest

from accounting import menu_option
from accounting import get_balance
class TestMainScript(unittest.TestCase):
    def setUp(self):
        menu_option = 's'

    def test_option_int(self):
        assert menu_option.isdecimal()

    def test_get_balance(self):
        assert isinstance(get_balance(), float)
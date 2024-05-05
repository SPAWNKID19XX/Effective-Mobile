import datetime, pytest
import unittest


class Menu:
    def __init__(self, title_menu=None, left=None, right=None):
        '''
        constructor witch warante me a correct view
        :param title_menu: "My Accounting"
        :param left: at least 20
        :param right: at least 20
        :param menu_dict: {
            '1': "Expanse",
            '2': "Income",
            '3': "Accounting list"
        }
        '''
        self.title_menu = title_menu if title_menu is not None else "My Accounting"
        self.left = left if left is not None and left >= 20 else 20
        self.right = right if right is not None and right >= 20 else 20
        self.menu_dict = {
            '1': "Expanse",
            '2': "Income",
            '3': "Accounting list"
        }

    def __str__(self):
        result = self.title_menu.center(self.left + self.right, '*') + '\n'
        result += 'Balance'.ljust(self.left, ".") + 'float(balance)'.rjust(self.right, '.') + '\n'
        for k, v in self.menu_dict.items():
            result += k.ljust(self.left, ".") + v.rjust(self.right, '.') + '\n'
        return result

menu = Menu()
print(menu.__str__())


class TestMenu(unittest.TestCase):
    def setUp(self):
        menu = Menu()

    def test_menu_title_menu(self):
        assert menu.title_menu == "My Accounting"

    def test_menu_k_v(self):
        assert menu.menu_dict == {
            '1': "Expanse",
            '2': "Income",
            '3': "Accounting list"
        }

    def test_menu_LEFTWIDTH(self):
        assert menu.left >= 20

    def test_menu_RIGHTWIDTH(self):
        assert menu.right >= 20

    def test_assert_len_title_and_each_of_menu_point(self):
        menu_list = menu.__str__().splitlines()
        for obj in menu_list:
            assert len(menu.title_menu.center(menu.left + menu.right, '*')) == len(obj)







if __name__ == "__main__":
    unittest.main()

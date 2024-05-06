import unittest
from accounting import Menu


class TestMenu(unittest.TestCase):
    def setUp(self):
        self.menu = Menu()

    def test_menu_title_menu(self):
        assert self.menu.title_menu == "My Accounting"

    def test_menu_k_v(self):
        assert self.menu.menu_dict == {
            '1': "Expanses",
            '2': "Add Expanse",
            '3': "Incomes",
            '4': "Add Income",
            '5': "Accounting list",
            '6': "Search",
            '7': "Edit",
            '0': "Exit"
        }

    def test_menu_LEFTWIDTH(self):
        assert self.menu.left >= 20

    def test_menu_RIGHTWIDTH(self):
        assert self.menu.right >= 20

    def test_assert_len_title_and_each_of_menu_point(self):
        menu_list = self.menu.__str__().splitlines()
        for obj in menu_list:
            assert len(self.menu.title_menu.center(self.menu.left + self.menu.right, '*')) == len(obj)


if __name__ == '__main__':
    unittest.main()
import unittest
from datetime import datetime
from accounting import Record


class TestRecords(unittest.TestCase):
    def setUp(self):
        self.record = Record()

    def test_record_data(self):
        assert isinstance(self.record.date, datetime)

    def test_record_data_update(self):
        assert isinstance(self.record.date_updated, datetime)

    def test_record_category(self):
        self.assertIn(self.record.category, [Record.Category.income[1], Record.Category.expense[1]])

    def test_record_amount(self):
        assert self.record.amount >= 0

    def test_record_description(self):
        assert self.record.description == None or isinstance(self.record.description, str)

if __name__ == '__main__':
    unittest.main()
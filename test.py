import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from datetime import date
import unittest
import cnholiday


class cnholidayTester(unittest.TestCase):
    def test_2018(self):
        self.assertTrue(cnholiday.isHoliday(date(2018, 1, 1)))
        self.assertFalse(cnholiday.isHoliday(date(2018, 2, 11)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 2, 15)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 2, 16)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 2, 17)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 2, 18)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 2, 19)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 2, 20)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 2, 21)))
        self.assertFalse(cnholiday.isHoliday(date(2018, 2, 24)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 4, 5)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 4, 6)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 4, 7)))
        self.assertFalse(cnholiday.isHoliday(date(2018, 4, 8)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 4, 29)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 4, 30)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 5, 1)))
        self.assertFalse(cnholiday.isHoliday(date(2018, 4, 28)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 6, 18)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 9, 24)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 10, 1)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 10, 2)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 10, 3)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 10, 4)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 10, 5)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 10, 6)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 10, 7)))
        self.assertFalse(cnholiday.isHoliday(date(2018, 9, 29)))
        self.assertFalse(cnholiday.isHoliday(date(2018, 9, 30)))

        self.assertFalse(cnholiday.isHoliday(date(2018, 8, 17)))
        self.assertTrue(cnholiday.isHoliday(date(2018, 8, 18)))

    # def test_2017(self):
    #     self.assertTrue(cnholiday.isHoliday(date(2017, 1, 1)))




unittest.main()

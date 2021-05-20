import unittest
import leapYear

class Testing(unittest.TestCase):
    def test_leapYear(self):        #will pass if input is leap year
        result = leapYear.is_leap_year(2002)
        self.assertTrue(result)

    def test_leapYear2(self):       #will pass if input is NOT leap year
        result = leapYear.is_leap_year(2002)
        self.assertFalse(result)

        

if __name__ == "__main__":
    unittest.main()
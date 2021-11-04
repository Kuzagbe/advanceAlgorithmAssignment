from main import sockMerchant
import unittest

class Test(unittest.TestCase):
    def test_case_one(self):
        arr = [25, 25, 82, 82, 100, 100, 25, 49, 25, 49, 93, 53, 53, 33, 87, 41, 41, 90, 96, 89, 89, 64, 95, 63, 90, 94,
               85, 66, 94, 13]
        num = 30
        final_output = 10
        self.assertEqual(sockMerchant(num, arr), final_output)

    def test_case_two(self):
        arr = [10, 10, 10, 10, 10, 10, 10, 10, 18, 10, 10, 10, 10, 10, 10, 10, 16, 10, 10, 10, 10, 10, 10, 10, 10, 10,
               10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 90, 10, 10, 10, 20, 10, 85, 10, 10, 10,
               10, 10, 40, 10, 10, 10, 10, 10, 20, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 22, 10,
               10, 9]
        num = 80
        final_output = 36
        self.assertEqual(sockMerchant(num, arr), final_output)

if __name__ == '__main__':
    unittest.main()
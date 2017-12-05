import unittest
import day1.workwtetwin


class workwtetwinTestCase(unittest.TestCase):
    """ testing the worktwtetwin script"""

    def setUp(self):
        """initialisation """
        self.name1 = day1.workwtetwin.name1
        self.age = day1.workwtetwin.age

    def test_name(self):
        """ tests if name mariam is printed"""
        name = day1.workwtetwin.name
        self.assertEqual(name, 'mariam')

    def test_number(self):
        """ tests if num is printed"""
        num = day1.workwtetwin.num
        self.assertEqual(num, 12)

    def test_user_name_age(self):
        """test for user name """

        self.assertIsInstance(self.name1, str)
        self.assertIsInstance(self.age, int)

    def test_function(self):
        """ test read input function"""
        greet = day1.workwtetwin.read_input(self.name1, self.age)
        self.assertEqual("hey, {}  {} old".format(self.name1, self.age), greet)


if __name__ == "__main__":
    unittest.main()

import unittest
import workwtetwin

class workwtetwinTestCase(unittest.TestCase):
    """ testing the worktwtetwin script"""
    
    def setUp(self):
        """initialisation """
        pass

    def test_name(self):
        """ tests if name mariam is printed"""
        name = workwtetwin.name
        self.assertEqual(name, 'mariam')

    def test_number(self):
        """ tests if num is printed"""
        num = workwtetwin.num
        self.assertEqual(num, 12)

        
        
if __name__ == "__main__":
    unittest.main()


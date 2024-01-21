#!/usr/bin/python3
import unittest
from models.base import Base


def setUpModule():
    """setup module for testing"""
    print("setup module")


def tearDownModule():
    """Tear down module after testing"""
    print("teardown module")


class TestBase(unittest.TestCase):

    def setup(self):
        """import module, create an instance"""
        # print("Crate test for base module ...\n")
        print("Test status: Start ...")
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Tear down after each method"""
        print(f"{self.__class__.__name__} {self._testMethodName}: done...")
        pass

# Test ----------- #1 -----------

    def test_id_with_Values(self):
        """ID with value"""
        base_with_id = Base(id=5)
        self.assertEqual(base_with_id.id, 5)
        """ID with no value"""

    def test_id_without_values(self, base_1=Base(), base_2=Base(), base_3=Base(), base_4=Base()):
        """Test ID increment"""
        self.assertEqual(base_1.id, 1)
        self.assertEqual(base_2.id, 2)
        self.assertEqual(base_3.id, 3)
        self.assertEqual(base_4.id, 4)
            
    def test_constructor(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__()
        msg = "Base.__init__() missing 1 required positional argument: 'self'"
        self.assertEqual(str(e.exception), msg)

    def test_constructor_args_2(self):
        '''Tests constructor signature with 2 notself args.'''
        with self.assertRaises(TypeError) as e:
            Base.__init__(self, 1, 2)
        msg = "Base.__init__() takes from 1 to 2 positional arguments but 3 were given"
        self.assertEqual(str(e.exception), msg)

    def test_constructor_has_attribute(self):
        """Constructor has the number of objects attribute"""
        b1 = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b1.id)
    
    def test_custome_id(self):
        """get the id value from a variable"""
        i = 95
        base_1 = Base(id=i)
        self.assertEqual(base_1.id, i)
    
# Test ----------- # -----------

if __name__ == '__main__':
    unittest.main()

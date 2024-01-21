#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Unittest for the Rectangle Class"""

    def setUp(self):
        """Start module test"""
        print(f"{self.__class__.__name__} {self._testMethodName}: Start...")
    
    def tearDown(self):
        """Teardown after test"""
        print(f"{self.__class__.__name__} {self._testMethodName}: done")

    def test_constructor_init(self):
        width_1 = 5
        height_1 = 10
        rectangle_1 = Rectangle(width_1, height_1)
        self.assertEqual(rectangle_1.width, 5)

    def test_define_object(self):
        expected_result = '<models.rectangle.Rectangle object at'
        rectangle = Rectangle(10, 5)
        # <class '__main__.Rectangle'>.
        self.assertIn(expected_result, str(rectangle))


        

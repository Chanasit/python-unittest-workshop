from unittest import TestCase
from mock import patch
from app import Example


class TestExampleWithLibs(TestCase):
    

    def test_case1(self):
        example = Example()
        actual = example.add(1,2)
        expect = 3
        
        self.assertEqual(actual,expect,"should be return 3")


    def test_case2(self):
        example = Example()
        actual = example.add(5,1000)
        expect = 1005

        self.assertEqual(actual,expect,"should be return 1005")

    @patch('random.randint')
    def test_case3(self, randint_mock):

        randint_mock.return_value = 3

        example = Example()
        actual = example.random_with_constant(3)

        self.assertEqual(actual, 6)
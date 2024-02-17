from unittest import TestCase
from mock import patch
from services.calculator import CalculatorService
from repositories.random import RandomRepository


class TestCalculatorService(TestCase):


    @patch("repositories.random.RandomRepository")
    def test_case1(self, random_repo):

        cal_srv = CalculatorService(random_repo)
        actual = cal_srv.add(1, 2)
        expect = 3
        self.assertEqual(actual, expect, "should be return 3")


    @patch("repositories.random.RandomRepository")
    def test_case2(self, random_repo: RandomRepository):

        random_repo.one_to_three.return_value = 3

        cal_srv = CalculatorService(random_repo)

        actual = cal_srv.random_with_constant(3)
        expect = 6

        self.assertEqual(actual, expect, "should be equal randint_mock + constant input")

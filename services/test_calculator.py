from unittest import TestCase
from services.calculator import CalculatorService, RandomRepository


# Manual mock random repository
class MockRandomRepository(RandomRepository):

  def __init__(self):
    self.spy_one_to_three = 0

  def one_to_three(self):
    self.spy_one_to_three += 1
    return 0


class TestCalculatorService(TestCase):


    def test_case1(self):
        random_repo = MockRandomRepository()
        cal_srv = CalculatorService(random_repo)
        actual = cal_srv.add(1, 2)
        expect = 3

        actual_callcount = random_repo.spy_one_to_three
        expect_callcount = 0

        self.assertEqual(actual_callcount, expect_callcount, "should not be call")
        self.assertEqual(actual, expect, "should be return 3")


    def test_case2(self):

        random_repo = MockRandomRepository()
        cal_srv = CalculatorService(random_repo)
        actual = cal_srv.random_with_constant(-1)
        expect = -1

        actual_callcount = random_repo.spy_one_to_three
        expect_callcount = 1

        self.assertEqual(actual_callcount, expect_callcount, "should be call once")
        self.assertEqual(actual_result, expect_result, "should be equal randint_mock + constant input")

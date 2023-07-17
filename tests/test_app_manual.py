from unittest import TestCase

from app import Example, random


class TestExample(TestCase):
    def test_case1(self):
        example = Example()
        actual = example.add(1, 2)
        expect = 3
        self.assertEqual(actual, expect, "should be return 3")

    def test_case2(self):
        example = Example()
        actual = example.add(5, 1000)
        expect = 1005
        self.assertEqual(actual, expect, "should be return 1005")

    def test_case3(self):
        class SpyExample(Example):
            def __init__(self):
                self.callcount = 0

            def random_with_constant(self, constant):
                self.callcount = self.callcount + 1
                return super().random_with_constant(constant)

        def stub_random_randint(a, b):
            return 100

        random.randint = stub_random_randint

        example = SpyExample()
        actual_result = example.random_with_constant(-1)
        expect_result = 99

        actual_callcount = example.callcount
        expect_callcount = 1

        self.assertEqual(actual_callcount, expect_callcount, "should be call once")
        self.assertEqual(
            actual_result,
            expect_result,
            "should be equal randint_mock + constant input",
        )

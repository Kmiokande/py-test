import unittest


def fun(a, b):
    return a + b


class MyTest(unittest.TestCase):
    def test_sum_positive_numbers(self):
        self.assertEqual(fun(1, 1), 2)

    @unittest.skip("not working")
    def test_letter_sum(self):
        with self.assertRaises(ValueError) as error:
            fun('a', 'b')
            self.assertSetEqual(error.msg, "Only numbers are allowed!")


if __name__ == '__main__':
    unittest.main()

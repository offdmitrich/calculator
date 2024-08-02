import unittest
from calculator import add, subtract, multiply, divide

class TestMain(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 2), 7)
        self.assertEqual(add(-4, 5), 1)
        self.assertEqual(add(-3, -2), -5)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(3, 3), 0)
        self.assertEqual(subtract(1, 0), 1)
        self.assertEqual(subtract(-2, -5), 3)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        self.assertEqual(multiply(5, 2), 10)
        self.assertEqual(multiply(-1, 52), -52)
        self.assertEqual(multiply(-1, -10), 10)
        self.assertEqual(multiply(1, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(20, 2), 10)
        self.assertEqual(divide(5, 5), 1)
        self.assertEqual(divide(-10, -2), 5)
        self.assertEqual(divide(52, 2), 26)
        with self.assertRaises(ValueError):
            divide(52, 0)


if __name__ == "__main__":
    unittest.main
import unittest
import hello

class TestHello(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello.hello(), "Hello, world!")

    def test_sin(self):
        self.assertEqual(hello.sin(0), 0)
        self.assertEqual(hello.sin(1), 0.8414709848078965)
        self.assertEqual(hello.sin(2), 0.9092974268256817)

    def test_cos(self):
        self.assertEqual(hello.cos(0), 1)
        self.assertEqual(hello.cos(1), 0.5403023058681398)
        self.assertEqual(hello.cos(2), -0.4161468365471424)
    def test_tan(self):
        self.assertEqual(hello.tan(0), 0)
        self.assertEqual(hello.tan(1), 1.5574077246549023)
        self.assertEqual(hello.tan(2), -2.185039863261519)
    def test_cot(self):
        self.assertEqual(hello.cot(0), float("inf"))
        self.assertEqual(hello.cot(1), 0.6420926159343306)
        self.assertEqual(hello.cot(2), -0.4576575543602854)
    def test_add(self):
        self.assertEqual(hello.add(1, 2), 3)
        self.assertEqual(hello.add(-1, 1), 0)
        self.assertEqual(hello.add(-1, -1), -2)
    def test_sub(self):
        self.assertEqual(hello.sub(2, 1), 1)
        self.assertEqual(hello.sub(1, 2), -1)
        self.assertEqual(hello.sub(-1, -1), 0)
    def test_mul(self):
        self.assertEqual(hello.mul(2, 3), 6)
        self.assertEqual(hello.mul(-1, 1), -1)
        self.assertEqual(hello.mul(-1, -1), 1)
    def test_div(self):
        self.assertEqual(hello.div(6, 3), 2)
        self.assertEqual(hello.div(-6, 3), -2)
        self.assertEqual(hello.div(-6, -3), 2)
        with self.assertRaises(ValueError):
            hello.div(1, 0)
    def test_sqrt(self):
        self.assertEqual(hello.sqrt(4), 2)
        self.assertEqual(hello.sqrt(9), 3)
        with self.assertRaises(ValueError):
            hello.sqrt(-1)
    def test_power(self):
        self.assertEqual(hello.power(2, 3), 8)
        self.assertEqual(hello.power(3, 2), 9)
        self.assertEqual(hello.power(2, -1), 0.5)
    def test_log(self):
        self.assertEqual(hello.log(1), 0)
        self.assertEqual(hello.log(2.718281828459045), 1)
        with self.assertRaises(ValueError):
            hello.log(-1)
    def test_exp(self):
        self.assertEqual(hello.exp(0), 1)
        self.assertEqual(hello.exp(1), 2.718281828459045)
        self.assertEqual(hello.exp(2), 7.3890560989306495)

if __name__ == "__main__":
    unittest.main()

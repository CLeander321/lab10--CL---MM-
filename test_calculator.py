class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 3), 5)
    def test_divide_by_zero(self):
        self.assert(divide(15, 5), 3)
    def test_log_invalid_base(self):
        self.assertRaises(ValueError, logarithm, 0, 0)
    def test_logarithm(self):
        self.assertEqual(math.log10(1000), 3)
        self.assertEqual(math.log(math.e), 1)
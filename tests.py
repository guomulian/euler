import unittest
import euler

class EratosthenesTest(unittest.TestCase):
    def test_small_values(self):
        self.assertEqual(euler.eratosthenes(50), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47])
        self.assertEqual(euler.eratosthenes(10), [2,3,5,7])
        self.assertEqual(euler.eratosthenes(3), [2])

    def test_less_than_two(self):
        self.assertEqual(euler.eratosthenes(1), [])
        self.assertEqual(euler.eratosthenes(0), [])
        self.assertEqual(euler.eratosthenes(-1), [])

    def test_noninteger(self):
        self.assertRaises(TypeError, euler.eratosthenes, 5.5)
        self.assertRaises(TypeError, euler.eratosthenes, 5.)

class UniquePrimeFactorsTest(unittest.TestCase):
    def test_small_values(self):
        self.assertEqual(euler.unique_prime_factors(50), [2,5])
        self.assertEqual(euler.unique_prime_factors(10), [2,5])
        self.assertEqual(euler.unique_prime_factors(3), [3])

    def test_less_than_two(self):
        self.assertEqual(euler.unique_prime_factors(1), [])
        self.assertEqual(euler.unique_prime_factors(0), [])
        self.assertEqual(euler.unique_prime_factors(-1), [])
        self.assertEqual(euler.unique_prime_factors(-10), [])

    def test_noninteger(self):
        self.assertRaises(TypeError, euler.unique_prime_factors, 5.5)
        self.assertRaises(TypeError, euler.unique_prime_factors, 5.)

class PrimeFactorsTest(unittest.TestCase):
    def test_small_values(self):
        self.assertEqual(euler.prime_factors(50), [2,5,5])
        self.assertEqual(euler.prime_factors(10), [2,5])
        self.assertEqual(euler.prime_factors(3), [3])

    def test_less_than_two(self):
        self.assertEqual(euler.prime_factors(1), [])
        self.assertEqual(euler.prime_factors(0), [])
        self.assertEqual(euler.prime_factors(-1), [])
        self.assertEqual(euler.prime_factors(-10), [])

    def test_noninteger(self):
        self.assertRaises(TypeError, euler.prime_factors, 5.5)
        self.assertRaises(TypeError, euler.prime_factors, 5.)

class TrialDivisionTest(unittest.TestCase):
    def test_small_values(self):
        self.assertFalse(euler.trial_division(50))
        self.assertFalse(euler.trial_division(10))
        self.assertTrue(euler.trial_division(3))

    def test_less_than_two(self):
        self.assertRaises(ValueError, euler.trial_division, 1)
        self.assertRaises(ValueError, euler.trial_division, 0)
        self.assertRaises(ValueError, euler.trial_division, -1)

class MillerRabinTest(unittest.TestCase):
    def test_small_values(self):
        self.assertFalse(euler.miller_rabin(50))
        self.assertFalse(euler.miller_rabin(10))
        self.assertTrue(euler.miller_rabin(3))

    def test_less_than_two(self):
        self.assertRaises(ValueError, euler.miller_rabin, 1)
        self.assertRaises(ValueError, euler.miller_rabin, 0)
        self.assertRaises(ValueError, euler.miller_rabin, -1)

class EulerTotientTest(unittest.TestCase):
    def test_small_values(self):
        self.assertEqual(euler.euler_totient(9), 6)
        self.assertEqual(euler.euler_totient(36), 12)
        self.assertEqual(euler.euler_totient(1), 1)

    def test_less_than_one(self):
        self.assertRaises(ValueError, euler.euler_totient, 0)
        self.assertRaises(ValueError, euler.euler_totient, -1)

if __name__ == '__main__':
    unittest.main()
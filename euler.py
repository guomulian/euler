"""A collection of functions (that may be) helpful in solving Project Euler (https://projecteuler.net/) problems."""

import random
import fractions

# LISTS OF PRIMES
def eratosthenes(n):
    """Return a list of the prime numbers less than a given limit via Eratosthenes' Sieve."""

    if n < 2:
        return []

    else:  
        sqn = int(n**0.5)
        sieve = [True]*n

        for i in xrange(2, sqn+1):
            if sieve[i] == True:
                for j in xrange(2*i, n, i):
                    sieve[j] = False

            else:
                pass

        return [k for k in xrange(2, n) if sieve[k] == True]

def unique_prime_factors(n):
    """Returns a list of the unique prime factors of a number using Eratosthenes' Sieve and trial division."""

    primes = eratosthenes(n + 1)

    return filter(lambda factor: n % factor == 0, primes)


def prime_factors(n):
    """Returns a list of the prime factors of a number using Eratosthenes' Sieve and trial division."""

    upfs = unique_prime_factors(n)
    prime_factors = []

    for f in upfs:
        while n % f == 0:
            n /= f
            prime_factors.append(f)

    return prime_factors


# PRIMALITY TESTS
def trial_division(n):
    if n < 2:
        raise ValueError("Number must be at least 2.")

    else:
        sqn = int(n**0.5)

        for i in xrange(2, sqn):
            if n % i == 0:
                return False

            else:
                pass

        else:
            return True

def miller_rabin(n, k=40, seed=None):
    """
    Returns whether a given number is a likely prime via the Miller-Rabin algorithm.
        A return value of True with Miller-Rabin only means that n is likely a prime.
        A return value of False means that n is not prime.
    """

    if n < 2:
        raise ValueError("Number must be at least 2.")

    elif n == 2 or n == 3:
        return True

    elif n % 2 == 0:
        return False

    else:
        random.seed(seed)

        r, d = 0, n - 1

        while d % 2 == 0:
            r += 1
            d /= 2

        for _ in xrange(k):
            a = random.randrange(2, n - 1)
            x = pow(a, d, n)

            if x == 1 or x == n - 1:
                continue

            else:
                for _ in xrange(r - 1):
                    x = pow(x, 2, n)

                    if x == 1:
                        return False

                    elif x == n - 1:
                        break

                else:
                    return False

        else:
            return True

# OTHER
def euler_totient(n):
    if n < 1:
        raise ValueError("Number must be at least one.")

    else:
        phi = 0

        for k in xrange(1, n + 1):
            if fractions.gcd(n, k) == 1:
                phi += 1

            else:
                pass

        return phi
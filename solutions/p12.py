# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

### Notes
## Now that I am getting a bit farther into them I will record some thought process here when needed
## Find the first triangle number with n divisors
# Biggest thing is computing for a number n, how many divisors does it have? Generating triangle #s is trivial. I could just check every number j < n and see if n % j == 0
# But i want to do better.. after some thinking I think I figured it out. What if I find the prime factorization of n and use that? more specifically: n = p1 * p2 * p3 * ..., where pi is prime. 
# BUT the prime factors alone can't tell me. ex: 9 is not a prime factor of 18 but it certainly is a divisor. So to be more specific I should specify it like this
# n = p1^a * p2^b * p3^c * ..., 
# then each divisor is some combination of these primes (say 9 = 3*3 or 6 = 3*2). So there are (a+1)(b+1)(c+1)(...) divisors! Lets hope this works

import math

def count_divisors(n: int) -> int:
    max_value = math.sqrt(n)
    prime_factors = {}
    i = 2
    while i <= max_value:
        while n % i == 0:
            prime_factors[i] = prime_factors.get(i, 0) + 1 # I had a long way to do this but Claude came up with this clean version
            n //= i
        i += 1
        
    if n > 1:
        prime_factors[n] = 1

    divisor_count = 1
    for exponent in prime_factors.values():
        divisor_count *= (exponent + 1)
    
    return divisor_count

if __name__ == "__main__":
    # config
    num_divisors = 500
    
    i = 1
    triangle_number = 1
    while True:
        i += 1
        triangle_number += i
        divisors = count_divisors(triangle_number)
        if divisors > num_divisors:
            break
    
    print(triangle_number)
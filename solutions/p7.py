# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

# code courtesy of github copilot : ). too lazy to write my own sieve tonight
def sieve_of_eratosthenes(limit):
    primes = []
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for start in range(2, limit + 1):
        if sieve[start]:
            primes.append(start)
            for multiple in range(start * start, limit + 1, start):
                sieve[multiple] = False

    return primes

def nth_prime(n):
    if n < 1:
        return None

    limit = 15  # Initial guess for the upper limit
    primes = []

    while len(primes) < n:
        primes = sieve_of_eratosthenes(limit)
        limit *= 2  # Increase the limit exponentially

    return primes[n - 1]

if __name__ == "__main__":
    n = 10001  # Change this value to find a different nth prime number
    prime = nth_prime(n)
    print(f"The {n}th prime number is: {prime}")
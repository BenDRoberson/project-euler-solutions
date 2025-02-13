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

if __name__ == "__main__":
    limit = 2000000
    primes = sieve_of_eratosthenes(limit)
    print(sum(primes))
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

# note: this is my first attempt - it will work except for it can't fit the first function in memory for 600851475143
# see p3b.py where I try and do it smarter :)

def list_of_primes_below_int(max_number: int) -> list[int]:
    primeList = list(range(2, max_number + 1))
    index = 0
    while index <= len(primeList): # prime to sieve
        i = index + 1
        while i < len(primeList): # remove all values divisible by this prime (up to the end of the list)
            if primeList[i] % primeList[index] == 0:
                    primeList.remove(primeList[i])
            i = i + 1
        index += 1

    return primeList

def max_prime_factor(primeList: list[int]) -> int:
    return(max(primeList))

if __name__ == "__main__":
    print(max_prime_factor(list_of_primes_below_int(600851475143)))
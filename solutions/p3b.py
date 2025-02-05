# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///


# the main difference here is we don't need every prime factor, just the biggest. so start by dividing out small ones!
def max_prime_factor(n: int) -> int:
    max_prime = 2

    for i in range(3, int(n**0.5) + 1, 2): # check every 2nd number (even number cant be prime factor for this input, )
        while n % i == 0:
            max_prime = i
            n //= i
    
    return max_prime

if __name__ == "__main__":
    print(f"max prime factor for 600851475143 is: {max_prime_factor(600851475143)}")
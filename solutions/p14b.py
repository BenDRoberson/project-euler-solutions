# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

### Notes
## Collatz
# if n is even n/2
# if n is odd 3n+1
## Not thrilled with this one I got it pretty easily but feels very.. slow
## Lets start with a fun one I want to time
## oh also fixed that dumbass code with the flag when i could just do n > 1

def calculate_collatz_chain(n: int) -> int:
    chain_length = 0
    while n > 1:
        if n & 1 == 0:
            n >>=1
        else:
            n = (3*n)+1
        chain_length += 1
    return chain_length

if __name__ == "__main__":
    largest_chain = {
        "n": -1,
        "chain_length": -1
    }

    for i in range(1, 1000000):
        if i % 100000 == 0:
            print(f"done {i}")
        new_chain_length = calculate_collatz_chain(i)

        if new_chain_length > largest_chain["chain_length"]:
            largest_chain["n"] = i
            largest_chain["chain_length"] = new_chain_length
    
    print(f"largest chain is {largest_chain["chain_length"]} at the number {largest_chain["n"]}")

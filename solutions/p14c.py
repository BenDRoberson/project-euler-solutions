# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

### Notes
## Collatz
# if n is even n/2
# if n is odd 3n+1
## Now lets do the most obvious speedup - don't recalculate every time
## the collatz sequences hit the same numbers a lot! so save then and look them up, don't keep doing long chains over and over
### file a: 10.24 seconds
### file b: 9.07 seconds (very reasonable 10% improvement from just 2 bit operations there)
### file c: 0.94 seconds turns out not rerunning the same numbers is good!

def calculate_collatz_chain_memoized(n: int, memo: dict) -> int:
    if n in memo:
        return memo[n]
    
    # Base case
    if n == 1:
        memo[n] = 1
        return 1
    
    if n & 1 == 0:
        next_n = n >> 1
    else:
        next_n = 3 * n + 1
    
    # Calculate chain length and memoize
    memo[n] = 1 + calculate_collatz_chain_memoized(next_n, memo)
    return memo[n]

if __name__ == "__main__":
    largest_chain = {
        "n": -1,
        "chain_length": -1
    }
    
    # Initialize memoization dictionary with base case
    memo = {1: 1}
    
    for i in range(1, 1000000):
        if i % 100000 == 0:
            print(f"done {i}")
        
        new_chain_length = calculate_collatz_chain_memoized(i, memo)
        
        if new_chain_length > largest_chain["chain_length"]:
            largest_chain["n"] = i
            largest_chain["chain_length"] = new_chain_length
    
    print(f"largest chain is {largest_chain['chain_length']} at the number {largest_chain['n']}")

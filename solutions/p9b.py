# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

import math
import time

def are_coprime(a: int, b: int) -> bool:
    while b:
        a, b = b, a % b
    return a == 1

def find_pythagorean_triples_euclid(total_sum: int) -> list[int]:
    # The below formulas generate a "primitive" (or base) pythagorean triples if:
    # 1) m, n are coprime (AKA their smallest common denominator is equal to 1)
    # 2) one of m, n is even and the other is odd (two odd numbers can be coprime)
    # a = m^2 - n^2
    # b = 2*m*n
    # c = m^2 + n^2
    # a + b + c = n => a + b + b^2 + c^2 = n

    max_m = int(math.sqrt(total_sum/2))
    
    for m in range(2, max_m + 1):
        for n in range(1, m):
            # Check if m,n are coprime and even/odd
            if are_coprime(m, n) and (m - n) % 2 == 1:
                a = m*m - n*n
                b = 2*m*n
                c = m*m + n*n
                primitive_sum = a + b + c
                
                if total_sum % primitive_sum == 0:
                    # Scale the triple such that we reach the total_sum
                    k = total_sum // primitive_sum
                    return [k*a, k*b, k*c]
    
    return None

if __name__ == "__main__":
    start_time = time.time()
    answer = find_pythagorean_triples_euclid(total_sum = 1000)
    end_time = time.time()
    print(answer)
    print(f"product is {answer[0]*answer[1]*answer[2]}")
    print(f"time elapsed: {end_time - start_time:.6f} seconds") # 0.000016 seconds vs 0.25406 seconds for p9a.py. quick little 99.9% improvement - thanks Euclid
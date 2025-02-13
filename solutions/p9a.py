# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

import math
import time

def find_pythagorean_triples(total_sum: int) -> list[int]:
    max_value = total_sum // 2 # can i improve this? what's the best lower bound. Maybe i can do this using some tricks for triples instead
    c_squared = [i**2 for i in range(1, max_value + 1)]
    for a in range(0, max_value):
        for b in range(a, max_value):
            if (a**2 + b**2) in c_squared:
                c = int(math.sqrt(a**2 + b**2))
                if a + b + c == 1000:
                    return [a, b, c]
    return None

if __name__ == "__main__":
    start_time = time.time()
    answer = find_pythagorean_triples(total_sum = 1000)
    end_time = time.time()
    print(answer)
    print(f"product is {answer[0]*answer[1]*answer[2]}")
    print(f"time elapsed: {round(end_time - start_time, 5)} seconds")
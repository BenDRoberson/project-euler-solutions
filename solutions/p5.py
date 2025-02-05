# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

def check_evenly_divisble_up_to_n(num: int, n: int) -> bool:
    for i in range(n, 2, -1):
        if num % i != 0:
            return False
    return True

if __name__ == "__main__":
    smallest_number = None
    max_divisor = 20

    # using a trick that the solution must be divisable by the largest divisor (duh). important since this lets us only check every nth number
    i = max_divisor
    while True:
        if check_evenly_divisble_up_to_n(i, max_divisor):
            smallest_number = i
            break
        i += max_divisor

    print(f"the smallest number evenly divisible by all of the numbers from 1 to {max_divisor} is {smallest_number}")
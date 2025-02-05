# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1] # gotta love python

if __name__ == "__main__":
    biggest_palindrome = 0
    for i in range(0, 1000):
        for j in range(0, 1000):
            k = i * j
            if is_palindrome(k) and k > biggest_palindrome:
                biggest_palindrome = k

    print(f"largest palinedrome that is the product of two three-digit numbers is: {biggest_palindrome}")
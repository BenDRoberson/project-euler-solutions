# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

if __name__ == "__main__":
    square_sum = 0
    sum_square = 0

    for i in range(1, 101):
        square_sum += i
        sum_square += i**2

    square_sum = (square_sum)**2

    print(f"For the first 100 natural numbers: (square of the sum) - (sum of the squares) -> {square_sum} - {sum_square} = {square_sum - sum_square}")
# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///


previous_number = 1
current_number = 2
sum = current_number

while current_number <= 4000000:
    next_number = previous_number + current_number
    previous_number = current_number

    if next_number % 2 == 0 and current_number <= 4000000:
        sum += next_number

    current_number = next_number

print(sum)
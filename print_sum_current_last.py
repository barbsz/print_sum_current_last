def print_sums():
    previous_number = 0
    for i in range(1, 11):
        sum = previous_number + i
        print(f"Current Number {i} Previous Number {previous_number} Sum: {sum}")
        previous_number = i

print_sums()

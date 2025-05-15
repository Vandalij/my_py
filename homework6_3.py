number = int(input("Enter your number: "))
if number <= 9:
    print(f"Result: {number}")
else:
    while number > 9:
        digits = [int(digit) for digit in str(number)]
        num_str = 1

        for digit in digits:
            num_str *= digit
        number = num_str
    print(f"Result: {number}")

#Loop for user input

while True:
    start = int(input("Enter the starting number (0 to terminate): "))

    if start == 0:
        print("Program terminated.")
        break
    elif start < 0:
        print("Enter a non-negative number.")
        continue

    end = int(input("Enter the ending number: "))

    if end < start:
        print("Enter a number greater than the starting number.")
        continue

    print(f"Prime numbers between {start} and {end}:")

#Computation for prime number

    for num in range(start, end + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
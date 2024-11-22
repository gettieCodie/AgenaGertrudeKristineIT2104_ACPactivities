def perfectNum(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

while True:
    num = input("Enter a number: ")

    if num.isdigit() and int(num) > 0:
        number = int(num)
        print(f"{number} is {'a perfect' if perfectNum(number) else 'not a perfect'} number.")
        print()
    else:
        print("Invalid input. Please enter a valid positive integer.")
        print()

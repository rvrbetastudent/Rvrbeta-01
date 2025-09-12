try:
    n = int(input("Enter number: "))
    print(n, end=' ')
    while n != 1:
        if n == 0:
            print("is not allowed. Please enter a different number.")
            break
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        print(n, end=' ')
    print()
except ValueError:
    print("Please enter a valid integer.")
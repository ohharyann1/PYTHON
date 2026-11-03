def armstrong(n, digits):
    if n == 0:
        return 0
    return (n % 10) ** digits + armstrong(n // 10, digits)

num = int(input("Enter a number: "))

digits = len(str(num))

if armstrong(num, digits) == num:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
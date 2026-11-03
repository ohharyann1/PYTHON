def armstrong(n, original):
    if n == 0:
        return 0
    
    digit = n % 10
    return digit ** 3 + armstrong(n // 10, original)

n = int(input("Enter number: "))

if armstrong(n, n) == n:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
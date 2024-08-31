def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
    
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print(f"The GCD of two numbers is {gcd(num1, num2)}")

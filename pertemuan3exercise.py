percentage = float(input("Enter your percentage: "))
if percentage >= 90:
    print("Excellent performance")
elif percentage >= 80:
    print("Very Good performance")
elif percentage >= 70:
    print("Good performance")
elif percentage >= 60:
    print("Average performance")
else:
    print("Not good")
    #number 2
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest = max(num1, num2, num3)  
print(f"The largest number is: {largest}")

#number3
def fibonacci(n):
    a,b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
n = int(input("Masukkan deret fibonacci: "))
fibonacci(n)

#number 4
n = int(input("Enter the value of n: "))
def print_odd_numbers(n):
    odd_numbers = [i for i in range(1, n+1) if i % 2 != 0]
    return odd_numbers
print("Odd numbers up to", n, "are:", print_odd_numbers(n))

#nomer 5
def number_pattern(n):
    for i in range(1, n + 1):
        print((str(i) + ' ') * i)
n = int(input('Masukkan nilai n untuk pola segitiga: '))
number_pattern(n)




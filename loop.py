#1. Write a program in Python to display the first 10 natural numbers.
for i in range(1,11,1):
    print(i)

#2. Write a Python program to compute the sum of the first 10 natural numbers.
sum = 0
for i in range(1, 11):
    sum += i

# Print the sum
print("Sum of the first 10 natural numbers:", sum)

#3.Write a program in Python to display n terms of natural numbers and their sum.
n = int(input("Enter the value of n: "))

#Display the first n terms of natural numbers and compute their sum'
sum = 0
for i in range(1, n+1):
    print(i)
    sum += i

# Print the sum of the natural numbers
print("Sum of the first", n, "natural numbers:", sum)

#4.Write a program in python to read 10 numbers from the keyboard and find their sum and average.

# Read 10 numbers from the keyboard
numbers = []
for i in range(10):
    num = float(input("Enter a number: "))
    numbers.append(num)

# Calculate the sum of the numbers
sum = sum(numbers)

# Calculate the average of the numbers
average = sum / len(numbers)

# Print the sum and average
print("Sum:", sum)
print("Average:", average)

#5.Write a program in python to display the cube of the number up to an integer.
# Accept an integer from the user
n = int(input("Enter an integer: "))

# Display the cube of numbers up to n
for i in range(1, n+1):
    cube = i ** 3
    print(f"The cube of {i} is {cube}")

#6.Write a program in Python to display the multiplication table for a given integer.
# Accept an integer from the user
num = int(input("Enter an integer: "))

# Display the multiplication table for the given integer
print(f"Multiplication Table for {num}:")
for i in range(1, 11):
    product = num * i
    print(f"{num} x {i} = {product}")


#7.Write a program in Python to display the multiplier table vertically from 1 to n.
# Accept an integer from the user
n = int(input("Enter an integer: "))

# Display the multiplier table vertically from 1 to n
for i in range(1, n+1):
    print(f"Multiplier table for {i}:")
    for j in range(1, 11):
        product = i * j
        print(f"{i} x {j} = {product}")
    print()  # Print an empty line after each multiplier table

#8.Write a python program to display the n terms of odd natural numbers and their sum.
n = int(input("Enter the value of n: "))

# Display the first n terms of odd natural numbers and compute their sum
sum = 0
count = 0
odd_number = 1

print(f"The first {n} odd natural numbers are:")
while count < n:
    print(odd_number)
    sum += odd_number
    odd_number += 2
    count += 1

# Print the sum of the odd natural numbers
print("Sum of the first", n, "odd natural numbers:", sum)

#9.Write a python program to find the 'Perfect' numbers within a given number of ranges.
#Test Data :
#Input the starting range or number : 1
#Input the ending range of number : 50

# Accept the starting and ending range from the user
start_range = int(input("Input the starting range or number: "))
end_range = int(input("Input the ending range of number: "))

# Function to check if a number is perfect
def is_perfect(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    return sum(divisors) == number

# Find and display the perfect numbers within the given range
print("Perfect numbers within the given range:")
for num in range(start_range, end_range+1):
    if is_perfect(num):
        print(num)
#10.Write a python program to determine whether a given number is prime or not.
#Test Data :
#Input a number: 13
def IsPrime(n):
  if n<2:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True      
print(IsPrime(13)) 







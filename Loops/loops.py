# loops.py  -  loops in python -  by Don Cross - 2021-06-20

# This program demonstrates the use of loops in Python.
# The program prints the first 10 Fibonacci numbers.

def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        a, b = b, a + b
        
fibonacci(10)

# end of file
        
count = 1
while count <= 499:
    print("python is fun!", count)
    count += 1
    
    # while loop with break statement  
    
    
    
 
    
    
i = 5
while i>=1:
    print(i)
    i -= 1  
print("loop endede")


i=1
while i <=100:
    print(i)
    i=i+1
    
    
a = 100
while a >= 1:
    print(a)
    a = a - 1
    
 
n = int(input("Enter a number: "))
j = 1
while j <= 10:
    print(n*j)
    j += 1
    
    
nums = [1, 11, 21, 32, 41, 51, 61, 71, 81, 91]
subjects = ["python", "java", "c++", "c", "ruby", "javascript", "html", "css", "php", "sql"]

indx = 0
# travers the list using while loop and print the elements of the list.
while indx < len(subjects):
    print(subjects[indx]) # print the element at the current index
    indx += 1
    
nums = [1, 11, 21, 32, 41, 51, 61, 71, 81, 91]

x = 41

indx = 0
while indx < len(nums):
    if nums[indx] == x:
        print("Element found at index", indx)
    indx += 1    
    



    

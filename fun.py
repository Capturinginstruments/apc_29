# # 1.	Write a function factorial(n) that accepts an integer and returns its factorial.
# # def a(n):
# #     fact=1
# #     for i in range (1,n+1):
# #         fact=fact*i
# #     print(fact)
# # p=int(input("Enter A number you want to remove factorial of: "))
# # a(p)
# # # 2.	Write a function check_even_odd(n) that determines whether a given number is even or odd.
# # def even(b):
# #     if b%2==0:
# #         print("even")
# #     else:
# #         print("odd")
# # even(1203)
# # #3.Define a function that accepts two numbers and returns the greater number.
# # def b(m,n):
# #     if m>n:
# #         print("m is greater",m)
# #     else:
# #         print("n is greater",n)
# # b(1872,1782)
# # # 4.	Create a function simple_interest(p, r, t) to calculate simple interest.
# # def simple_interest(p, r, t):
# #     a=(p*r*t)/100
# #     print(a)
# # simple_interest(10,12,35)
# # # 5.	Write a function is_prime(n) that returns True if a number is prime; otherwise, returns False.
# # def is_prime(n):
# #     count =0
# #     for i in range (1,n+1):
# #         if n%i==0:
# #             count= count +1
# #     if count==2:
# #         print("prime")
# #     else:
# #         print("not prime ")
# # is_prime(20)
# # # 6.	Define a function to calculate the area of a circle using its radius.
# # def cr(n):
# #     c=3.14*n*n
# #     print(c,"is the radius")
# # cr(10)
#     # 7.	Write a function that accepts n and returns the sum of the first n natural numbers.
# # def add(n):
# #     s=0
# #     for i in range(1,n+1):
# #         s=s+i
# #     print(s)
# # add(10)
# # 8.	Create a function power(base, exponent) to calculate the value of base raised to exponent.
# # def power(base, exponent):
# #     a=base**exponent
# #     print(a)
# # power(1,3)
# # # 9.	Write a function that accepts a list of numbers and returns the largest element without using the built-in max() function.
# # def largest(numbers):
# #     largest = numbers[0]
# #     for num in numbers:
# #         if num > largest:
# #             largest = num
# #     print(largest)
# # numbers = [10, 25, 7, 40, 65]
# # largest(numbers)
# # # 10.	Define a function that accepts a string and returns the number of vowels present in it.
# # def count_vowels(string):
# #     count = 0
# #     for ch in string:
# #         if ch in "aeiouAEIOU":
# #             count += 1
# #     print (count)
# # count_vowels("hellloo")
# # # 11.	Write a function that accepts a string and returns its reverse.
# # def rev(s):
# #     print(s[::-1])
# # rev("mummyyy")
# # # 12.	Create a function that checks whether a given string or number is a palindrome.
# # def pal(n):
# #     if n==n[::-1]:
# #         print("palindrome")
# #     else:
# #         print("no")
# # pal("131")
# # # 13.	Write a function that accepts a list of numbers and returns their average.
# # def avg(n):
# #     s=0
# #     for i in n:
# #         s=s+i
# #     print(s/len(n))
# # p=[10,9,11]
# # avg(p)
# # 14.	Define a function that accepts a list and an element and returns the number of times that element occurs.
# # 14. Count occurrence of an element
# def count(a, x):
#     c = 0
#     for i in a:
#         if i == x:
#             c += 1
#     return c
# p = [10, 101, 10, 10, 123, 12, 12]
# print("Count:", count(p, 10))
# # 15.	Write a function that accepts a list and returns a new list containing only unique elements.
# def unique(a):
#     b = []
#     for i in a:
#         if i not in b:
#             b.append(i)
#     print(b)
# print("Unique:", unique(p))
# # 16.	Create a function to find the second-largest number in a list.
# def second_largest(a):
#     a = list(set(a))
#     a.sort()
#     return a[-2]
# print("Second largest:", second_largest(p))
# # 17.	Write a function that accepts n and returns the first n Fibonacci numbers.
# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         print(a, end=" ")
#         a, b = b, a + b
# print("Fibonacci:")
# fibonacci(7)
# # 18.	Create a function that accepts marks in five subjects and returns the student's percentage and grade.
# def marks(m1, m2, m3, m4, m5):
#     per = (m1+m2+m3+m4+m5) / 5
#     if per >= 90:
#         grade = "A"
#     elif per >= 75:
#         grade = "B"
#     elif per >= 60:
#         grade = "C"
#     else:
#         grade = "D"
#     print("Percentage:", per)
#     print("Grade:", grade)
# marks(80, 85, 75, 90, 85)
# # 19.	Write a function that accepts the number of units consumed and calculates the electricity bill according to predefined slabs.
# def bill(unit):
#     if unit <= 100:
#         b = unit * 5
#     elif unit <= 200:
#         b = 100*5 + (unit-100)*7
#     else:
#         b = 100*5 + 100*7 + (unit-200)*10
#     print (b)
# print("Electricity Bill:", bill(250))

# # # 20.	Write a function that accepts basic salary and calculates gross salary after adding HRA and DA.
# def salary(basic):
#     hra = basic * 0.20
#     da = basic * 0.10
#     return basic + hra + da
# print("Gross Salary:", salary(20000))
# 21.	Create a function that accepts item prices and quantities and returns the total bill after applying a discount.

# 22.	Write a function that accepts a list of numbers and returns the minimum, maximum, sum, and average.
def fun(n):
    print(max(n))
    print(min(n))
    s=0
    for i in n:
        s=s+i
    a=s/len(n)
    print(s,"\n",a)
fun([12,12,12,13])
# 23. Student Records

def student(name, roll, marks):
    total = sum(marks)
    per = total / 5

    if per >= 75:
        grade = "A"
    elif per >= 60:
        grade = "B"
    elif per >= 50:
        grade = "C"
    else:
        grade = "D"

    return total, per, grade

students = [
    ("Amit", 1, [80, 75, 90, 85, 70]),
    ("Rahul", 2, [60, 65, 70, 55, 60]),
    ("Neha", 3, [90, 95, 85, 92, 88])
]

totals = []
for s in students:
    t, p, g = student(s[0], s[1], s[2])
    totals.append(t)
    print(s[0], "Total:", t, "Percentage:", p, "Grade:", g)

print("Class Average:", sum(totals)/(len(totals)*5))
print("Highest Scorer:", students[totals.index(max(totals))][0])
print("Lowest Scorer:", students[totals.index(min(totals))][0])
# 24. Bank Account
balance = 1000
history = []
def deposit(amount):
    global balance
    balance += amount
    history.append("Deposited " + str(amount))
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        history.append("Withdrawn " + str(amount))
    else:
        print("Insufficient balance")
def enquiry():
    print("Balance:", balance)
def transactions():
    print("History:", history)
deposit(500)
withdraw(300)
enquiry()
transactions()
# 25. Library Management
books = {
    "Python": True,
    "Java": True,
    "C++": False
}
def add_book(book):
    books[book] = True
def issue_book(book):
    if book in books and books[book]:
        books[book] = False
        print("Book issued")
    else:
        print("Book not available")
def return_book(book):
    books[book] = True
def search_book(book):
    print("Found" if book in books else "Not found")
def available_books():
    for book in books:
        if books[book]:
            print(book)
add_book("SQL")
issue_book("Python")
return_book("C++")
search_book("Java")
available_books()
# 26. Electricity Bill
def electricity_bill(units):
    if units <= 100:
        bill = units * 5
    elif units <= 200:
        bill = 100*5 + (units-100)*7
    else:
        bill = 100*5 + 100*7 + (units-200)*10
    fixed = 50
    tax = bill * 0.05
    discount = bill * 0.10 if units < 100 else 0
    return bill + fixed + tax - discount
print("Electricity Bill:", electricity_bill(250))
# 27. Hospital Bill
def consultation(x):
    return x
def laboratory(x):
    return x
def medicine(x):
    return x
def room(x):
    return x
def final_bill(category, c, l, m, r):
    total = c + l + m + r
    if category == "senior":
        total = total * 0.90

    return total

print("Hospital Bill:",
      final_bill("senior", consultation(500),
                 laboratory(1000), medicine(1500), room(2000)))


# 28. Shopping Invoice

def subtotal(products):
    total = 0
    for price, qty in products:
        total += price * qty
    return total

def coupon(total):
    return total * 0.10

def gst(total):
    return total * 0.18

def invoice(products):
    sub = subtotal(products)
    discount = coupon(sub)
    tax = gst(sub - discount)
    return sub - discount + tax

products = [(100, 2), (500, 1), (200, 3)]
print("Final Invoice:", invoice(products))


# 29. Recursive Binary Search

def binary_search(a, x, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if a[mid] == x:
        return mid
    elif x < a[mid]:
        return binary_search(a, x, low, mid-1)
    else:
        return binary_search(a, x, mid+1, high)

a = [10, 20, 30, 40, 50]
print("Position:", binary_search(a, 30, 0, len(a)-1))


# 30. Decimal to Binary using Recursion

def binary(n):
    if n == 0:
        return ""
    return binary(n//2) + str(n%2)

print("Binary:", binary(10))


# 31. Palindrome using Recursion

def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

print("Palindrome:", palindrome("madam"))


# 32. Functions as Arguments

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def calculate(a, b, operation):
    return operation(a, b)

print(calculate(10, 5, add))
print(calculate(10, 5, subtract))
print(calculate(10, 5, multiply))
print(calculate(10, 5, divide))
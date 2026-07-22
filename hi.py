#1
a=int(input("Enter a number you want to check wheter zero or non zero :"))
if a==0:
    print('zero')
else:
    print('non-zero')

#2
b=int(input('num1'))
c=int(input('num2'))
if b>c :
    print('num1 is largest')
else:
    print('num2 is largest')

#3
k=int(input("enter the number :"))
if k<=0:
    print('positive')
else:
    print('negative')

#4
aas=input("enter ch:\n")
sa =aas.lower()
if len(sa)!= 1:
    print("only enter one charchter")
elif sa=='a' or sa=='e'or sa=='i' or sa=='o'or sa=='u':
    print("is a vowel")
else:
    print("consonant")

#5
marks=int(input("enter your marks:"))
if marks>100:
    print("enter appropriate marks")
elif marks>=90:
    print("excelent")
elif marks>=80:
    print('very good')
elif marks>=70:
    print("good")
elif marks>=60:
    print("average")
else:
    print("fail")

#6
q1 = int(input("enter q1: "))
q2 = int(input("enter q2: "))
q3 = int(input("enter q3: "))
#largest
if q1 > q2 and q1 > q3:
    print("largest =", q1)
elif q2 > q1 and q2 > q3:
    print("largest =", q2)
else:
    print("largest =", q3)
#smalles
if q1 < q2 and q1 < q3:
    print("smallest =", q1)
elif q2 < q1 and q2 < q3:
    print("smallest =", q2)
else:
    print("smallest =", q3)
#7
jk=int(input("enter the number :"))
if jk%2==0:
    print('even')
else:
    print('odd')

#8
j=int(input("enter the year  :"))
if j<1000 | j>9999:
    print('not apporopriate year')
elif j%4==0:
    print('leap year')
else:
    print('not a leap year')
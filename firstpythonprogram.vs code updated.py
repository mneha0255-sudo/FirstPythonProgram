
print("hello world")
print (5+6)
#variables
name="Neha"#string
#identifiers
age=18
price=28
old=False
a=None
#data types,integers,string,float,boolean,none
print("name=",name)
print("age=",age)
print("price=",price)
print("my name is :",name)
print("my age is :",age)
print("my price is :",price)
print("i am old:",old)
print("a")
print(type(name))
print(type(age))
print(type(price))
print(type(old))
print(type(a))
#arithematic operators
A=int(input("enter number="))
B=int(input("enter number="))
C=lambda A,B:(A+B,A-B,A*B,A/B,A**B,A%B)#remainder,A^B
print(C(A,B))
#relational operators
print(A==B)
print(A!=B)
print(A>=B)
print(A<=B)
print(A<B)
print(A>B)
#assingnment operator
num=int(input("enter number="))
num=num+80
print("num:",num)
num+=80
print("num:",num)
num-=80
print("num:",num)
num*=80
print("num:",num)
num/=80
print("num:",num)
num**=8
print("num:",num)
#logical operators
e=int(input("enter number="))
f=int(input("enter number="))
print(not(e>f))
val1=False
val2=True
print("AND operator:",val1 and val2)
print("OR operator:",val1 and val2)
print("NOT operator:",val1 and val2)
print("NOR operator:",val1 and val2)
print("NAND operator:",val1 and val2)
print("EXCLUSIVE NOR operator:",val1 and val2)
print("EXCLUSIVE OR operator:",val1 and val2)
#type conversion
a=int("2")
b=4.25
print(type(a))
sum=a+b#2.0+4.25=>6.25
print(sum)
#type casting
a,b=1,"2"
c=int(b)
sum=a+c
#input in python
name=input("enter your name:")
print("welcome",name)
name=input("enter your age:")
print("you entered",name)
int("5")
val=input("enter some value:")
print(type(val),val)#"25","99.99"
name=input("enter name=")
age=input("enter age=" )
marks=input("enter marks=")
print("welcome",name)
print("age=",age)
print("marks=",marks)
a=float(input("enter number="))
b=float(input("enter number="))
print ("sum=",a+b)
a=float(input("enter length="))
print("area=",a*a)
a=float(input("enter num="))
b=float(input("enter num="))
print("average=",(a+b)/2)
a=int(input("enter number="))
b=int(input("enter number="))
print(a>=b)
str1="neha"
print (len(str1))
str2="more"
len2=len(str2)
print(len2)
final_str=str1+str2
print (final_str)
final_str=str1+" "+str2
print (final_str)
print(len(final_str))
str="neha_more"
ch=str[7]
print(ch)
print(str[1:5])
print(str[0:len(str)])
print(str[2:])
print(str[:8])
print(str[-6:-3])
str="I am a coder and also I am a student"
print(str.endswith("dent"))
print(str.endswith("more"))
print(str.capitalize())
print(str.replace("coder","programmer"))
print(str.replace("a","r"))
print(str.find("coder"))
print(str.find("Q"))
print(str.find("o"))
print(str.count("o"))
print(str.count("I am a"))
#Write a program to input user's first name and print its length
name=input("Enter your name=")
print("length of your name is",len(name))
#To find occurrance in the string
str = input("enter string=")
ch=input("enter character=")
print(str.count(ch))
#conditional statements
age=int(input("enter age="))
if age >= 18:
    if True:
        print("can vote")
    print("can drive")
else:
    print("cannot vote &  cannotdrive")
    colour=(input("enter colour of light="))
    if("colour of light==red"):
        print("stop")
    elif("light colour==green"):
        print("go")#indentation(spacing)
    elif("light colour==yellow"):
        print("look")
    else:
        print("light is broken")
marks=float(input("enter marks="))
if(marks>=90):
    print("grade=A")
elif(marks>=80 and marks < 90):
    print("grade=B")
elif(marks>=70 and marks < 80):
    print("grade=C")
else:
    print("grade=D")
#nesting
age=int(input("enter age="))
if(age>=18):
    if (True):
        print("can vote")
    else:
        print("can drive")
else:
    print("cannot vote & cannot drive")
#list
marks=[94.4,87.5,95.2,66.7,45.3]
print (marks)
print(type(marks))
print(marks[0:4])
print(marks[-1:1])
#mutablity
student=["karan",56.9,18,"Pune"]
print(student[0])
student[0]="arjun"
print(student)
#list methods
m=[input("enter matrix element: ").replace("\n", ",") for _ in range(3)]
print("[" + "\n".join(m)+ "]")
m.sort()
print(m.append("enter additional number="))
print(m.sort())
print(m)
print(m.sort(reverse=True))
print(m)
list=["dragon fruit","peach","litchi","pear","pomogranate","banana","mulberry","blueberry"]
print(list.sort())
print(list)
list.reverse()
print(list)
r=int(input("NUMBER OF ROWS= "))
c=int(input("NUMBER OF COLUMNS= "))
m=[list(map(int,input("enter matrix elements= ").split())) for _ in range(r)]
print("[" + "\n".join(map(str, m))+ "]")
x=sorted(sum(m, []))
m=[x[i*c:(i+1)*c]for i in range(r)]
for row in m:
    print(row)
n=int(input("enter additional number="))
a=sum(m,[])
a.append(n)
a.sort()
print("Sorted:", a)
for i in range(r):
    print(a[i*c:(i+1)*c])   
a.reverse()
print("Reversed:", a)   
for i in range(r):
    print(a[i*c:(i+1)*c])       
list=["dragon fruit","peach","litchi","pear","pomogranate","banana","mulberry","blueberry"]
print(list.sort())
print(list)
list.reverse()
print(list)
list=[56,9,45,67,78,90]
list.insert(1,100)
print(list)
list.pop(3)
print(list)
tup=(56,9,45,67,56,78,90)
print(tup[0:4])
print(tup[-1:1])
tup[-1:1]=[100,200]#tuples are immutable
print(tup.count(56))
print(tup.index(67))
list=(input("enter list of movies: ")).split(",  ")
print(list)
name=(input("enter name: "))
if name==name[::-1]:
    print("palindrome")
else:
    print("not palindrome")
#dictonaries & sets
dict={"name":"neha","age":18,"marks":95.5}#dictionaries
print(dict)
print(dict["name"])
print(dict["age"])
print(dict["marks"])
dict["marks"]=99.5
print(dict)
student={
"name":"neha",
"age":18, 
"marks":95.5
}
print(student)
#dictionary methods
print(list(student.keys()))
print(len(list(student.keys())))(student)
print(list(student.values()))
print(student.items())
pairs=list(student.items())
print(pairs)
print(student.get("name"))
student.update({"marks":100})
print(student)
#sets
sets={1,2,3,4,4,5,6,7,8,9}
print(sets)
print(type(sets))
print(len(sets))
#set methods
print(sets.add(10))
print(sets)
print(sets.remove(4))
print(sets)
print(sets.pop())
print(sets)
print(sets.clear())
print(sets)
print(sets.union({11,12,13}))
print(sets.intersection({1,2,3}))
print(sets.difference({1,2,3}))
print(sets.symmetric_difference({1,2,3}))
#you are given a list of subjects for students. assume one classroom is required for each subject. write a program to find the number of classrooms required for the subjects.
subjects=["maths","science","english","hindi","social science","computer science"]  
classrooms=len(set(subjects))
print("Number of classrooms required:", classrooms)
#loops
count=1
while(count<=5):
    print("hello world")
    count+=1
nums=(input("enter numbers: ")).split(",")
x=sorted(nums)
print(x)
x=(input("enter numbers to search: "))
i=0
while(i<len(nums)):
            if(x==nums[i]):
                print("number found")
                break
            i+=1
else:
                print("number not found")
num=(1,2,3,4,5,67,97,89,90)
x=67
idx=0
for i in num:
    if(i==x):
        print("number found at index:",idx)
        break
    idx+=1
    #range function


for i in range(1,11):
    print(i)
for i in range(1,11,2):
    print(i)
for i in range(10,0,-1):
    print(i)
n=3
fact=1      
i=1
while(i<=n):    
    fact=fact*i    
    i=i+1
print("Factorial of", n, "is", fact)
n=5
fact=1
for i in range(1,n+1):
    fact=fact*i 
print("Factorial of", n, "is", fact)
#functions and recursion
def calculate_factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*calculate_factorial(n-1)
print("Factorial of 5 is:", calculate_factorial(5))
print("Length of 'neha' is:", len("neha"))
print("Type of 'neha' is:", type("neha"))
print("Range from 1 to 10 is:", list(range(1,10)))
def calc_prod(b,a=1):
    return a*b
print("Product of 5 and 3 is:", calc_prod(5,3))
def converter(usd_amount):
    inr_amount=usd_amount*82.74
    return inr_amount
print("Amount in INR is:", converter(100))
#recursion
def show(n):
    if n==0:
        return
    show(n-1)
    print(n)
show(5)
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print("Factorial of 5 is:", factorial(5))
def fibonacci(n):
    if n<=0:
        return []
    elif n==1:
        return [0]
    elif n==2:
        return [0, 1]
    else:
        fib_series=fibonacci(n-1)
        fib_series.append(fib_series[-1]+fib_series[-2])
        return fib_series
print("Fibonacci series up to 10 terms:", fibonacci(10))
def calculate_sum(n):
    if n==0:
        return 0
    else:
        return n+calculate_sum(n-1)
print("Sum of numbers from 1 to 5 is:", calculate_sum(5))
#file i/o
file=open("sample.txt","w")
file.write("Hello, this is a sample text file.\n")
file.close()
file_read=open("sample.txt","r")
content=file_read.read()
print(content)
file_read.close()
data=f.readlines()
for line in data:
    print(line.strip())
    f=open("sample.txt","a")
f.write("This line is appended to the file.\n") 
f.close()
f=open("sample.txt","r")
content=f.read()
print(content)
f.close()
f=open("sample.txt","w+")
f.write("This is a new line in the file.\n")
f.seek(0)
content=f.read()
print(content)
f.close()
f=open("sample.txt","r+")
f.write("This line is written at the beginning of the file.\n")
f=open("sample.txt","a+")   
with open("sample.txt","r") as f:
    content=f.read()
    print(content)
import os
if os.path.exists("sample.txt"):os.remove("sample.txt")
with open("sample.txt","w") as f:
    f.write("This is a new file created using Python.\n")
with open("sample.txt","r") as f:
    content=f.read()
    content=content.replace("python","python programming")
    print(content)

#oops
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Marks:",self.marks)
        class car:
            color="red"
            brand="BMW"
            def __init__(self,model,year):
                self.model="X5"
                self.year=2026
            def display(self):
                print("Color:",self.color)
                print("Brand:",self.brand)
                print("Model:",self.model)
                print("Year:",self.year)
class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def display(self):
        print("Name:",self.name)
        print("Species:",self.species)
        #defalut constructor
class Person:
    def __init__(self):
        self.name="John"
        self.age=30
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        #parameterized constructor
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        #copy constructor
class Person:
    def __init__(self,other):
        self.name=other.name
        self.age=other.age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        #class & instance attributes
class Car:
    wheels=4
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Wheels:",Car.wheels)
class student:
    college="ABC College"
    name="Anonymous"
    def __init__(self,name,age):
        self.name=name
        self.age=age    
        print("College:",student.college)
        print("Name:",student.name)
        #methods
class Calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b!=0:
            return a/b
        else:
            return "Error: Division by zero"
def get_student_info(name,age,marks):
    return {"name":name,"age":age,"marks":marks}
class sudent:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        avg=sum/len(self.marks)
        print(self.name,"average marks:",avg)
        s1=student("neha",18,[95,88,92])
        return avg
    #static methods  #decorator
class MathOperations:
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def subtract(a,b):
        return a-b
    @staticmethod
    def multiply(a,b):
        return a*b
    @staticmethod
    def divide(a,b):
        if b!=0:
            return a/b
        else:
            return "Error: Division by zero"
 #abstraction
class car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.acc=True
        print("car started..")
car1=car()
car1.start()
#Encapsulation
class account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no=acc
        #debt method
        def debit(self,amount):
            self.balance =- amount
            print("Rs.",amount,"was debited")
            print("total balance=",self.get_balance())
        def credit(self,amount):
            self.balance+= amount
            print("Rs.",amount,"was created")
            print("total balance=",self.get_balance())
        def get_balance(self):
            return self.balance
print(account.balance)
print(account.account_no)
acc=account(100000,45375)
acc.debit(1000)
acc.credit(5000)
#delete keyword
class student:
    def __init__(self,name):
        self.name=name
s1=Student("neha")
print(s1.name)
del s1.name
print(s1.name)
class Account:
    def __init__(self,acc_no,acc_pass):
        self._acc_no=acc_no
        self.__acc_pass=acc_pass
    def reset_pass(self):
        print(self.__acc_pass)
acc1=Account("14546","abcde")
print(acc1._acc_no)
print(acc1.__acc_pass())
class person:
    __name="anonymous"
    def __hello(self):
        print("hello person!")
    def welcome(self):
            self.__hello(self.name)
    p1=Person()
    print(p1.__welcome())
#Inheritance
class car:
    def start():
        print("car started")
    def stop():
        print("car stopped")
def _init__(self,name):
        self.name=name
        self.colour="White" 
class ToyotaCar(car):
    def _init__(self,brand,name):
        self.name=name
        self.colour="White"
car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")    
print(car1.name)
print(car1.colour)
class Toyotacar(car):
 def _init__(self,brand):
        self.brand=brand
class Fortuner(Toyotacar):
    def __init__(self,type):
        self.type=type
car1=Fortuner("diesel")
car1.start()
#muliple inheritance 
class A:
    varA="welcome to class A"
class B:
    varB="welcome to class B"
class C(A,B):
    varC="welcome to class C" 
c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
#super method
class car:
    def _init__(self,type):
        self.type=type
    def start():
            print("car started")
    def stop():
            print("car stopped")
class  ToyotaCer(Car):
    def _init__(self,name):
            self.name=name
            super().__init__(type)
            super().start()
car1=ToyotaCar("prius","electric")
print(car1,type)
#class method
class person:
    name="anonymous"
    def changeName(self,name):
        self.name=name # or self.__class__name="rahul"
        @classmethod
        def changeName(cls,name):
            cls.name=name
p1=person()
p1.changeName("rahul kumar")
print(p1.name)
print(person.name)
#property decorator
class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    #def calcpercentage(self):
        #self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3)+"%"
stu1=student(98,97,99)
print(stu1.percentage)
stu1.phy=86
print(stu1.percentage)
#polymorphism
print(1+2)
print("neha"+"more")#concatenate
print(type("neha"))
print([1,2,3]+[4,5,6])#merge
print(type([1,2,3]))
#complex numbers
class complex: #dunder function
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def shownumber(self):
        print(self.real,"i+",self.img,"j")
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg=self.img+num2.ing
        return complex(newreal,newimg)
    def __sub__(self,num2):
            newreal=self.real+num2.real
            newimg=self.img+num2.ing
            return complex(newreal,newimg)
num1=complex(1,3)
num1.shownumber()
num2=complex(14,6)
num2.shownumber()
print(num1+num2)
        #num3=num1.add(num2)
        #num3.shownumber()
num3=num1-num2
num3.shownumber()
class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return (22/7)*self.radius**2
    def permeter(self):
        return 2*(22/7)*self.radius
c1=circle(21)
print(c1.area())
print(c1.radius())
        
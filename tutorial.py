#this is my first python code
#i want to learn python and i am doing it;😎
'''this file must not be deleted because it contains notes
Lets write the first code of python'''
# import os
# print("hello world!")
#practise set-1 Ques=1: write a program to create a poem twinkle twinkle little star
# print('''Twinkle Twinkle Little Star
# How I Wonder what You are!
# Up in above the world so high,
# Like a diamond in the sky''')
#how to write comments
#single line comments: just use # this symbol to write single-line comments
#multi line comments: just use '''''' sign to write multi-line comments
#use ''' when printing more than one line
#practise set-1 Ques=3: install an external module and use it to perform an operation of your intrest
#install playsound module and give it to any mp3 file
#syntax to use playsound
# from playsound import playsound
# playsound('path of the file')
#practise set-1 Ques=4": write a python prograam to print the contents of a diectory using OS module. Search online for the function which does that
#solution:
'''
syntax:
import os
print(os.listdir())
output: files in the directory
'''
#practise set-1 Ques=5":Label the program written in the problem 4 with comments.
#solutions
# 
# syntax:
'''**************************************************end of practise set-1'''

#chapter_2: variables and datatypes in python
#variables: A variable is the name given to  memory location in a progam.for example:
'''
datatype: type of the data written under the guidance of programmer
a= "harry"#string: stores the data written under double quotes/single quotes/triple quotes
b= 989#integer: stores alpha-numerical data
c= 98.89#float: stores the decimal data
d= true or false#boolean: stores the conditional data true or false
e= none#nothing: empty data
for example to check the type of data:
    a= 89#it is a variable and its datatype is int
    syntax: print(type(a))
    output: class<'int'>
'''
#keywords: reserved words under python that can't be used to declare python
'''
Rules to make a variables:
1) A variable name can contain alphabhets, digits and underscores
2) A variable name can only start with n alphabhat and underscores.
3) A variable name can't start with  digit 
4) A variable must not be an integer(1,2,3,4,5,6)
5) A variable must not be written in whitespaces
6) A variable is a case-sensitive
for example: 
    a= 10#here this is different
    A= 123#here this is also different
'''
#invalid variables
# 1a= "fiu"
#output: invalid syntax.


#operators in python
'''
following are the some common operators in python 
1) Arthmetic operators: +,-,*,/,%
2) Assignment operators: =,+=,-=
3) Comprasion operators: ==,<,>,>=,!=
4) Logical operators: and, or, not
'''

#arthmetic operators
# a= 10
# b= 20
# print("the value of 10+20 is ",a+b)
# print("the value of 10-20 is ",a-b)
# print("the value of 10*20 is ",a*b)
# print("the value of 10/20 is ",a/b)
# print("the value of 10%20 is ",a%b)

#assignment operators
# v= 98
# a-=12
# a+=26
# a=6
# print(a)

#comparison operators
# print("the value of 10+20 is ",a==b)
# print("the value of 10+20 is ",a<b)
# print("the value of 10+20 is ",a>b)
# print("the value of 10+20 is ",a<=b)
# print("the value of 10+20 is ",a>=b)
# print("the value of 10+20 is ",a!=b)

#logical operators
# bool1= True
# bool2= False
# print("the value of bool1 and bool2 is",bool1 and bool2)
# print("the value of bool1 or bool2 is",bool1 or bool2)
# print("the value of the bool2 is",not bool2)

#typecasting in python: changing the type of datatypes
#syntax:
# a= "2565"
# int(a)
# print(type(a))
# print(a)

#input functions: taking the value from the user
# a= input("enter your name") #this function will print the name entered while the prompt is shown
# print(a)#a variable that has taked the value of the user and then shows on the screen by using print function.

#Practise set-2, Ques=1: write a python program to add two numbers
# num1= int(input("enter first number:"))
# num2 = int(input("enter a second number:"))
# num3 = (num1+num2)
# print(num3)

#practise set-2, Ques=2: Write a python program to find remainder when a number is divided by Z.
# num1= int(input("enter first number:"))
# num2= int(input("enter second number:"))
# num3= (num1/num2)
# print(num3)

#Practise set-2, Ques=3: Check the type of the variable assigned using input() function.
# ty= int(input("enter a number:"))
# print(type(ty))

#practise set-2, Ques=4: Use comparison operators to find out whether a given variable a is greator than 'b' or not
#Take a= 34 and b= 80
# a= 34
# b= 80
# print(a<b,"is smaller than b")

#practise set-2, Ques=5: Write a program to find average of two numbers entered by the user.
# num1= int(input("enter first number:"))
# num2= int(input("enter second number"))
# num3 = (num1+num2)/2
# print(num3)

#practise set-2, Ques=6: Write a python program to calculate square of a number entered by the user.
# a= int(input("enter a number:"))
# print(a*a)
'''******************************end of python practise set-2*****************************************************'''
#chapter-3 Strings
# a= 89
# b= "harry"
# print(type(a))
# print(type(b))
#introduction to strings
# 
# String is a datatype in Python.
# String is a sequence of characters enclosed in quotes.
# We can primarily, write a string in these three ways
# 1) Single-quoted --> ''
# 2) double-quoted --> ""
# 3) triple-quoted strings --> ''''''''

# String slicing:
# A string in Python can be sliced for getting a part of the string.
# consider the following string:
# a= "harry"
# b= 89
# print(a,b)#output: harry89
# 
#getting length of strings by slicing
#index start with 0 then 1, then 2, and so on....
# name= "harry"
#you cannot change the strings
# name[3]= "d" --> does not work
# print(len(name))
# Negative index can also be used as shown in figure above corresponds to the length-1 index
#the last character of a unknown string can be finded by negative index.
# name= "harry"
# print(name[-3])#output: r
#Slicing with skip value 
#We can provide a askip value as a part of our slice like this:
# word= "amazing"
# d= word[1:3:5]
# print(d)

#len() function: this function will retrun the length of the string.
#for example:
# name= "hemant dahiya"
# length= len(name)
# print(length)

#string endswith function: this function tells wheter the variable's string ends with the string "rry"
# print(name.endswith("a"))

#string.count function: Counts the total number of accurence of any character.
# print(name.count("a"))

#string.captilaize() function: This function capitalizes the first character of a given string.
#print(name.capitalize(""))#only one character will captialize
#String.find(word): Thsis function finds a word and returns the index of the first occurance of that word in the string.
# print(name.find("dahiya"))

#string.replace(old word, new word)- This function replces the old word with new word in the entire string.
# print(name.replace("hemant","dishant"))

#escape sequence character
#to start a new line 
#for ex:
# name1= "hemant\n dahiya"
# print(name1)

'''************************practise set-3, Ques=1: write a python progrm to display a user entered name followed by Good Afternoon using input() function.************************'''
# greetings= input("enter your name:")
# print("Good afternoon",greetings)

#practise set-3, Ques=2: write a program to fill in a letter templte given below with name and date.
'''
letter = 'Dear <!NAME>
you are selected!
<date>'
'''
# letter = '''Dear <|name|>,
# you are selected!
# date: <|date|>
# '''
# name= input("enter your name\n")
# date = input("enter date\n")
# letter= letter.replace("<|name|>",name)
# letter= letter.replace("<|date|>",date)
# print(letter)

#practise set-3, Ques=3: Write a program to detect double spaces in a string.
# space= "hemant dahiya is the owner of world's one of the most famous company"
# doublespaces= space.find("  ")
# print(doublespaces)

#practise set-3, Ques=4: Replace the double spaces from Problem 3 with single spaces.
# space= "hemant dahiya is the owner of world's one of the most famous  company"
# doublespaces= space.replace("  "," ")
# print(doublespaces)

# practise set-3, Ques=5: Write a program to format the following letter using sequence character.
# Letter: "dear harry this python course is nice thanks"
# letter = "dear harry this python course is nice thanks"
# formatted_letter = "dear harry\n\t this python course is nice\t thanks"
# print(formatted_letter)

#****************************end of practise set-3******************************************
#python listing: python lists are containers to store a set of values of any data type
# a= [1,2,3,4,5,6,7,8,9,0]
# print(a)
# a[0] = 89
# print(a[0])

#we can create a list with items of different types.
# c= ["harry",False,89,8.9]

#list indexing start with 0

#List slicing
#sorting the list
# friends= [12,23,56,89,87,1,2,3,]
# # print(friends[0:3])
# print(friends)
# friends.sort()
# print(friends)

#reversing the string
# friends.reverse()
# print(friends)

#adds items to the list
# friends.append(63)
# print(friends)

#inserting in the list
# friends.insert(8,9)
# print(friends)

#removing items from the list according to the index.
# friends.pop(2)
# print(friends)

#removing the items from the list
# friends.remove(23)
# print(friends)

#you don't have to learn all the list methods search on the official python website.


#Tuples in python
# t = (1,2,4,5,1,1,1)
#printing the elements of a tuple
# t[0]= 89# cannot update the tuples(immutiable)
# print(t[0])

#creating an empty tuple
# t2= ()
# print(t2)

#creating a single element tuple 
# t3 = (1)#this is the wrong way to decalre a tuple

#counting the tuples
# print(t.count(1))#no need to make  new variable directly use print function
#go to python.org to view more tuples methods

#practise set-4, Ques=1: Write a program to store fruits in a list entered by the user
# f1 = input("enter fruit number 1\n")
# f2 = input("enter fruit number 2\n")
# f3 = input("enter fruit number 3\n")
# f4 = input("enter fruit number 4\n")
# f5 = input("enter fruit number 5\n")
# f6 = input("enter fruit number 6\n")
# f7 = input("enter fruit number 7\n")

# myfruitlist = [f1,f2,f3,f4,f5,f6,f7]
# print(myfruitlist)

#practise set-4, Ques=2: Write a program to accept marks of 6 students and diplay them in a  sorted manner
# marks1= int(input("enter marks of student 1:\n"))
# marks2= int(input("enter marks of student 2:\n"))
# marks3= int(input("enter marks of student 3:\n"))
# marks4= int(input("enter marks of student 4:\n"))
# marks5= int(input("enter marks of student 5:\n"))
# marks6= int(input("enter marks of student 6:\n"))

# mymarks= [marks1,marks2,marks3,marks4,marks5,marks6]
# mymarks.sort()
# print(mymarks)

#practise set-4, Ques=3: Check that a tuple cannot be changed in pyhton
# change=(1,8,89,8,2)
# change[0]= 5
# print(change)#tuple cannot be changed

#practise set-4, Ques=4: Write a program to sum a list with 4 numbers.
# num1= int(input("enter first number:"))
# num2= int(input("enter second number:"))
# num3= int(input("enter third number:"))
# num4= int(input("enter fourth number:"))

# sum1= [num1+num2+num3+num4]
# print(sum1)
#practise set-4, Ques=5: Write a program to count the number of zeroes:
#a = (7,0,8,0,0,9)
# a= (7,0,8,0,0,9)
# b= a.count(0)
# print(b)

#*****************************************end of practise set-4****************************

#chapter-5 Dictionary and Sets

# mydict = {
#     "fast":"Moving in a speed",
#     "harry":"a coder",
#     1: 2
# }
# print(list(mydict.keys()))to print the keys of the dictionary
#Dictonary is  collection of key-value pairs

#properties of a python dictionary
'''
1) it is unordered
2) it is mutable
3) it is indexed
# 4) cannot contain duplicate keys
'''
# mydict = {
#     "name": "A identity given to a species or a thing",
#     "programming":"creating programs using special languages",
#     "html":"Hyper Text Markup Language",
#     1:2
# }
'''dictonary methods'''
#printing the words
# print(list(mydict.keys()))
#printing their meanings or values
# print(mydict.values())

#dictionary items
# print(mydict.items())#print the key and value of all contents of the dictonary

#updating dictionary: adding new values to the dictionary
# updatedict= {
#     "profession":"hacker"
# }
# mydict.update(updatedict)
# print(mydict)
# print(mydict.get("name"))#returns none if not present in the dictionary
# print(mydict["html"])#throws an error as html is not present

#search on python.org for more dictionary methods


#*****************set******************
# a= {1,3,4,5,1,5}#same elements doesn't count
# print(a)
# print(type(a))
# a= set()#syntax to make an empty set.
# print(type(a))
#you cannot add list and dictonary in a set but can add tuple 
#set methods

# a= set()
# #adding values to na empty set 
# a.add(7)
# a.add(98)
# a.add(4)
# a.add(4)
# # print(a)

#finding the length of the set.
# print(len(a))
#throws an error while trying to remove a value which is not present in the set
#removing a value using pop in python
# prin ())
# print(a)


#practise set-5, Ques=1: write a program to create a dictionary of Hindi word with values as their english translation.provide user with an option to look it up!
# hindidict= {
#     "pankha":"fan",
#     "dabba":"box",
#     "vidhalaya":"school",
# }
# print("options are",hindidict.keys())
# a= input("enter your word in hindi:")
# #dont throw error when the key is not found instead display none
# print("the menaing of your word is:",hindidict[a])

#practise set-5, Ques=2: Write a program to input eight numbers from the user and display all the unique numbers(once)
# f1 = input("enter number 1\n")
# f2 = input("enter number 2\n")
# f3 = input("enter number 3\n")
# f4 = input("enter number 4\n")
# f5 = input("enter number 5\n")
# f6 = input("enter number 6\n")
# f7 = input("enter number 7\n")
# f8 = input("enter number 8\n")
# mylist = {f1,f2,f3,f4,f5,f6,f7,f8}
# print(mylist)

#practise set-5, Ques=3: can e have a set with 18(int) and "18"(str)
# sj= {18,"18"}#set will not throw an error if write a different value
# print(sj)

#practise set-5, Ques=4: What will be the length of following set S.
'''
s= set()
s.add (20)
s.add(20.0)
s.add("20")
'''
# s= set()
# s.add(20)
# s.add(20.0)
# s.add("20")
# print(len(s))

#practise set-5, Ques=5: s= {} 
#What is the type of set.
# s= {}
# print(type(s))

#practise set-5, Ques=6:Create an empty dictionary. Allow 4 friends to enter their favorite languge as values and ue keys a their names. Assure that the names are unique.
# favlang= {}
# a= input("enter your favorite language number1\n")
# b= input("enter your favorite language number2\n")
# c= input("enter your favorite language number3\n")
# d= input("enter your favorite language number4\n")
# favlang['number1'] = a
# favlang['number2'] = b
# favlang['number3'] = c
# favlang['number4'] = d
# print(favlang)

#practise set-5, Ques=7: If nams of two friends are same what will to the program in problem 6
# what = {
#     "name":"hemantdahiya",
#     "name":"kunal gulia",
# }
# print(what["name"])

#practise set-5, Ques=8: If languages of two friends are same; what will happen to probleml 6
#values can be same

#practise set-5, Ques=9: Can you change the value in a list which is in  set S?
# s= {1,2,3,6,6[1,2],"harry"}
# print(s)


#chapter-6 Conditional Expression
'''If else and elif sttements are a multiway decision taken by our program due to certain conditions in our code.
syntax:
if(condition1#if true):
    #python code goes here
elif(condition2#if this condition is true):
    #python code goes here
else:
    #python code goes here
'''
#for example:
# a = int(input("enter a number:"))
# b= int(input("enter the second number:"))
# if (a>b):
#     print("you can go!")
# elif(a<b):
#     print("you cannot go!")
# else:
#     print("you can go if you have permission")

# Quiz:
# a = int(input("enter a number:"))
# if (a>18):
#     print("Yes!")

# else:
#     print("NO")


#Relational operators
'''Relational operators are used to evaluate conditions inside the if statements. Some examples of operators are:
== equals
>= greater than/equal to
<= smaller than/equal to


Logical operators:
In python operators operates on conditional statements. Example:
and --> True if both operands are true else false
or --> True if at least one operand is true else false
not --> Inverts true to false & false to true.
'''
#for Example:
#AND
# a= int(input("enter your age\n"))
# if(a>25 and a<89):
#     print("you can work with us")
# else:
#     print("you can't work with us")

#OR
# a= int(input("enter your age\n"))
# if(a>25 or a<89):
#     print("you can work with us")
# else:
#     print("you can't work with us")

#IS
# a= None
# if(a is None):
#     print("yes")
# else:
#     print("no")

#IN
# a= [45,65,5]
# items= a
# print(items in a)

#Practise set-6, Ques=1: Write a program to find greatest of four numbers entered by the user
# num1= int(input("enter number 1:"))
# num2= int(input("enter number 2:"))
# num3= int(input("enter number 3:"))
# num4= int(input("enter number 4:"))

# if(num1>num4):
#     f1= num1
# else:
#     f1= num4
# if(num2>num3):
#     f2= num2
# else:
#     f2= num3
# if(f1>f2):
#     print(str(f1)+"  is greatest")
# else:
#     print(str(f2)+"is greatest")

#practise set-6, Ques=2: Write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.
# marks1= int(input("enter the marks of the subject:"))
# marks2= int(input("enter the marks of the subject:"))
# marks3= int(input("enter the marks of the subject:"))

# if(marks1<33 or marks2<33 or marks3<33):
#     print("you failed becaus you have less than 33% in one of the subjects")
# elif(marks1+marks2+marks3)/3 <40:
#     print("you fail due to total percentage is less than 40")
# else:
#     print("you passed the exam")

#practise set-6, Ques=3: A spam comment is defined as a text containing the following keyords:
'''"make a bit of money","buy now","suscribe this","click this". Write a program to detect these spams
'''
# vart = "make a bit of money"
# # text = vart
# text= input("enter text\n")
# if(vart in text):
    # spam= False
# else:
    # spam= True
# if(spam):
#     print("this text is a spam")
# else:
#     print("this text is not spam")3

#practise set-6, Ques no=4: Write a program to find wheter a given username contains less than 10 character or not

# username= input("enter a name:")
# test= (len(username))
# if(test>10):
#     print("your username must not contain more than 10 character")
# else:
#     print("your username has been created")

#practise set-6, Ques no=5: Write a program which finds out whether a given name is present in a list or not.
# mylist= ["hemantdahiya","kunalgulia","deepanshugulia"]
# name= input('enter your name\n')
# if name in mylist:
#     print("your name is present in the list")
# else:
#     print("sorry cannot find your name")

#practise set-6, Ques no=6: Write a program to calculate the grade of a student from this marks from the following scheme:
# marks1 = int(input("enter your marks\n"))
# if marks1>90:
#     marks= "EX"
# elif marks1>=80:
#     marks= "A"
# else:
#     marks= "you failed"
# print(marks)

#practise set-6, Ques no=7: Write a program to find out whether a given post is talking about "harry" or not.
# post = "harry is a youtuber who makes videos to teach programming"
# po=  input("enter a name\n")
# if("harry" in po):
#     print("Yes they are talking about harry")
# else:
#     print("No they are not talking about harry")


#Loops in python
#sometime we want to repeat a set of statements in our program.for instance: Print 1 to 1000
'''
Types of loops in python
primarily there are two types of loops in Python
1) while
2) for loop
'''

#while loop: the syntax of a while loop look like this:
#syntax:
'''
while condition:
    #body of the loop --> the block keeps executing until the condition is true
'''
# i = 0
# while i<=10:
#     print("yes"+ str(i))
#     i  = i+1
# print("done")

#Quick Quiz: Write a program to print 1 to 50 using a while loop.
# i= 0
# while i<=50:
#     print(str(i))
#     i= i+1
# print("exceution done!")

#Quick Quiz: Write a program to print the content of a list using while loop
# lit= [1,2,3,4,5,6,7,8,9]
# i = -1
# while i<len(lit):
#     print(lit[i])
#     i = i+1
# print("done")

#for loop: A for loop is used to iterats through a sequence like list, tuple or string [iterables]
#syntax: 
# l = ["mango","watermelon"]
# for item in l:
#     print(item)

#range function in python 
'''
the range function in python is used to generate a sequence of numbers. we can also specify the start and step. size as follows:
'''
# for i in range(2,8):#this will generate an output from 2 to 8
#     print(i)

# for i in range(2,9,3):#this will generate an output from 2 to 8 except 3
#     print(i)

# for i in range(10):
#     print(i)
# else:
#     print(i+1) will print output from 1 to 10 


#Break statement: break statement is used to come out of the loop when encounterd 
# for i in range(10):
#     print(i)
#     if i == 8:#must use
#         break


#continue 
# for i in range(10):
#     if i ==5:#skip the 5
#         continue
#     print(i)

#pass: passes the statement without errors
# a = 89
# b= 90
# if a<b:
#     pass

#practise set-7, Ques=1: Write a program to print multiplication table of a given number using for loop
# table = int(input("enter a number to start printing the table:"))
# for i in range(1, 11):
#     print(i*table)

#practise set-7, Ques=2: Write a program to greet all the person names tored in a list l1 and which starts with S
# l1 = ["harry","sachin","subham","Rahul"]
# for name in l1:
#     if name.startswith("s"):#remember s
#         print("hello "+ name)

#practise set-7, Ques=3: attempt problem 1 using while loop.

#easiest syntax
# num = int(input("enter the number\n"))
# i = 1
# while i<=10:
#     print(num*i)
#     i= i+1

#practise set-7, Ques=4: Wheter this number is a prime or not
# num = int(input("enter the number:"))
# prime = True
# for i in range(2, num):
#     if(num%i == 0):
#         prime = False
#         break
# if prime:
#     print("this number is  prime")
# else:
#     print("this number is not prime")

#practise set-7, Ques=5: Write a program to find the sum of first n natural numbers using while loop.
# num = int(input("enter a number:"))
# n = int(input("enter the limit:"))
# i = 1
# while i<=n:
#     print(i+n)
#     i= i+1

#practise set-7, Ques=6: Write a program to calculate the fctoril of a given number using for loop.

# num = int(input("enter the number:\n"))
# factorial = 1
# for i in range(1, num+1):
#     factorial = factorial*i
#     print(factorial)

#practise set-7, Ques=8: Write a program to print the following star pattern
# for i in range(4):
#     print("*"*(i+1))

#practise set-7, Ques=7: Write a program to print the following star pattern
# n = 3
# for i in range(3):
#     print("" *(n-i-1))
#     print("*" *(2-i+1))
#     print("*" *(n-i-1)

#chapter-8  Functions and recursions

#a function is a group of statements performing a specific task
# marks = [26,56,5,6,89]
# percentage = (sum(marks)/500)*100
# print(percentage)

# def day():
#     good = str(input("enter the name:\n"))
#     print("good morning",good)
# day();
# day();

# def mysum(a,b):
#     return a+b
# s = mysum(3,54)
# print(s)

#Default parameter value
'''
We can also have a value as default argument in a function.
'''
# def greet(name="stranger"):      #this is a default value if no argument is passed
#     print("good day",name)
# greet("hemant dahiya")
# greet()

#recursion is a function which calls itself. It is used to directly use  a mathmetical formula
##note: the programmer need to be extremly careful while working with recursion. recusion is used to make algorithems

# n= 4
# product= 1
# for i in range(n):
#     product = product* (i+1)
# print(product)
# def factorial(n):
#     product = 1
#     for i in range(n):
#         product = product*(i+1)
#         return product
# f=factorial(3+9)
# print(f)

# def factorial_recursive(n):
#     if n==1 or n==0:
#         return 1
#         return n* factorial_recursive(n-1)
# g = factorial_recursive(1)
# print(g)


#Practise set-8, Ques-1: Write a program using function to find the greatest of three numbers
# def maximum(num1,num2,num3):
#     if (num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#                 return num3
#     else:
#         if(num2>num3):
#                 return num2
#         else:
#                 return num3

# m= maximum(33,99,9)
# print("the maximum is ",str(m))

#Practise set-8, Ques-2: Write a python program using function to convert celsius to fahreneit

# def farh(cel):
#     return (cel *(9/5)) + 32
# c= 0
# f = farh(c)
# print("fahreheit Temperature is"+ str(f))

#Practise set-8, Ques-3: How do you prevent a python print() function to print a new line at the end.
#just use end=""
# print("hello",end="/")
# print("world",end="")


#Practise set-8, Ques-4: Write a recursive function to calculate the sum of first n natural numbers
# def add():
#     n=0
#     for i in range(n):
#         n= n+1
#         i = i*n
#         i= i+1
#         print(i)
# add();

#Practise set-8, Ques-5: Write a python function to print first n lines  of the following patterns.
'''
***
**
*
# '''
# n= 3
# for i in range(n):
#     print("*"*(n-i))

#Practise set-8, Ques-6: Write a python function to remove a given word from  string and strap it at the same time
# def remove(string,word):
#     newstr = string.replace(word,"")
#     return newstr.strip()
# this  = "hemant dahiya"
# n = remove(this,"hemant")
# print(n)

#project 1= Snake water gun

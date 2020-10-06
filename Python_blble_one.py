import random
import math
# health = 50
# diffculty = 3

# potion_health =int(random.randint(10, 125) / diffculty)
# print(potion_health)

# increase_health = health + potion_health
# print(increase_health)

# # the above is python health potion file

# # Maths module
# print(round(2.1)) #rounding down
# print(round(1.5)) #rounding up
# print(math.floor(1.5))  # rounding down
# print(math.ceil(2.1)) #rounding up
# print(math.pi)
# print(math.e)
# print(math.sin) #sine
# print(math.sin(math.pi))
# print(math.floor(math.sin(math.pi)))
# print(math.cos(0)) #cosine
# print(math.asin(0)) #
# print(math.asin(0)) # inverse of sine
# print(math.acos(0)) # inverese of cosine
# print(math.hypot(3, 4)) # findin the hypothenus of a right angle triangle
# print(math.pow(2,3))
# print(math.exp(3)) # exponential
# print(math.log(math.e)) 
# print(math.log10(10000)) # log to base 10
# print(math.log2(8)) #log to base 
# # The above is basic mathematical operators

# Stings in python
# Creating string
# "hello"
# name= 'Chukwudumebi'
# print(type(name))
# message = 'Medley said to me "will see you later"'
# print(message)

# # """ used to make quotations"""
# hello = "Hellow world"
# print(hello)

# print(input("What is your name?"))
# print(input("What is your age?"))
# print(input("What do you love doing?"))
# A = 'part one  ' 
# B = 'part two'
# A + B
# print(A + B)# String concatenation
# print('=' * 20)
# A = 'part'
# B = 1
# A + str(B)
# print(A + str(B))
# "{1} - {0}".format(A, B) # String formating
# print("{1} - {0}".format(A, B))

# String Clustering
# name = input("What is your name? :")
# age = input("What is your age? :")
# level = input("What is your level of education? :")
# course = input('what is your specialty? :')
# lecture = input('What do you teach? :')
# string = "I am {} and I am {} years old . I am the {} of {} and am happy to teach you {}".format(name, age, level, course, lecture)
# print(string)
# output = string.format(name, age, level, course, lecture)
# print(output ) 

# 
# # Using string method
# h ='ehllow'.count('l')
# print(h)
# big = 'the birthday present'
# print(big.count('t')) # this is used to count the number of  letter in a string
# sample = 'The  Steadfast Love Of The Lord Never End'
# print(sample.lower())
# print(sample.upper())
# y = 'new moon'
# o = y.capitalize
# q = y.title()

# print(sample.islower())
# print(sample.isupper())
# print(q)
# print(sample.istitle())
# print(sample.isalpha())
# print(sample.isdigit())
# print(sample.isalnum)

# # indexing
# s = 'merrry birthday'
# s.index('birthday')
# print(s.index('birthday'))
# print(s.find('birthday')) # The index function is used to locate the position of an indentation in a string

# Using strip function
# y ="eeeeeeeYouOnLiveOnceeeeeeeee"
# print(y.strip('e')) # used for striping item
# print(y.lstrip('e')) # used for striping item on the left
# print(y.rstrip('e'))# used for stiping item on the right
# # strip() is used for  removing extra space .
# # Length function
# name = input("What is your name?:")
# print(len(name))

# Slicing in python
# sttring are iterable data type meaning you can go step by step until us reach the end
# The element of string start at zero
# string = 'supercalifragilisticexpialidocious'
# print(string[0])
# # slicing can have the beginning of the slice the end of the slice and the step to go in the slice
# print(string[0:5:1]) # This line of code start at 0 index and end at index 5 while moving one step at a time
# print(string[5:9:1])# This line of code start at index 5 and end at index 9 while moving a step at a time
# print(string[5:]) # this line of code start at 5 and goes right to the end
# print(string[5::2]) # This line of code star at index 5 and goes to the end while counting two steps at a time
# print(string[:7]) # This line of code runs from index 0 to 7 but not including 7
# print(string[:7:2]) # This line of code starts from index 0 to 7 without counting 7 while counting two steps at a time
# print(string[::-1]) #  This line of code reverses the string
# print(string[:: 2]) # This line of count two steps at the same time before going to the next
# print(string[-5]) # This line of code count from the end of the code
# print(string.index("fragilisti")) # This line of code starts counting  from the 9 element
# print(string[string.index('cali'):string.index('ex')]) # this line of code return elements starting from the first index element of the string that was included in the list to the first element that was included in  the end of the list not including that particular element
# print(string[string.index('docious'):]) # this is used to return the end element in a given list
# # index retun the first instance of the word you are looking for

# # get use  email address
# email = input("What  is your email address?:").strip()
# #slice out user name
# user = email[:email.index("@")]
# # #slice domain name
# domainName = email[email.index('@') + 1:]
# # # format message
# output ="Your username is {} and your domain name is {}"
# ocommand = output.format(user, domainName)
# # # display output message
# print(ocommand)

# Booleans Comparison Operators
# B = True
# P = False
# print(type(B)) # To know the type of element
# print(2>3) # the greater than operator
# print(type(2>3))
# print(2== 3) # The equallity operator
# print(type(3 != 2)) # The not equal to operator
# print(4 >= 3) # the greater than or equall to operator
# print(6 <= 3)# the less than or equall to operator
# print(3 < 9) # the less than operator

# If Statement
# if True:
#     print("it worked")

# num1 = 100
# num2 = 100
# if num1> num2:
#     print('num1 is bigger than num2')
# elif num2 > num1:
#     print("num2 is bigger num1")
# else:
#     print("They are both equal")

# the formular for if else statement is 
# if condition:
# code (what would happen)
# elif condiontion:
    # code
# else:
# code (what would happen)

# Logical Operatior
# The difference between logical operators and comparism operators
# Comparism operator (including > < == !=) are used to compare piecies of informations to make condition
# Logical operators combine and modify the condition to make bigger conditions
# Example of logical operation
# print(not True)
# print(not False)
# print(not 2 < 3)
# print(not 2 > 3)
# print( not 3 == 4)

# s = 10
# y = 20
# if not y < s:
#     print("it worked")

# G = 20
# D = 3
# if G > 20 and D >1: # using the 'and' operators
    # print("it worked")
# else:
    # print("It is booting it")
# if G >= 20 and D >1:
    # print("it worked")
# else:
#     print("It is booting it")
# if not (G > 20 and D >1): # using the "and" and "not" operators
    # print("it worked")
# else:
#     print("It is booting it")

# The "or" logic operator

# C = 5
# D = 5
# if C > 10 or D >10:
    # print("it worked")
# if C > 1 or D >1:
#     print("it worked")
# if C > 100 or D >100:
    # print("it worked")
# else:
    # print("it is booting")
# if not (C > 100 or D >100):
    # print("it worked")

# C = 6
# D = 2

# if (C > 5 and D > 5) or (C > 1 and D > 1):
    # print("It worked")
# print(False or True)
# print(False and True)
# if not((C > 5 and D > 5) or (C > 1 and D > 1)):
    # print("It worked")
# else:
    # print("not is boooting")

# Data Structure Section in Python
# creating a list done using a square angle bracket
# our_list = [27,46, -5, 17, 99]
# print(our_list)
# a list can contain string, interger, float, booleans
# An iterable  data can be broken down into components called element
# jackson = ["A", "B", "C", 1, 2, 3, "Do", "Rey", True, False ]
# print(jackson[4])
# print(jackson[7])
# print(jackson[-2])
# x  = jackson[6]
# print(x)
# y = jackson[start:end:step]
# y = jackson[0:3:]
# print(y)
# print(jackson[3:1:2])
# our_list = [1,2,[3,4,5,[10, 11, 12,["p", "g", "r",]]], 6, 7, 8]
# print(our_list[2][3][3][1])
# our_table = [[1,2,3],[4,5,6], [7,8,9]]
# our_table2 = [["a","b","c"], ["d", "e", "f"], ["g", "h", "i"], ["j","k", "l"]]
# print(our_table2[1][:2] )

# Application of list Travis the Ridiculous Security System
# known_users = ['Alice', 'Bob', 'Claire', 'Dan', 'Emma', 'Fred', 'Georgie', 'Harry']

# print(len(known_users)) # len means lenght
# while True:
#     print("hi my name is Travis")
#     name = input("Tell me your name?").strip().capitalize()
# #     # mean = name
#     if name in known_users:
#         print("I recognize that name")
#     else:
#         print("you seem new {}".format(name))
#         print("Do you want to join the club")
# The 'in' keyword tell us if a particular element is in a list
# l = [1,5,2,6,2,9]
# print(2 in l)
# # print(10 in l)
    # print("hi my name is Travis")
    # name = input("Tell me your name?").strip().capitalize()
    # # # # mean = name
    # if name in known_users:
    #     print("Hi {}! Good to have you here.".format(name))
    #     remove = input("would you like to be removed from the system (y/n)?:").strip().lower()

    #     if remove == 'y':
    #         print(known_users)
    #         known_users.remove(name) # this is used for removing an element from a list
    #         print(known_users)
    #     elif remove == "n":
    #         print("It is great you are still part of the team")
    #         print(known_users)
    #     elif remove != 'y' or 'n':
    #         print('you made an invalid selection {}'.format(name))
    #         c = input(' do you want to try again? Select y, for yes or n for no:').strip().lower
    # if c == 'y':
    #             print(known_users)
    #             b = input("would you like to be removed from the system (y/n)?:").strip().lower()
                
    # else:
    #     print("you seem new {}".format(name))
    #     print("Do you want to join the club")
    #     add = input("Would you like to join the winning club (y/n)?:").strip().lower()

    #     if add == 'y':
    #         print(known_users)
    #         known_users.append(name) # append method is used for adding element to a list
    #         print(known_users)
    #     elif add == 'n':
    #         print('great you came by')
    #     else:
    #         print('you have made an invalid selection')
            
# using the del function
# l = [1, 2, 3, 4, 5]
# del(l[3]) # del is use to remove a particular index
# print(l)
# example = ['A', 'B', 'C', 'D', 'B', 'C']
# example.remove('B')
# print(example)
# del(example[0:2])
# print(example)
# del(example[0:6:2])
# print(example)
# del and remove can be used to remove element from a list

# Adding things to list with the addition operator, note that only list can be added to list
# example 
# A = [5,12 ]
# a = A +  [1]
# print(a)
# b = [2,3,5,6,8,]
# c = b + ['abcd']
# print(c)
# d = b + list('abcd')
# print(d)
# # Note interger are not iterable that is the can not be converted to list, but we can convert a number to a list by converting it to a string
# e = b + [1, 2, 3]
# print(e)
# f = b + list(123) #will give an error message because the integers have to be converted to string for it to be iterable
# print(f)
# g= b + list(str(123))
# print(g)

# A = [5,12,72,44, 55, 89,1]
# b = A + [[1234]]
# print(A)
# print(A[-1])
# A.append([10,110,123])
# print(A)
# print(A)
# A.insert(2,100)
# print(A)
# list are mutable data type that means they can be  changed after you define them  while string are immutable 
# A = [1,2,3]
# A [0] = 5
# print(A)

# using tuple
# Tuple are similar to list but are immutable data type

# our_tuple = 1,2,3, "A", "B", "c" # tuple can be difined using a comma but it is best to use a parentesis when defining them
# our_tuple2 = (1,2,3, "A", "B", "c")
# print(type(our_tuple))
# print(type(our_tuple2))
# print(our_tuple2[0:3])
# our_tuple2 [0] = 'e' tuple is immutable hence does not support assignment
# print(our_tuple2) tuple is used when you want ot store data that you dont' waht to accidentaly modify
# converting an element to tuple
# A = [1, 2, 3]
# print(tuple(A))
# A = tuple(A)
# print(A)
# tuple can be used for multiple assignment, that is defining mutlplevariable in one for example
# (A, B, C) = 1, 2, 3
# print(A)
# tuple can make mutiple assingnment to list, string, tuple
# example
# G,H,I = "678"
# print(H)
# Tupples work like a list but you can not change them, it is used to store data without changing them


#  DICTIONARIES
# Python dictionaries has key and dict_values
# the Curly bracket are used to creat dictionaries
# Dictionaries = {key : value}
# students = {"Alice":24, "Bob":27, "Claire":17, "Dan":21, "Emma":22}
# # Note, the key must be a string with quotation marks
# print(students["Dan"])
# students['Fred'] = 23
# students["Alice"] = 26
# print(students['Alice'])
# del(students['Bob'])
# print(students)
# print(students.keys()) # prints dictionary keys which has quotation
# print(students.values()) # prints dictionary values which may have or may not have quotation
# a = list(students.keys())
# print(a)
# print(a[1])
# b = list(students.values())
# print(b)
# print(b[2:])
# Note A dictionary unlike list or tupple has no order the just store the keys and value together

# Using Dictionary to assign mutiple values to a single key

# Students = {
#            "Alice":["1D0001", 26, "A"],
#            "Bob":["ID0002", 27, "B"],
#            "Claire":['ID0003', 17, "C"], 
#            "Dan":["ID0004", 21, 'D'],
#            'Emma':["ID0005", 22, "E"]
#            }
# print(Students)
# print(Students['Alice'])
# print(Students['Alice'][0])
# print(Students['Alice'][1:])

# giving each key a value of a dictionary example
# Students = {
#            "Alice":{'id':"1D0001", 'age':26, 'grade':"A"},
#            "Bob":{'id':"ID0002",'age': 27, 'grade':"B"},
#            "Claire":{'id':'ID0003', 'age':17, 'grade':"C"}, 
#            "Dan":{'id':"ID0004", 'age':21, 'grade':'D'},
#            'Emma':{'id':"ID0005", 'age':22, 'grade':"E"}
#            }
# print(Students['Alice']['age'])
# print(Students['Alice']['id'], Students['Alice']['grade'])

# MAKING A CENIMA SIMULATOR
# MAKING USE OF VARIABLE LOGIC AND DATA TYPE AND dATA STRUCTURE

# films = {
#         'Finding Dory':[3,5],
#         'Bourne':[18,5],
#         'Tarzan':[15,5],
#         'Ghost Busters':[12,5]
#         }
# while True:
#     # print('Hey there! What film do you want to watch?')
#     choice = input('Hey there! What film do you want to watch?: ').strip().title()
#     if choice in films:
#         # pass # This function tells python to do nothing
#         age = int(input("How old are you?:").strip())
#         if age >= films[choice][0]: # check user age
#             # Check enough seats
#             # num_seats = films[choice][1]
#             # if num_seats > 0:
#             if films[choice][1]>0:
#                 print("Enjoy the movie!")
#                 films[choice][1] = films[choice][1] - 1
#                 # num_seats = num_seats - 1
#             else:
#                 print("Sorry, we have sold all the movies") 
#         else:
#             print("You are too young to watch that movie")


#     else:
#         print("We don't have the film...")

# WOOKING WITH LOOPS
# WHILE LOOPS
# FOR LOOPS
# LIST COMPREHESION WITH LIST AND LOGIC WITH FOR LOOPS
# # while loop repeat some code over and over while a condition is true
# while True:
#     print("hello")

# while loop runs only when a condition is true it is use for automation of repeatable pattern


# number = 1
# while number  <= 10:
#     print(number)
#     number = number + 1


# number = 1
# while number  <= 20000:
#     if number % 2 == 1:
#          print(number)
#     number = number + 1

# Combining logic with loop 

# L = []
# while len(L) < 3:
#     new_name = input("Please add a new:").strip().capitalize()
#     L.append(new_name)
# print("Sorry list is full")
# print(L)
# while loop would continue to run a certain piece of code as long as the condition is true, but as soon as the condition is false the loop stops running the code

# answer = input("why is the sky blue?: ").strip().lower()
# while answer != 'just because':
#     answer = input("why?: ").strip().lower()
# from random import choice
# questions = ["how old is the earth?: ", "What is a plant?: ", "why does an elephant eat grass?: "]
# question = choice(questions)
# answer = input(question).strip().lower()

# while answer != 'just because God has made it so':
#     answer = input('why?:')
# print('oh...okay')

# FOR LOOPS; CREATING AND USING THEM
# for loops are made up of a variable and an iterable of some kind, and in each round of the for loop, the variable becomes the next value of the iterable
# for python 3  range start from the first index and goes all the way to but not including the last index. Range (start:stop:steps)
# example of using for loop

# for number in range(1,1001):
#     print(number)
# for letter in 'abcd':
#     print(letter)

# counting vowels and consonants
# vowels = 0
# consonants = 0

# # for letter in "hello":
# for letter in 'supercalifragilisticexpialidocious':
#     if letter.lower() in "aeiou":
#         vowels = vowels + 1
#     elif letter == "":
#         pass
#     else:
#         consonants = consonants + 1
# print("There are {} vowers".format(vowels))
# # print("There are {} consonants".format(consonants))
# for letter in '11112223334445559997776666888000':
#     if letter.lower() in "13460":
#         vowels = vowels + 1
#     elif letter == "":
#         pass
#     else:
#         consonants = consonants + 1
# print("There are {} vowels".format(vowels))
# print("There are {} consonants".format(consonants))
# /********************************************************************/
# Using for loop and dictionaries
# students = {
#      'male':['Tom', 'Charlie', 'Harry', 'Frank'],
#      'female':["Sarah", "Huda", "Samantha", 'Emily', 'Elizabeth']
# } # Lets print the name with letter a

# for key  in students.keys():
#     # print(students)
#     for name in students[key]:
#         if 'c'.capitalize() in name:
#             print(name)
 
# /**********************************************************************#
# List Comprehension
# List comprehension is a short hand to combine variable for loops and if statement in a single line of code.
#Example
# even_numbers = [x for x in range(1,301) if x % 2 ==0]
# print(even_numbers)
# odd_numbers = [x for x in range(1,301) if x % 2 !=0]
# print(odd_numbers)

# words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
# answer = [[w.upper(), w.lower(), len(w)] for w in words]
# print(answer)
#/**********************************************************************************
# Pig Latin Project - Part1
# This program takes the first consonant cluste before a vowel in a word and attaches it to the end of the word,
# In addition to that, it adds the letters 'ay' to the word
# If a word starts with vowel the pig latin project just add the letters 'yay' to the end of the word
# Steps in the pig latin project

#get sentence from user

# original = input('Please enter a sentence: ').lower().strip()

# # split sentence into words

# words = original.split()
# # print(words)
# # loop through the words and convert to pig lantin
# new_words = []
# # if the word starts with a vowel, just add 'yay'
# # otherwise, move the first consonant cluster to end, and add 'ay'
# for word in words:
#     # print(word)
#     if word[0] in 'aeiou':
#         new_word = word + 'yay'
#         new_words.append(new_word)
#     else:
#         vowel_pos = 0
#         for letter in word:
#             if letter not in 'aeiou':
#                 vowel_pos = vowel_pos + 1
#             else:
#                 break # used for breaking a loop
#                 # continue # used for continuing a loop
#         cons = word[:vowel_pos]
#         the_rest = word[vowel_pos:]
#         new_word = the_rest + cons + 'ay'
#         new_words.append(new_word)
# print(new_words)
# # stick words back together/
# output = " ".join(new_words)
# # output the final string
# print(output) 

# /*******************************************************************************************
# FUNCTION WHAT THEY ARE, HOW THE WORK AND HOW TO USE THEM
# Function is a block of organized and reuseable code that performs an action or give some result
# They are created by defining the using the def key word

# def add(x,y): # the def tells python we are defining the function, add is the functin neame and x and y are the parameter
#     # parameter can be what ever you like as long as the stick to python rule
#     x + y
#     # To make a function to run we have to call the function, this is done by returning the function
# add(5, 10)
# def add(x,y):
    # return x + y
# print(add(5,10))

# answer = add(100, 20)
# print(answer)
# Note that returning value is not the same as printing. Print just shows things on the screen while return does a funciton
# def add(x, y):
    # print(x + y) 
# word = 'pen'
# print(word[::-1])

# def rev(text):
    # return text[::-1]

# r = rev('texsc')
# print(r)

# e = rev([1,2,3,4])
# print(e)

# /***********************************************************************************************************
# Scoopes
# There are two types of variable scoope in python. The are the local and global variable scoope
# If a variable is in a global scoope, it is a global variable and it can be seen anywhere within the program, and if a variable is in a local scoope it is a local variable and can be seen only in the specific local scope 
# local scope in python is created by fucntion but not with loops and if statement dont


# a  = 100 The variable for the global scope can be seen in any part of the program
# python prevent the changing of a global variable in a local scope so python creates a local variable for the local scope function
# You cant change global variable inside a function automatically, but you can use the variable locally. the local functions are destroyed when the function finishes
# b = 250
# def f1(): # this is the first local scope
#     b = 100
#     print(b)

# def f2(): # this is the second local scope
#     b = 200
#     print(b)

# f1()
# f2()
# print(b)
# a  = 250

# def f1():
#     b = a + 10
#     print(b)

# def f2():
#     a = 50
#     print(a)

# f1()
# f2()
# print(a)

# /****************************************************************************************
# overwriting a global variable in a local function

# a = 250

# def f1():
#     global a #changing a global variable to alocal variable
#     a = 100 #new global value
#     print(a)


# def f2():
#     a = 50 #local value
#     print(a)
# f1()
# f2()
# print(a)


# a = [1,2,3]

# def f1():
#     # global a #changing a global variable to alocal variable
#     a[0] = 5 # Changing part of the global variable
#     print(a)


# def f2():
#     a = 50 #local value
#     print(a)
# f1()
# f2()
# print(a)
# # Note  python function create local scopes but loop and if statment don't
# When using list you can change part of the global variable

# /***********************************************************************************************
# THE DIFFERENCE BETWEEN FUNCTION ARGUEMENT AND FUNCTION PARAMETERS
# KEYWORD ARGUMENT AND DEFAULT PARAMETERS

# def about(name, age, likes): # parameter
#     sentence = "Meet {}! They are {} years old and they like{}".format(name, age, likes)
#     return sentence

# print(about('jack', 23, 'python')) # arguments positional argrment
# print(about(age = 23, name = 'Jack', likes = 'Python')) these are key word argument
  
# def about(name, age, likes = "Python"): # this function has a parameter with a default value
#     sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
#     return sentence
# # print(about('jack', 23))
# print(about('jack', 23, "Foot ball")
# def about(name = 'Ziyad', age = 23, likes = 'python'):
#     sentence = "Meet {}! He is {} years old and he likes {}".format(name, age, likes)
#     return sentence

# # print(about('jack', 29, "Football")) 
# print(about())# this prints out the default parameter with out including arguments

# Note; Parameter are what are in the functions you are defining while argument are what you parse when calling the funtion
# There are two types of argument: They are the key word argument and possitional argurment
# keyword argument can be placed in any order while positional arguement has to be placed in  the order in which the parameter appear in the definition of the function
# You can have as many default parameter as possible as long as you put the last in the definition

# /*************************************************************************************************
# Packing and Unpacking variables
# how to unpack argument
# example
# print(1,2,3,4,5,)
# numbers = [1,2,3,4,5,6]
# print(numbers)
# Unpacking a list  is done  using the astericks symbol *
# print(*numbers) unpacking a list make it possible for eachh item of an iterable datatype to become its own arguement to a function So instead of having a list of number, we hava many arguement with their own number each
# print('abc')
# print(*"abc") this unpack the above item


# Packing arguement
# def add(x,y):
    # return x + y
# print(add(10,10))

# def add(* numbers): #packing an arguement helps us to perform functions with many parameters
#     total = 0
#     for number in numbers:
#         total = total + number
#     return(total)

# print(add(1,2,3,4,5,6,7,8,9))
# Note this is similar to taking the above parameters and inputing the into a tuple. Something like this
# numbers = (1,2,3,4,5,6,7,8,9)
# packing is useful when the number of arguement expected is unknown

# /*********************************************************************************************************************
#  UNPACKING KEYWORD ARGUEMENTS
# def about(name, age, likes):
#     sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)
#     return sentence
#     # NOTE ; one star is used to unpack normal argument  while two stars are used to unpack keyword arguements
# dictionary = {'name':'Ziyad', 'age':23, 'likes':'Python'}
# about(**dictionary)
# print(about(**dictionary))
# /********************************************************************************************************************************
# PACKING KEYWORD ARGUEMENT
# def foo(**kwargs):
#     for key, value in kwargs.items():
#         print("{}:{}".format(key, value))


# foo(huda = 'Female', ziyad = 'male')
# print(foo())
# /*******************************************************************************************************************************************
# board = ["   " for i in range (9)]
# print(board)


# def print_board():
#     row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
#     row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
#     row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    # print()
    # print(row1)
    # print(row2)
    # print(row3)
    # print()


# def player_move(icon):
#     if icon == "X":
#         number = 1
#     elif icon == "O":
#         number = 2

#     print("Your turn player {}".format(number))

#     choice = int(input("Enter your move (1-9): ").strip())

#     if board[choice -1] == "   ":
#         board[choice -1] = icon
#     else:
#         print()
#         print("That space is taken!")
# def is_victory(icon):
#     if (board[0] == icon and board[1] == icon and board[2] == icon) or \
#         (board[3] == icon and board[4] == icon and board[5] == icon) or \
#         (board[6] == icon and board[7] == icon and board[8] == icon) or \
#         (board[0] == icon and board[3] == icon and board[6] == icon) or \
#         (board[1] == icon and board[4] == icon and board[7] == icon) or \
#         (board[2] == icon and board[5] == icon and board[8] == icon) or \
#         (board[0] == icon and board[4] == icon and board[8] == icon) or \
#         (board[2] == icon and board[4] == icon and board[6] == icon) :
#         return True
#     else:
#         return False
# def is_draw():
#     if"   "not  in board:
#         return True
#     else:
#         return False



# while True:
#     print_board()
#     player_move("X")
#     print_board()
#     if is_victory("X"):
#         print("X wins! Congratulations!")
#         break
#     elif is_draw():
#         print("Its a draw!")
#         break
#     player_move("O")
#     if is_victory("O"):
#         print_board()
#         print("O wins! Congratulations!")
#         break
#     elif is_draw():
#         print("Its a draw!")
#         break
    
#     # board[choice -1] = "X"

# /********************************************************************************************************************************************
# OBJECT ORIENTED PROGRAMMING
# cLASSES ARE TEMPLATE USED TO CREATE INSTANCES WHICH ARE object put equally that an object is an instance of a class template
# CLASSES ARE MADE UP OF VARIABLE kNOWN AS STATE AND FUNCTIONS KNOWN AS METHOD
# EXAMPLES ON STATE
# A coin
# Value = 0.1
# Colour = 'Silver'
# Number of edges = 1
# Diameter = 24.5(mm)
# Thickness = 1.85(mm)
# Heads = True

# Function or method in class are like the behavior
# example of coin method
# flip()
# Classes are templates, make an object and an object has state and method
#In classes to create a state use a varible and to cr3ate a behaviour we use method (this another name for funtion in clases)
# Finanlly classes are made up of states and method


# class Pound: # Definning a class
#     # The next is definnning the states
    
#     value = 1.00
#     colour = "gold"
#     num_edges = 1
#     diameter = 22.5 # mm
#     thickness = 3.15 # mm
#     heads = True

# # Creating an object is usually done outside of the class below is an example of a created object
# coin1 = Pound()
# # coin1.value #used to print a  particular state
# print(coin1.value)
# # print(type(coin1))
# print(coin1.colour)
# coin1.colour = 'greenish' # used to change the value of a particular state
# print(coin1.colour)
# coin2 = Pound() # creating another object from the same class
# # print(coin2.colour) note classes are the base template from which objects are made, once the objects are made, each object can have its own unique characteristics which are independent from other object of the same class
# coin1.value = 1.25 # changing the value of a particular state in an object
# print(coin1.value)

# CLASS MEHTODS
# Method are used to give behaviour to our class
# Creating a class metod requires a constructor


import random

# class Pound:


#     def __init__(self, rare = False): # Constructing an object state and a constructor can have more than one parameter
        
#         self.rare = rare
        
#         if self.rare:
#             self.value = 1.25
#         else:
#             self.value = 1.00

#         self.colour = "gold" 
#         self.num_edges = 1
#         self.diameter = 22.5 # mm
#         self.thickness = 3.15 # mm
#         self.heads = True
#     def rust(self):
#         self.colour = 'greenish' # Used to give a new method to an object
    
#     def clean(self):
#         self.colour = 'gold'
    
#     def flip(self): # Using a random method
#         heads_options = [True, False]
#         choice = random.choice(heads_options)
#         self.heads = choice
#     def __del__(self):
#         print('coin spent')

# # coin1 = Pound(rare = True)
# coin1 = Pound()
# # coin2 = Pound()
# coin1.rust()
# coin1.clean()
# coin1.flip()
# coin1.heads
# print(coin1.rare)
# # print(coin2.rare)
# print(coin1.value)
# print(coin1.colour)
# print(coin1.heads)
# # del(coin1)



# class Coin:
#     def __init__(self, rare = False, clean = True, heads = True, **kwargs):


#         for key,value in kwargs.items():
#             setattr(self, key,value)
        

           




#         self.is_rare = rare
#         self.is_clean = clean
#         self.heads = heads

#         if self.is_rare:
#            self.value = self.origninal_value * 1.25
#         else:
#             self.value = self.original_value

#         if self.is_clean:
#             self.colour = self.clean_colour
#         else: 
#             self.colour = self.rusty_colour
#     def rust(self):
#         self.colour = self.rusty_colour

#     def clean(self):
#         self.colour = self.clean_colour

#     def flip(self): # Using a random method
#         heads_options = [True, False]
#         choice = random.choice(heads_options)
#         self.heads = choice

#     def __del__(self):
#         print('coin spent')

        


# class Pound(Coin): # When something inherit from another class it by default takes the behavior of that class 
#    def __init__(self):
#        data = {
#           'original_value': 1.00,
#           'clean_colour': 'gold',
#           'rusty_colour': 'greenish',
#           'num_edges': 1,
#           'diameter': 22.5,
#           'thickness': 3.15,
#           'mass': 9.5
#           }
#        super().__init__(**data) #the super class is used to run the parent data


# one_pound_coin = Pound()
# one_pound_coin.rust()
# # print(one_pound_coin.colour)
# print(one_pound_coin.colour)   



# /*****************************************************************************************************************
# POLYMORPHISM = This is when a method has multiple form in the same class


# class Coin:
#     def __init__(self, rare = False, clean = True, heads = True, **kwargs):


#         for key,value in kwargs.items():
#             setattr(self, key,value)
        

           




#         self.is_rare = rare
#         self.is_clean = clean
#         self.heads = heads

#         if self.is_rare:
#            self.value = self.origninal_value * 1.25
#         else:
#             self.value = self.original_value

#         if self.is_clean:
#             self.colour = self.clean_colour
#         else: 
#             self.colour = self.rusty_colour
#     def rust(self):
#         self.colour = self.rusty_colour

#     def clean(self):
#         self.colour = self.clean_colour

#     def flip(self): # Using a random method
#         heads_options = [True, False]
#         choice = random.choice(heads_options)
#         self.heads = choice
    
#     def __str__(self):
#        if self.original_value >= 1:
#            return "${} Coin".format(int(self.original_value))
#        else:
#             return "{}p Coin".format(int(self.original_value * 100))
            



   


# class One_Pence(Coin): 
#    def __init__(self):
#        data = {
#           'original_value': 0.01,
#           'clean_colour': 'bronze',
#           'rusty_colour': 'brownish',
#           'num_edges': 1,
#           'diameter': 20.3,
#           'thickness': 1.52,
#           'mass': 3.56
#           }
#        super().__init__(**data)

# class Two_Pence(Coin): 
#    def __init__(self):
#        data = {
#           'original_value': 0.02,
#           'clean_colour': 'bronze',
#           'rusty_colour': 'brownish',
#           'num_edges': 1,
#           'diameter': 25.9,
#           'thickness': 1.85,
#           'mass': 7.12,
#           }
#        super().__init__(**data)
        
# class Five_Pence(Coin): 
#    def __init__(self):
#        data = {
#           'original_value': 0.05,
#           'clean_colour': 'silver',
#           'rusty_colour': None,
#           'num_edges': 1,
#           'diameter': 18.0,
#           'thickness': 1.77,
#           'mass': 3.25,
#           }
#        super().__init__(**data)

#        def rust(self):
#            self.colour = self.clean_colour
        
#        def clean(self):
#            self.colour = self.clean_colour



# class Ten_Pence(Coin): 
#    def __init__(self):
#        data = {
#           'original_value': 0.10,
#           'clean_colour': 'silver',
#           'rusty_colour': None,
#           'num_edges': 1,
#           'diameter': 24.5,
#           'thickness': 1.85,
#           'mass': 6.50,
#           }
#        super().__init__(**data)

#        def rust(self):
#            self.colour = self.clean_colour
        
#        def clean(self):
#            self.colour = self.clean_colour

        
# class Twenty_Pence(Coin): 
#    def __init__(self):
#        data = {
#           'original_value': 0.20,
#           'clean_colour': 'silver',
#           'rusty_colour': None,
#           'num_edges': 7,
#           'diameter': 21.4,
#           'thickness': 1.7,
#           'mass':5.00,
#           }
#        super().__init__(**data)

#        def rust(self):
#            self.colour = self.clean_colour
        
#        def clean(self):
#            self.colour = self.clean_colour


# class Fifty_Pence(Coin): 
#    def __init__(self):
#        data = {
#           'original_value': 0.50,
#           'clean_colour': 'silver',
#           'rusty_colour': None,
#           'num_edges': 7,
#           'diameter': 27.3,
#           'thickness': 1.78,
#           'mass':8.00,
#           }
#        super().__init__(**data)

#        def rust(self):
#            self.colour = self.clean_colour
        
#        def clean(self):
#            self.colour = self.clean_colour


# class One_Pound(Coin): # When something inherit from another class it by default takes the behavior of that class 
#    def __init__(self):
#        data = {
#           'original_value': 1.00,
#           'clean_colour': 'gold',
#           'rusty_colour': 'greenish',
#           'num_edges': 1,
#           'diameter': 22.5,
#           'thickness': 3.15,
#           'mass': 9.5
#           }
#        super().__init__(**data) #the super class is used to run the parent data


# class Two_Pound(Coin): # When something inherit from another class it by default takes the behavior of that class 
#    def __init__(self):
#        data = {
#           'original_value': 2.00,
#           'clean_colour': 'gold & silver',
#           'rusty_colour': 'greenish',
#           'num_edges': 1,
#           'diameter': 28.4,
#           'thickness': 2.50,
#           'mass': 12.00,
#           }
#        super().__init__(**data)

    
# coins = [One_Pence(),Two_Pence(), Five_Pence(),Ten_Pence(), Twenty_Pence(),
#         Fifty_Pence(), One_Pound(), Two_Pound()]

# for coin in coins:
#     arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness,
#                   coin.num_edges, coin.mass]

#     string = "{}.Colour: {}, value:{}, diameter(mm):{}. thichkness(mm):{}, number of edges:{}, mass(g):{}".format(*arguments)
#     print(string)

#     def __del__(self):
#             print('coin spent')





# /***************************************************************************************************************************
# MAKING A BANK

class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
        

    def deposit(self,amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
           self.balance -= amount
        else:
            print("Sorry, not enough funds!")

    def statement(self):
        print("Account Balance: ${}".format(self.balance))
   
    def salutation(self):
       print("Thank you for banking with us {}".format(self.name))

class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)
    def __str__(self):
        return "{}'s Current Account : Balance ${}".format(self.name, self.balance)


class Savings(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)
    def __str__(self):
        return "{}'s Savings Account : Balance ${}".format(self.name, self.balance)
# x = Current("Ziyad", 500)
z = Current("Siyad", 500)
z.deposit(5000)
z.salutation()
z.withdraw(800)
z.statement()
z.withdraw(16000)
t = Savings('Tom', 10000)
t.withdraw(300)
t.statement()
print(z)
print(t)

# completed on Octber 6 2020



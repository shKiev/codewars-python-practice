#                               ---===Important Python Concepts===---
# number : int = 10
# decimal : float = 2.5
# text : str = 'Hello, world'
# active : bool = False

# names : list = ['Anna', 'Bob', 'Jenny']
# coordinates : tuple =  (1.5, 2.7) #it can't be change
# unique : set = {1, 4, 2, 9} #it has unique and no-double
# data : dict = {'name': 'Bob', 'age': 20}
#====================================================================================================


# # # Take a firs name as a variable and last name , then print to console "Your name is ____?"


# # #There var take a firs name and a last name

# # fname = input ("What is your first name? ")
# # sname = input ("What is your second name? ")

# # print(f"your fullname is {fname} {sname}")
# # #print("your name is " + fname + " " + sname)

# #===================================================================================================

# #1 Create a greeting for a program.

# #2 Ask for the user for a name of a pet.

# #3 Ask for the name of the city you were born in.

# #4 Combine the pet name with the word cyber as a new twitter handle and then add the city they are from

# # The output should look like "Your new twitter handle and bio @cyberfred from Honolulu. 

# print("Welcome to program")

# pname = input("What is your pet name? \n" )
# cname = input("What was the city name where you was born? ")

# print(f"Your new twitter acc now is @cyber{pname} from {cname}")

# =================================================================================================
# =================================================================================================


# Part 2 DATA TYPES
# 1 String

# print(type("Hello World"))
# print("hello World"[8]) -- this is subscripting!


# 2 Integer
# print(type(5))

# 3 Float
# print(type(5.57))

# 4 Boolean
# True or False

#========================================================================================
#                               LITTLE PROJECT with math.
#========================================================================================

# """
#     In this project, you'll create a program that calculates the total
#     cost of a customers shopping basket, including shipping.

#     - If a customer spends over $100, they get free shipping
#     - If a customer spends < $100, the shipping cost is $1.20 per kg of the baskets weight

#     Print the customers total basket cost (including shipping) to complete this exercise.
# """

# customer_basket_cost = 34
# customer_basket_weight = 44

# # Write if statement here to calculate the total cost
# if customer_basket_cost > 100:
#   print("Free shipping")
# else:
#   shipping = 1.20 * customer_basket_weight

# total = customer_basket_cost + shipping

# print(total)

#========================================================================================
#========================================================================================
#                                         FILES
#========================================================================================
#========================================================================================


# f = open("file_name", "r")
#     print(f.read())

# '''==================================================================================
# To open the file, we use the built-in open() function,
# and the "r" parameter stands for "read" and is used as we're reading the contents of the file. 
# The variable has a read() method for reading the contents of the file.
# You can also use the readlines() method and loop over each line in the file; 
# useful if you have a list where each item is on a new line. 
# '''==================================================================================



# '''==================================================================================
# You can also create and write files.
# If you're writing to an existing file, you open the file first and use the "a" in the open function 
# after the filename call (which stands for append). 
# If you're writing to a new file, you use "w" (write) instead of "a". 
# See the examples below for clarity:

# f = open("demofile1.txt", "a") # Append to an existing file
#     f.write("The file will include more text..")
#     f.close()
    
#     f = open("demofile2.txt", "w") # Creating and writing to a new file
#     f.write("demofile2 file created, with this content in!")
#     f.close()
    
# Notice we use the close() method after writing to a file;
# this closes the file so no more writing to the file (within the program) can occur.
# '''==================================================================================
# import this
# print(type("Всем привет я вот изучать пайтон начал"))

# #======================================================================================
# If you don’t want characters prefaced by \ to be interpreted as special characters, 
# you can use raw strings by adding an r before the first quote:git help git


# >>>
# print('C:\some\name')  # here \n means newline!
# C:\some
# ame
# print(r'C:\some\name')  # note the r before the quote
# C:\some\name
# #======================================================================================
# print(
#    type({}) == type({1}),
#    type(()) == type((1)),
#    )
# #======================================================================================


# #                      = задачка : есть масив а и б, выведи мин макс этих масивов =

# def min_max_funct(a, b):
#     min_a = min(a)
#     min_b = min(b)
#     max_a = max(a)
#     max_b = max(b)
#     return f'min a = {min_a} \nmin b = {min_b} \nmax b = {max_b} \nmax a = {max_a}'

# # добавляем сам список из которого будем выберать мин и мах

# a = [4,6,74,1,54,2,12,33]
# b = [65,44,-7,15,22]

# print(min_max_funct(a, b))

#--------------------------------------------------------------------

def minimum(a,b):
    min_a = min(a)
    min_b = min(b)
    return(f'min_a = {min(a)} \nmin_b = {min(b)}')
    
def maximum(a,b):
    
    max_b = max(b)
    max_a = max(a)
    return f'nmax b = {max_b} \nmax a = {max_a}'

# добавляем сам список из которого будем выберать мин и мах

a = [4,6,74,1,54,2,12,33]
b = [65,44,-7,15,22]

print(maximum(a,b))
print(minimum(a,b))

# Python Project :- 1
# Project Name :- Write a python program to build a simple calculator.

# Available Operations :- 
"""
1. Addition :- Sum of numbers
2. Subtraction :- Difference between two numbers
3. Multiplication :- Product of two numbers
4. Division :- Quotient of two numbers 
5. Average :- Average of numbers"""


# python program to create asimple calculator

# 3 steps to build Simple Calculator
""" 1) Create a Function
    2) User inputs
    3) Print result"""

# Step 1 :- Create a Function 
# Function to add two numbers 
def add(num1,num2):
    return num1 + num2    

# function to subtract two numbers
def sub(num1,num2):
    return num1 - num2

# function to multiply two numbers
def multiply(num1,num2):
    return num1 * num2

# function to dvide two numbers
def divide(num1,num2):
    return num1 / num2

 # function to find avarage of numbers 
def avg(num1,num2):
    return (num1 + num2)/2


# Step 2 :- User Input 
print("Please Select The Operations :\n" \
      "1.Addition \n" \
      "2.Subtraction \n" \
      "3.Multiplication \n" \
      "4.Division \n" \
      "5.Average \n")

select=int(input("Select a Operation From 1,2,3,4,5 :"))
number1=int(input("Enter The First Number :"))
number2=int(input("Enter The Second Number :")) 


# Step3 :- Print The Result
if select == 1:
    print(number1,"+",number2,"=",\
        add(number1,number2))

elif select == 2:
    print(number1,"-",number2,"=",\
        sub(number1,number2))

elif select == 3:
    print(number1,"*",number2,"=",\
        multiply(number1,number2))

elif select == 4:
    print(number1,"/",number2,"=",\
        divide(number1,number2))   

elif select == 5:
    print("(",number1,"+",number2,")","/","2","=",\
        avg(number1,number2)) 

else:
    print("Invalid Operation...! Pls Select again") 
                        
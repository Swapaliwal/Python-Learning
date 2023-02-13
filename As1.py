#!/usr/bin/env python
# coding: utf-8

# # 1.Write a Python program to print 'Hello Python' ?

# In[ ]:


print('Hello Python')


# # 2.Write a Python program to do arithmetic operations addition and division ?

# In[ ]:


import operator

ops = { "+": operator.add, "-": operator.sub, "*":operator.mul, "/":operator.truediv } 

print('Select a Arithmetic Operation:         \n1.Addition(+)        \n2.Division(-)        \n2.Multiplication(*)        \n4.Division(/)        \n3.Stop(0)\n')
   

while True:
    operator = input('Enter a arithmetic operation -> ')
    if operator == '0':
        print("Program Stopped successfully")
        break
    elif operator not in ['+','-','*','/']:
        print("Please enter a valid operator")
    else:
        num_1 = int(input('\nEnter 1st Number: '))
        num_2 = int(input('Enter 2nd Number: '))
        print('{}{}{}={}\n'.format(num_1, operator, num_2, ops[operator](num_1,num_2)))


# # 3.Write a Python program to find the area of a triangle ?
# 

# In[ ]:


h = int(input('enter height : '))
b = int(input('enter base : '))
a = h*b
print('area', a)


# ## 4.Write a Python program to swap two variables ?

# In[ ]:


num_1 = int(input("Enter First Number: "))
num_2 = int(input("Enter Second Number: "))

def swapNumbers(a,b):
    temp = a
    a = b
    b = temp
    return a,b

print('Before swapping -> ',num_1, num_2)
num_1, num_2 = swapNumbers(num_1, num_2)
print('After swapping -> ',num_1,num_2)


# # 5.Write a Python program to generate a random number ?

# In[ ]:


end=int(input('Enter your max number to generate random number between o and ___ '))
from random import randint
def number(start=0,end=1000000):
    print('Random Number -> ', randint(start,end))
number(0,end)


# In[ ]:





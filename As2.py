#!/usr/bin/env python
# coding: utf-8

# ## 1.Write a Python program to convert Kilometers to Miles ?

# In[ ]:


x= int(input('Select 0 for k or 1 for m ?\n'))
            
if x == 0:
    m = int(input('enter no of Miles : '))
    print("{} miles is Equal to {} km".format(m,m/0.621))
      
elif x == 1:
    km = int(input('enter no of Kilometes : '))
    print(km ," km is Equal to ",km*0.621 ," miles")
    
else :
    print('u have entered wrong input')


# ## 2.Write a Python program to convert Celsius to Farenheit ?

# In[ ]:


def celToFarh():
    celsius = int(input("Enter temperature in celsius : "))
    Farenheit = (celsius*(9/5))+32
    print("{}° Celsius is Equal to {}° Farenheit".format(celsius,Farenheit))
    
celToFarh()


# # 3.Write a Python program to display calender ?

# In[5]:


import calendar
def showcalendar():
    year = int(input("Enter year: "))
    print(calendar.calendar(year))
showcalendar()


# ## 4.Write a Python program to swap two variables without temp variable ?

# In[ ]:


num1 = int(input('Enter first number: '))
num2 = int(input('Enter first number: '))
def swap(num1,num2):
        print('Before swap',num1,num2)
        num1 = num1+num2
        num2 = num1-num2
        num1 = num1-num2
        print('after swap',num1,num2)
    
swap(num1,num2)


# In[ ]:





# In[ ]:





# In[ ]:





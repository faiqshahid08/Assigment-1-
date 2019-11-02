#!/usr/bin/env python
# coding: utf-8

# In[7]:


print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are")


# In[9]:


import sys 
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# In[10]:


from datetime import date
today = date.today()
print("Today's date:", today)


# In[19]:


from math import pi 
r=float(input("input The radius of circle"))
print("radius of circle is" + str(r) + " is: " + str(pi * r**2))


# In[23]:


fname=input("input Your First name ")
lname=input("input your last name ")
print( lname + " "  + fname)


# In[35]:



num1=input("1st number ")
num2=input("2nd number ")
sum= float(num1) + float(num2)
print('the sum of {0} and {1} is {2}'.format( num1 , num2 ,sum))


# In[ ]:





# In[ ]:





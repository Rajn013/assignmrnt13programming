#!/usr/bin/env python
# coding: utf-8

# Write a program that calculates and prints the value according to the given formula:
# 
# 
# 
# 
# Q = Square root of [(2 * C * D)/H]
# 
# 
# 
# 
# Following are the fixed values of C and H:
# 
# 
# 
# 
# C is 50. H is 30.
# 
# 
# 
# 
# D is the variable whose values should be input to your program in a comma-separated sequence.
# 
# 
# 
# 

# In[15]:


import math

A = 50
B = 30
D_values = input('Enter comma-separated values of D:').split(",")
Q_values = []
for D in D_values:
    D = float(D)
    Q = math.sqrt((2 * A * D) / B)
    Q_values.append(round(Q))
print(",".join(str(q) for q in Q_values))


# 2.Question 2:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# 
# 
# 
# 
# Note: i=0,1.., X-1; j=0,1,¡Y-1.
# 

# In[24]:


X, Y = map(int, input("Enter two digits X and Y: ").split(","))
array_2d = []

for i in range(X):
    row = []
    for j in range(Y):
        row.append(i*j)
    array_2d.append(row)
print(array_2d)


# 3.Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

# In[25]:


words = input("Enter comma separated sequence of world: ").split(",")
sorted_words = sorted(words)
print(",".join(sorted_words))


# 4.Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

# In[26]:


words = input("Enter whitespace separated sequence of words: ").split()
unique_words =sorted(set(words))
print(",".join(unique_words))


# 5.Write a program that accepts a sentence and calculate the number of letters and digits.

# In[27]:


sentence = input("Enter a sentence: ")
letter_count = 0
digit_count = 0
for char in sentence:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count +=1
        
print("LETTERS",letter_count)
print("DIGITS",digit_count)


# 6.A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

# In[4]:


import re 
def is_vaild_password(password):
    if len(password) < 6 or len(password) > 12:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[$#@]", password):
        return False
    return True

passwords = input("Enter comma separated passwords: ").split(",")
valid_passwords = []
valid_passwords.append(password)

print(",".join(valid_passwords))


# In[ ]:





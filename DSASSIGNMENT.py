#!/usr/bin/env python
# coding: utf-8

# In[12]:


#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
def allpair(array,snum):
    for i in range(len(array)+1):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==snum:
                print("pairs:", (array[i],array[j]))
                
array=[-1,2,5,7,4,3,8,0]
snum=7
allpair(array,snum)


# In[13]:


#Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.
def rarray(array):
    start=0
    end =len(array)-1
    while(start<end):
        temp=array[start]
        array[start]=array[end]
        array[end]=temp
        start+=1
        end=end-1
    return array[start]
array=[2,3,4,5,1,6,9]
print("before reverse:",array)
rarray(array)
print("after reverse:",array)


# In[33]:


#Q3. Write a program to check if two strings are a rotation of each other?
def rotation(s1,s2):
    if len(s1)!= len(s2):
        return False
    s3=s1+s1
    if s2 in s3:
        return True
    else:
        return False
s1=input("enter the 1st string: ")
s2=input("enter the 2nd string: ")
print(rotation(s1,s2))


            


# In[47]:


#Q4. Write a program to print the first non-repeated character from a string?
def non_repeat(str):
    c=[]
    for i in str:
        if (str.count(i)==1):
            c.append(i)
            return c
            
str=input("enter the string: ")
f=non_repeat(str)
print(f)
    

            


# In[53]:


#Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.
def thanoi(n , fstrod, lrod, mrod):
    if n == 0:
        return
    thanoi(n-1, fstrod, mrod, lrod)
    print(n ,"Disk move from", fstrod, "to", lrod  )
    thanoi(n-1, mrod, lrod, fstrod)
          
n =int(input("enter the range: "))
thanoi(n, 'X', 'Z', 'Y') 


# In[79]:


#Q7. Write a program to convert prefix expression to infix expression.
pre=input("enter the experession:")
In=[]
opr=[]
for i in pre:
    if i.isalpha():
        try:
            In.append(i)
            In.append(opr.pop())
        except:
            pass
    else:
        opr.append(i)
print("".join(In))


# In[65]:


#Q8. Write a program to check if all the brackets are closed in a given code snippet.
def bpara(s):
    stack=[]
    for i in range (len(s)):
        if s[i]=="(" or s[i]=="[" or s[i]=="{":
            stack.append(s[i])
        elif len(stack)!=0 and stack[-1]=="(" and s[i]==")":
            stack.pop()
        elif len(stack)!=0 and stack[-1]=="[" and s[i]=="]":
             stack.pop()
        elif len(stack)!=0 and stack[-1]=="{" and s[i]=="}":
             stack.pop()
   
    if len(stack)==0:
        return True
    else:
        return False
s=input("input the brackets: ")
r=bpara(s)
if r==1:
    print("closed")
else:
    print("not closed")
        


# In[70]:


#Q9. Write a program to reverse a stack
            


# In[76]:


#Q10. Write a program to find the smallest number using a stack.



# In[78]:





# In[ ]:





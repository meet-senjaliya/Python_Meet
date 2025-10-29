#!/usr/bin/env python
# coding: utf-8

# ## STRING DATA STRUCTURE
# 

# In[1]:


s = 'LJU'
print(s)
print(id(s))
s = s + "2025"
print(s)
print(id(s))


# ## Typecasting

# In[2]:


a=10
print(a , id(a), type(a))
a = str(a)
print(a , id(a), type(a))


# ## Indexing

# In[3]:


s = 'hello world'
print(s[0])
print(s[-1])
print(s[2])
print(s[-3])
print(s[20])


# ## IMMUTABILITY

# In[5]:


s = 'hello'
s[0] = 'z'   #Error


# ## SLICING

# In[8]:


s = 'hello world'
print("1 - ",s[0:6:2])
print("2 - ",s[2:4:2])
print("3 - ",s[2::-1])
print("4 - ",s[:-1:3])
print("5 - ",s[::2])
print("6 - ",s[0:7:3])
print("7 - ",s[2:-1:2])
print("8 - ",s[:-2:2])
print("9 - ",s[1:-1:3])
print("10 - ",s[-1:-5:-2])
print("11 - ",s[-5::])


# In[9]:


s = 'hello'


# In[10]:


print(s)


# In[12]:


s= s[::-1]


# In[13]:


print(s)


# ## Comparision

# In[14]:


print("gandhi" == "Gandhi")


# In[15]:


print("gandhi" < "Gandhi")


# In[16]:


print(ord('g'),ord('G'))


# In[17]:


print("gAndhi" < "gandhi")


# In[18]:


print("hello" or "world")
print("hello" and "world")


# In[19]:


print(not "")


# ## Looping through string

# In[20]:


s = 'hello'
for i in s:
    print(i,end = " ")


# In[21]:


s='hi'
for i in s:
    print('hello')


# ## Enumerate

# In[24]:


get_ipython().run_line_magic('pinfo2', 'enumerate')


# In[25]:


s = 'hello'
for i,j in enumerate(s,start=100):
    print(i,"--",j)


# ## MEMBERSHIP OPERATOR

# In[27]:


print('z' in 'python')
print('m' not in 'python')


# In[30]:


print('pt' in 'python')


# In[32]:


import keyword


# In[33]:


keyword.kwlist


# ## Universal Methode
# - ` len, max, min, sorted`

# In[37]:


s = 'hello world'
print(len(s))
print(min(s))
print(max(s))
print(sorted(s,reverse=True))


# ## Write a programme to characters and spaces in a given string
#     input = "This is a python tutorial"

# In[39]:


c_char = 0
c_space = 0
s = "This is a python tutorial"
for i in s:
    if i==" ":
        c_space += 1
    else:
        c_char += 1
print("word : ",c_char)
print("space : ",c_space)


# ## STRING ATTRIBUTES AND METHODS

# In[41]:


dir(s)


# In[50]:


s = 'This is python a programming tutorial'


# In[45]:


s.capitalize()


# In[46]:


print(s)


# In[47]:


s.upper()


# ## Title

# In[51]:


s.title()


# ## Swapcase

# In[52]:


s.swapcase()


# ## Count

# In[57]:


s.count('i',15,100)


# In[60]:


s.count('i',15)


# ## Find

# In[64]:


s.find('is')


# In[65]:


s.find('iz')


# In[67]:


print(s)
s.find('is',3,5)


# ## index

# In[69]:


get_ipython().run_line_magic('pinfo2', 's.index')


# In[74]:


print(s)
print(s.index('is'))

# s.index('iz')

print(s.index('is',3,5))


# ## startswith

# In[75]:


print(s.startswith('TH'))
print(s.startswith('th'))


# ## ENDSWITH

# In[76]:


print(s.endswith("al "))
print(s.endswith("al"))


# ## isalnum()

# In[81]:


"12345".isalnum()


# ## isalpha()

# In[82]:


print("this".isalpha())
print("this8".isalpha())


# ## isupper() and islower()

# In[86]:


print("This".isupper())
print("THIS".isupper())
print("this".islower())
print("THIS".islower())


# ## isnumeruc()

# In[87]:


"123abc".isnumeric()


# In[88]:


"123".isnumeric()


# In[89]:


"3.14".isnumeric()


# In[90]:


"%".isnumeric()


# ## isdigit()

# In[91]:


"123.45".isdigit()


# In[92]:


"123".isdigit()


# ## islower(),isupper(), istitle() and isspace()

# In[93]:


print("this".islower())
print("THIS".isupper())
print("This is".istitle())
print(" ".isspace())


# ## SPLIT METHOD

# In[96]:


s.split()


# In[98]:


s.split(maxsplit=1)


# In[100]:


s1 = "This.is.python"
s1.split(".",1)


# ## join

# In[101]:


"".join(["this","is",'python'])


# In[102]:


" ".join(["this","is",'python'])


# In[103]:


"^".join(["this","is",'python'])


# In[105]:


"1".join('python')


# In[107]:


s.replace('is','iz',1)


# ## strip method

# In[108]:


"    hello   ".strip()


# In[109]:


"   hello".strip()


# In[110]:


"hello    ".strip()


# In[ ]:





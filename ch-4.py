#!/usr/bin/env python
# coding: utf-8

# ## STRING DATA STRUCTURE
# 

# In[ ]:


s = 'LJU'
print(s)
print(id(s))
s = s + "2025"
print(s)
print(id(s))


# ## Typecasting

# In[ ]:


a=10
print(a , id(a), type(a))
a = str(a)
print(a , id(a), type(a))


# ## Indexing

# In[ ]:


s = 'hello world'
print(s[0])
print(s[-1])
print(s[2])
print(s[-3])
print(s[20])


# ## IMMUTABILITY

# In[ ]:


s = 'hello'
s[0] = 'z'   #Error


# ## SLICING

# In[ ]:


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


# In[ ]:


s = 'hello'


# In[ ]:


print(s)


# In[ ]:


s= s[::-1]


# In[ ]:


print(s)


# ## Comparision

# In[ ]:


print("gandhi" == "Gandhi")


# In[ ]:


print("gandhi" < "Gandhi")


# In[ ]:


print(ord('g'),ord('G'))


# In[ ]:


print("gAndhi" < "gandhi")


# In[ ]:


print("hello" or "world")
print("hello" and "world")


# In[ ]:


print(not "")


# ## Looping through string

# In[ ]:


s = 'hello'
for i in s:
    print(i,end = " ")


# In[ ]:


s='hi'
for i in s:
    print('hello')


# ## Enumerate

# In[ ]:


get_ipython().run_line_magic('pinfo2', 'enumerate')


# In[ ]:


s = 'hello'
for i,j in enumerate(s,start=100):
    print(i,"--",j)


# ## MEMBERSHIP OPERATOR

# In[ ]:


print('z' in 'python')
print('m' not in 'python')


# In[ ]:


print('pt' in 'python')


# In[ ]:


import keyword


# In[ ]:


keyword.kwlist


# ## Universal Methode
# - ` len, max, min, sorted`

# In[ ]:


s = 'hello world'
print(len(s))
print(min(s))
print(max(s))
print(sorted(s,reverse=True))


# ## Write a programme to characters and spaces in a given string
#     input = "This is a python tutorial"

# In[ ]:


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

# In[ ]:


dir(s)


# In[ ]:


s = 'This is python a programming tutorial'


# In[ ]:


s.capitalize()


# In[ ]:


print(s)


# In[ ]:


s.upper()


# ## Title

# In[ ]:


s.title()


# ## Swapcase

# In[ ]:


s.swapcase()


# ## Count

# In[ ]:


s.count('i',15,100)


# In[ ]:


s.count('i',15)


# ## Find

# In[ ]:


s.find('is')


# In[ ]:


s.find('iz')


# In[ ]:


print(s)
s.find('is',3,5)


# ## index

# In[ ]:


get_ipython().run_line_magic('pinfo2', 's.index')


# In[ ]:


print(s)
print(s.index('is'))

# s.index('iz')

print(s.index('is',3,5))


# ## startswith

# In[ ]:


print(s.startswith('TH'))
print(s.startswith('th'))


# ## ENDSWITH

# In[ ]:


print(s.endswith("al "))
print(s.endswith("al"))


# ## isalnum()

# In[ ]:


"12345".isalnum()


# ## isalpha()

# In[ ]:


print("this".isalpha())
print("this8".isalpha())


# ## isupper() and islower()

# In[ ]:


print("This".isupper())
print("THIS".isupper())
print("this".islower())
print("THIS".islower())


# ## isnumeruc()

# In[ ]:


"123abc".isnumeric()


# In[ ]:


"123".isnumeric()


# In[ ]:


"3.14".isnumeric()


# In[ ]:


"%".isnumeric()


# ## isdigit()

# In[ ]:


"123.45".isdigit()


# In[ ]:


"123".isdigit()


# ## islower(),isupper(), istitle() and isspace()

# In[ ]:


print("this".islower())
print("THIS".isupper())
print("This is".istitle())
print(" ".isspace())


# ## SPLIT METHOD

# In[ ]:


s.split()


# In[ ]:


s.split(maxsplit=1)


# In[ ]:


s1 = "This.is.python"
s1.split(".",1)


# ## join

# In[ ]:


"".join(["this","is",'python'])


# In[ ]:


" ".join(["this","is",'python'])


# In[ ]:


"^".join(["this","is",'python'])


# In[ ]:


"1".join('python')


# In[ ]:


s.replace('is','iz',1)


# ## strip method

# In[ ]:


"    hello   ".strip()


# In[ ]:


"   hello".strip()


# In[ ]:


"hello    ".strip()


# In[5]:


"This is python".strip("Thon")


# ## maketrans and translate() method
# - This method are used to replace indivisual character from given string

# In[7]:


intab = 'aeiou'
outtab = '12345'
mystring = 'This is a string function'
table = mystring.maketrans(intab,outtab)
print(table)
newstring = mystring.translate(table)
print(newstring)


# ## Remove puctuation

# In[8]:


import string


# In[9]:


string.punctuation


# In[15]:


mystring = 'T@h$i#s i^s a s&t*r[i]ng f{unct}ion'
table = mystring.maketrans('i','$',string.punctuation)
print(table)
newstring = mystring.translate(table)
print(newstring)


# ## del method

# In[20]:


s = 'hello'
del s
print(s)


# In[ ]:





# In[ ]:





# ## WAP to implement the find method in string

# In[25]:


def findchar(s,char):
    ind = 0
    for i in s:
        if i==char:
            return ind
        ind += 1   
    else:
        return -1


# In[26]:


s = input("Enter any String : ")
char = input("Enter char to find : ")
print(findchar(s,char))


# ## WAP a programm to shift a number based on following condition
# ```
# input - 12345
# 
# shift - 1 -> o/p = 23451
# 
# shift - 2 -> o/p = 34512
# 
# shift - 3 -> o/p = 45123
# 
# shift - 4 -> o/p = 51234
# 
# shift - 5 -> o/p = 12345
# 
# shift - 6 -> o/p = 54321

# In[17]:


def shifting(number,shift):
    strnumber=(str(number))
    digit = len(strnumber)
    
    if shift > digit:
        result = strnumber[::-1]
    else:
        result = strnumber[shift:] + strnumber[:shift]
        
    return int(result)


# In[18]:


shifting(12345,6)


# ## WAP to convert first and last characters of a word in given string to uppercase
#     input - this is python
#     output - ThiS IS PythoN

# In[26]:


mystring = 'this is python'
s = mystring.title()
m = s.split()
new = ''
for i in m:
    new = new + i[:-1] + i[-1].upper() + " "
print(new)


# ## check password validity

# In[32]:


def passwordcheck(password):
    l=0
    u=0
    d=0
    s=0
    for i in password:
        if i.islower():
            l+=1
        if i.isupper():
            u+=1
        if i.isdigit():
            d+=1
        if i in "@_$":
            s+=1
    if l>=1 and u >= 1 and d>=1 and s>=1 and l+u+d+s >= 8:
        print("valid password")
    else:
        print("invalid password")
         


# In[33]:


passwordcheck('R@1a')


# In[39]:


ip='1+2+1+1+3+3+4+5+2'
s=ip.split('+')
s.sort()
print(s)
"+".join(s)


# ## WAP to check if two string are balanced
# - eg string s1 and s2 are balanced if all th charcter of s1 are in s2 regardleass of position

# In[44]:


s1 = 'lk'
s2 = 'ljku'
valid=True
for i in s1:
    if s2.find(i)==-1:
        valid=False
if valid:
    print("balanced string")
else:
    print("unbalanced string")
    


# ## TUPLE
# - tuple is an immutable
# - ordered
# - sequnced
# - it supports indexing, slicing and iterations
# - Hetrogeneous element

# In[1]:


t = (1,'hi',[1,2,3],None)


# In[2]:


type(t)


# ## zipping

# In[3]:


t1 =(1,2,3)
t2 = (4,5,6)
t = zip(t1,t2)
print(t)
t = tuple(zip(t1,t2))
print(t)


# ## Tuple packing and unpacking

# In[4]:


a =1,2,3,4
print(a)
print(type(a))


# In[5]:


m,n,o,p = a
print(m,n,o,p)


# ## Taking input from th user

# In[7]:


tuple1 = eval(input("Enter numbers saparated by comas - "))
print(tuple1)
print(type(tuple1))


# ## type conversion

# In[8]:


s = 'hello'
t = tuple(s)
print(t)


# In[9]:


l = [2,3,4]
t =tuple(l)
print(t)


# # `+ and *`

# In[10]:


t1 = (1,2,3)
t2 = (4,5,6)


# In[11]:


t1 + t2


# In[13]:


t1 * 3


# ## Membership operators

# In[14]:


8 in (7,8,9)


# In[15]:


9 not in (5,6,7)


# ## iterating through tuple

# In[17]:


t = (4,5,6)
for i in t:
    print(t)


# In[18]:


t = (4,5,6)
for i in t:
    print(i)


# In[19]:


for i,j in enumerate(t):
    print(i,j)


# ## Comparing tuples

# In[20]:


(1,2,3) == (2,3,1)


# In[21]:


(1,2,3) < (1,3,4)


# In[22]:


(1,2,3) < (1,1,4)


# In[23]:


(1,2,'a') < (1,2,'A')


# In[24]:


(1,2,'a') < ('a',2,'A')


# ## univarsal methods
# `len, min , max , sum, sorted`

# In[27]:


t = (8,5,9,1,6,2,3,4)
print(len(t))
print(min(t))
print(max(t))
print(sum(t))
print(sorted(t, reverse=True))


# In[28]:


t = ('python', 'cat','thete','java')
sorted(t)


# In[30]:


t = ('python', 'cat','thete','java')
sorted(t,key = len,reverse=True)


# ## Tuple methods

# In[32]:


t = (6,5,5,5,3,4,7,8,5)


# ## count 

# In[36]:


t.count(5)


# ## index

# In[37]:


t.index(5)


# In[38]:


print(t)


# In[39]:


t.index(5,4)


# ## Generator
# - generator function lazily exicute the code block and stores the iterable and provides the element on demand. if the elements are exhusted it will throw stop iteration error

# In[40]:


x = (i**2 for i in (3,4,5,6))
print(x)


# In[41]:


next(x)


# In[42]:


next(x)


# In[43]:


next(x)


# In[44]:


next(x)


# In[45]:


next(x)


# In[46]:


t = tuple(x)
print(t)


# In[47]:


x = (i**2 for i in (3,4,5,6))
print(x)


# In[48]:


t = tuple(x)
print(t)


# In[49]:


next(x)


# ## comprehension

# In[51]:


x = [i**2 for i in (3,4,5,6)]
print(x)


# In[52]:


x = [i**2 for i in (3,4,5,6) if i**2 > 20]
print(x)


# ## WAP to return the maximum even number from given tuple
# - input - (8,7,2,3,4,5,100,3,56)
# - outout - 100

# In[59]:


def maximum(t):
    max1 = 0
    for i in t:
        if i%2 == 0 and i>max1:
            max1 = i
    print(max1)


# In[60]:


t = (8,7,2,3,4,5,101,100,3,56)
maximum(t)


# In[61]:


t = max(i for i in(8,7,2,3,4,5,101,3,56) if i%2 == 0)
print(t)


# In[62]:


t = tuple(i for i in(8,7,2,3,4,5,101,3,56) if i%2 == 0)
print(t)


# ## PB 314 Ceaser cipher
# - input : LJIET ENG
# - shift - 3
# - Cipher - OMLHW HQJ

# In[ ]:





# In[73]:


def encrypt(message,key):
    message = message.upper()
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    
    for letter in message:
        if letter in alpha:
            letterindex = (alpha.find(letter) + key) % 26
            result = result + alpha[letterindex]
        else:
            result += letter
    return result


# In[75]:


encrypt("ljiet eyg",3)


# ## WAP to replace special symbol in a given string with `#`
# 
# `input - l^j$i[e?t`
# `output - ljiet`

# In[80]:


import string
s = input("Enter string - ")
for i in string.punctuation:
    s = s.replace(i,'#')
print(s)


# ## WAP to find the sum of nagative numbers in given tuples

# In[85]:


t = sum(i for i in(8,7,-2,3,4,-5,-101,3,56) if i < 0)
print(t)


# In[ ]:





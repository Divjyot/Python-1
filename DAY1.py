#output command
print('Harry')
#variable declaration and assigning values
a=10
b=1.01
c=1j
print(a, b, c)
#declaration in single line and sum of two numbers
a,b,c= 10, 12, 1.2
print(a+b, c)
#string can be in '' or ""
a='harrie'
print(a)
#printing variable with predefined text in ""
print("this is " + a)
#random number with range
import random
print(random.randrange(1,100))
#multiple Strings this can be in """----""" or '''----'''
a="""hey this is harrie"""
print(a)
#joining two strings in a variable
a= "harrie "
b= "singh"
c= a+b
print(c)
#data type of variable
print(type(a))
#specifing data types
x=str("hi")
y=int(2.09)
z=list(("ap","op"))
print(x,y,z)
print(type(x),type(y),type(z))
#Strings are array
a="abcdef"
print(a[0])
#positive indexing
a= 'harry is dumb'
print(a[0:5])
#negative indexing (starting from back)
print(a[-7:-4])
#String length
a='harrie'
print(len(a))
#String methods;
#strip()-toremove whitespace
#lower()-to make text in lower case
#upper()-to make text in upper case
#replace()-to replace word
a=" Harrie Is White "
print("original; "+ a)
print(a.upper())
print(a.strip())
print(a.lower())
print(a.replace("ie","y"))
#Check strings
txt= "harrie is in"
tbt= "he is not in"
x= "harrie" in txt
y= "harrie" in tbt
print(x,y)
x= "harrie" not in txt
y= "harrie" not in tbt
print(x,y)
#formating int to add in string
age= 16
txt= "My age is {}"
print(txt.format(age))
#multiple formating
a=10
b=12
c=28
txt= "value of a is {} Value of b is {} Value of c is {}"
print(txt.format(a,b,c))
#multiple formating unorderd
c=28
b=12
a=10
txt= "value of a is {2} Value of b is {1} Value of c is {0}"
print(txt.format(c,b,a))
#Escape Characters
txt= "Hey this is \"Harrie\" from Punjab"
print(txt)
txt= "Hey this is \'Harrie\' from Punjab"
print(txt)
txt= "Hey this is \\Harrie\\ from Punjab"
print(txt)
txt= "Hey this is \nHarrie from Punjab"
print(txt)
txt= "Hey this is \tHarrie from Punjab"
print(txt)
txt= "Hey this is \aHarrie from Punjab"
print(txt)
#Boolean
print(100<200)
print(100>200)
print(100==200)
a=10
b=20
if a < b:
    print("b is Greater")
else:
    print("a is Greater")
#isinstance is used to verify the value
print(isinstance(a,int))

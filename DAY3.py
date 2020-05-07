#tuple writen in () and they are unchangable
tpl1=("apple","orange","banana")
print(tpl1)
#indexing is same as of Lists
#range the first is included but not the last
print(tpl1[0:2])
#modifing tuple
x=("a","o","c")
y=list(x)
y[1]="b"
x=tuple(y)
print(x)
#loop in tuple
for x in x:
    print(x)
#Checking items in tuple
if "apple" in tpl1:
    print("apple is here")
print(len(tpl1))
#Single element tuple(add coma after element)
x=("Harry",)
print(x)
#deleting tuple will delete whole tuple
del tpl1
#joining tuple are same as list with '+'
#tuple constructor
x=tuple(("Toyota","Maruti","Hyndayi"))
print(x)
########################################### (SETS) written in '{}'
set={"apple","orange","banana"}
print(set)
#Accessing Set only by for not by index
for x in set:
    print(x)
#Checking item Present in set results bool value
print("banana" in set)
#Changing items
#Adding Items
set.add("kiwi")
print(set)
#to add multiple items use update()
set.update(["mango","grapes","peach"])
print(set)
#set length
print(len(set))
#Removing elements
#remove() method - leave a error if item not in list
set.remove("peach")
print(set)
#discard() method - no error
set.discard("peach")
#pop() metod- we cant assign the index and will delet random element
set.pop()
print(set)
#clear() method- cleares all the Set
set.clear()
print(set)
#del method- delets the Set
del set
#Joining 2 SETS
#union() Method
set1={"a","b","c"}
set2={"1","2","3"}
set3= set1.union(set2)
print(set3)
#update() metod - this will update one set with both quantities
set1.update(set2)
print(set1)
#set constructor
set=set(("this","is","a","set"))
print(set)
#########################################  PYTHON DICTIONARY
mydict= {
    "brand":"Toyota",
    "model":"Fortuner",
    "year": 2015
}
#Accessing items
print(mydict)
x=mydict["model"]
print(x)
#by get
x=mydict.get("brand")
print(x)
#Changing Values
mydict["year"]=2018
print(mydict.get("year"))
#Loop in DICTIONARY - this will print only key
for a in mydict:
    print(a)
#Loop in DICTIONARY - Values
for a in mydict:
    print(mydict[a])
for a in mydict.values():
    print(a)
#Loop for both keys and Values
for x,y in mydict.items():
    print(x,y)
#Check if key exists
if "brand" in mydict:
    print("Brand Yes")
#DICTIONARY length
print(len(mydict))
#Adding items
mydict["colour"]="Black"
print(mydict)
#Removing items
#--by pop() Method
mydict.pop("brand")
print(mydict)
#--by popitem() method
mydict.popitem()
print(mydict)
#--by del method
#del mydict
#Copying DICTIONARY
thisdict = mydict.copy()
print(thisdict)
del thisdict
thisdict = dict(mydict)
print(thisdict)
#NESTED DICTIONARY
myfamily= {

    "child1":
    {
    "name":"Divjyot",
    "year":1993
    },
    "child2":
    {
    "name":"Bhavneet",
    "year":1997
    },
    "child3":
    {
    "name":"Harry",
    "year":2003
    }
}
for x,y in myfamily.items():
    print(x,y)
#Nesting if already other are DICTIONARY
child1 ={
"name":"Divjyot",
"year":1993
}
child2 ={
"name":"Bhavneet",
"year":1997
}
child3 ={
"name":"Harry",
"year":2003
}
myfamily1={
"child1":child1,
"child2":child2,
"child3":child3
}
print(myfamily1)
del mydict
#Dict constructor
mydict = dict(brand="ford", model="mustang", year="2019")
################################-- If-Else
#Usinf If
a = 13
b = 20
if a < b:
    print("b is greater")
#Using elif
if a > b:
    print("elif a is greater")
elif b > a:
    print("elif b is greater")
#Using Else
a = 20
b = 20
if a > b:
    print("a is greater")
elif a < b:
    print("b is grater")
else:
    print("Equal")
#if you have only one statement to exucute with if-Else
if a == b: print("a is greater")
print("b is greater") if a < b else print("whtever")
print("A") if a > b else print("=") if a == b else print("B")
#And keword
a = 10
b = 20
c = 15
if b > c and b > a: print("YES")
#Or keword
if c < b or c < a: print("YESC")
#NESTED IF
x=15
if x > 10:
    print("greater than 10")
    if x > 20:
        print("greater than 20")
    else:
        print("below 20")
#put pass to avoid error
if a < b:
    pass
#####################################LOOPS-WHILE-FOR
#--WHILE LOOP
i = 1
while i < 6:
    pass
    print(i)
    i+=1
#WHILE BREAK
i = 1
while i < 6:
    pass
    print(i)
    if i == 3:
        break
    i+=1
#WHILE CONTINUE
i = 1
while i < 6:
    pass
    i += 1
    if i == 4:
        continue
    print(i)
#WHILE ELSE
i=1
while i<6:
    pass
    print(i)
    i+=1
else:
    print("I am hahha")
#FOR loop
abc=["a","b","c"]
for x in abc:
    print(x)
#String LOOP
for x in "fruit":
    print(x)
#break stat1
for x in abc:
    print(x)
    if x=="b":
        break
#break stat2
for x in  abc:
    if x=="b":
        break
    print(x)
#continue
for x in abc:
    if x=="b":
        continue
    print(x)
#Range()
for x in range(10):
    print(x)
#Range between two
for x in range(2,10):
    print(x)
#Range for sequence
for x in range(2,10,2): #sequence for 2
    print(x)
#Else in for LOOP
for x in abc:
    print(x)
else:
    print("cmplt")
#NESTED loop
adj=["red","big","tasty"]
frt=["apple","banana","cherry"]

for x in adj:
    for y in frt:
        print(x,y)
#pass
for x in abc:
    pass
######################--FUNctions

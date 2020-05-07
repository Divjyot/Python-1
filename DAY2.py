#Lists
thislist = ["Harry","Rahul","Krish"]
print(thislist)
print(thislist[0]) # Indexing
print(thislist[-1])
#for printing 1 by 1
for x in thislist:
    print(x)
#Checking Items
if "Harry" in thislist:
    print("yes")
#List length
print(len(thislist))
#adding items #append
thislist.append("Singla")
print(thislist)
#Inserting items inbetween
thislist.insert(1,"Sidharth")
print(thislist)
#Removing items
thislist.remove("Singla")
print(thislist)
#this will remove by index, if not specified it will remove last index
thislist.pop(1)
print(thislist)
#by del
del thislist[1]
#this delets whole list with the list variable
print(thislist)
del thislist
#by clear this will clear the list items but not the variable
thislist=["apple","banana","orange"]
print(thislist)
thislist.clear()
print(thislist)
#Copping List
thislist=["Car","Computer","Cat"]
copylist=thislist.copy()
print(copylist)
#Copping by list()
copylist.clear()
print(copylist)
copylist=list(thislist)
print(copylist)
#Join two Lists
list1=["Harry","Krish"]
list2=["Rahul","Gautum"]
list3 = list1 + list2
print(list3)
list3.clear()
#By append
for x in list2:
    list1.append(x)
print(list1)
#By Extend Method
l1=["a","b","c"]
l2=["1","2","3"]
l1.extend(l2)
print(l1)
#list constructor
thislist=list(("ap","ba","or"))
print(thislist)
 

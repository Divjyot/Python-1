#defining a function
def myfnc():
    print("hello function")
#calling function
myfnc()
#argument
def myfnc1(nam):
    print(nam+" singh")
myfnc1("Harry")
myfnc1("Deep")
myfnc1("anyone")
#number of argument
def itfnc(fn,ln):
    print(fn+" "+ln)
itfnc("Harry","Singh")
#arbitary arguments- will select onearry argument from list
def fam(*kid):
    print("smalest "+ kid[1])
fam("Harry","Nonu","gudia")

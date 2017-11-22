name = 'mariam'
print (name)

num = 12
print (num)

name1 = str(input("Enter name:"))
age = int(input("Enter age"))
#print ("Hey" + name1) 

#function that takes in user input and then greet the user with input
def read_input(name, age):
    """ reads user input"""
    return "hey, {}  {} old".format(name, age)

print (read_input(name1, age))

def print_many(*args):
    arg1, arg2 = args
    """ r stands for raw input
    s stands for string
    d stands for decimal"""
    """ This prints the args as they are, whether number or string"""
    print("arg1: %r, arg2: %r" % (arg1, arg2))


""" This prints only numbers. A string would bring an error
    print ("arg1: %d, arg2: %d" %(arg1, arg2))

    This prints them as strings, no quotes
    print ("arg1: %s, arg2: %s" %(arg1, arg2))"""

"""print_many("12", "23")"""


def string(par):
    string = par
    x = "martha"
    return string + x


print(string("pin"))


def string1(par1, par2):
    string = par1
    string2 = par2
    return string, string2


print(string1("magic", "martha"))


def listt(*args):
    return list(args)


print(listt(2, 3, 4, 5, 6, 7, 8, 9))


def listt(*args):
    list1 = list(args)
    list1.pop(2)
    return list1


print(listt(2, 3, 4, 5, 6, 7, 8, 9))


def listt(*args):
    list1 = list(args)
    return list1.pop(2)


print(listt(2, 3, 4, 5, 6, 7, 8, 9))

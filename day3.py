list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""for loop"""
for x in list1:
    if x % 2 == 0:
        print('even')
    else:
        print('odd')

for i in range(0, 20, 3):
    """using the range method, first and second values are the start and
    stop ranges,the third value is the step"""
    print(i)

names = ['mariam', 'lucky', 'martha', 'magic', 'breezy']
for name in names:
    print(name.capitalize())

dictionary = {}
dictionary["name"] = "lucky"
dictionary["age"] = 18
dictionary["hobbies"] = ["sleeping", "eating"]
print(dictionary)

d = dict(name="magic", age=22, hobbies=["chess", "coding"])
print(d)

student1 = dict(name="magic", age=22, hobbies=["chess", "coding"])
class1 = {}
class1["mariam"] = student1
class1["etwin"] = dict(name="probuse", age=23, hobbies=["weed", "coding"])
print(class1)

print(class1["etwin"])

class1["etwin"]["hobbies"] = ["gym", "reading"]
print(class1["etwin"]["hobbies"])

class1["etwin"].update({"hobbies": ["coding", "swimming"], "sex": "male"})
print(class1["etwin"])

for hobby in class1["etwin"]["hobbies"]:
    print(hobby)

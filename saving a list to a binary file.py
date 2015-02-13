#Lewis Travers
#13/2/2015
#saving a list of records to a binary file

import pickle

class People:
    def __init__(self):
        self.name = None
        self.DoB = None

names = []

def details(names, People):
    done = False
    while done == False:
        new_person = People()
        new_person.name = input("Please enter a person's name. Press only the enter key if you are finished: ")
        if new_person.name == "":
            done = True
        else:
            new_person.DoB = input("Please enter their DoB in this format dd/mm/yyyy: ")
            names.append(new_person)

def binary_file(names):
    with open("people.txt", mode="wb") as people_file:
        pickle.dump(names, people_file)



#main program

people = details(names, People)
file = binary_file(names)

#Lewis Travers
#10/02/2015
#appending names to a text file

with open("studentnames.txt", mode="w", encoding="utf-8") as my_file:
     done = False
     while done == False:
         name = input("Please enter a name. When done enter -1: ")
         if name == "-1":
             done = True
         else:
             my_file.write(name+"\n")
         

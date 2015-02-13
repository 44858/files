#Lewis Travers
#10/02/2015
#student names

with open("studentnames.txt", mode = "r", encoding ="utf-8") as my_file:
    count = 0
    for line in my_file:
        count = count + 1
        print("{0}. {1}".format(count, line))

#Lewis Travers
#13/02/2015
#displaying contents of a file

with open("my_file.txt", mode="r", encoding="utf-8") as my_file:
    for line in my_file:
        print(line, end="")

#Lewis Travers
#12/02/2015
#saving lines of text to a file

with open("my_file.txt", mode="w", encoding="utf-8")as my_file:
    for count in range(5):
        message = input("Please enter a message: ")
        my_file.write(message+"\n")

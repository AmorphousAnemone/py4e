# This program reads through a file and print the contents of the file (line by line)
# all in upper case.

xfile = open('mbox-short.txt')
for line in xfile:
    print(line.upper())
# Write a program to open the romeo.txt and read it line by line.
# For each line, split the line into a list of words using the split function.

# For each word, check to see if the word is already in a list. If the word is not in the list, add it to the list.

# When the program completes, sort and print the resulting words in alphabetical order.

fname = input('Enter file: ')

try:
    xfile = open(fname)
except:
    print('Cannot open')
    quit()

mylist = list()
for line in xfile:
    # Parse word by word
    for word in line.split():

            ### UNPLANNED CODE EXAMPLE ###
        # if '\n' in word:
        #     # remove \n from word and add to list
        #     rmword = word[:word.find('\n')]
        #     if rmword in mylist:
        #         print("Hello")
        #     mylist.append(rmword)
        #     continue
        #     # print(rmword)
        # if word in mylist:
        #     print('Hello')
        # mylist.append(word)

        # remove \n from word and add to a list
        # wordcopy = word
        # if '\n' in word:
        #     wordcopy = word[:word.find('\n')]
        
        if word in mylist:
            continue
        mylist.append(word)
mylist.sort()
print(mylist)

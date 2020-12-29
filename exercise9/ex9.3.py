# Write a program to read through a mail log, build a histogram using a dictionary
# to count how many messages have come from each email address, and print
# the dictionary

fname = input('Enter file name: ')
try:
    xfile = open(fname)
except:
    print('File not found')
    quit()

print('all good')

emaillist = dict()
for line in xfile:
    if "From " in line:
        words = line.split()
        key = words[1]
        emaillist[key] = emaillist.get(key, 0) + 1
        # print(words[1])

print(emaillist)

# for key,value in emaillist.items():
#     print(key + ': ' + str(value))
    
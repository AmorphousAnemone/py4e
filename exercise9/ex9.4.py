# After all the data has been read nad the dictionary has been created,
# look through the dictionary using a maximum loop (see
# Section [maximumloop]) to find who has the most mesages 
# and print how many messages the person has.

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

# print(emaillist)

maxname = None
maxvalue = None
for email,count in emaillist.items():
    if maxvalue is None or count > maxvalue:
        maxvalue = count
        maxname = email

print(maxname + ': ' + str(maxvalue))

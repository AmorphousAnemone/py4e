# This program records the domain name (instead of the address) where
# the message was sent from instead of who the mail came from (i.e.,
# the whole email address). At the end of the program, print out
# the contents of your dictionary


fname = input('Enter file name: ')
try:
    xfile = open(fname)
except:
    print('File not found')
    quit()

print('')
# print('all good')

# Returns domain from full email address
def splitter(fullemail):
    emailparts = fullemail.split('@')
    domain = emailparts[1]
    return domain

domainlist = dict()
for line in xfile:
    if "From " in line:
        # Handle error from the single line in text file causing trouble
        if " From " in line:
            continue
        words = line.split()    
        key = splitter(words[1])   
        domainlist[key] = domainlist.get(key, 0) + 1
        
            ### Debugging ###
        # fullemail = words[1]
        # emailparts = fullemail.split('@')
        # 
        # try:
        #     jjj = emailparts[1]
        # except:
        #     print(line)

for key,value in domainlist.items():
    print(key + ': ' + str(value))
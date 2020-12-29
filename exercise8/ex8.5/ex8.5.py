# Write a program to read though the mail box data and when you find line
# that start with "From", split the line into words using 'split' function.
# We are interested in who sent the messge, which is the second word on the From line.
#
#   From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#
# Parse the From line and print out the second word for each From line,
# then you will also count the number of From (not From:) lines and 
# print out a count at the end.

fname = input('Enter a file name: ')
try:
    xfile = open(fname)
except:
    print('Cannot open file - Exiting')
    quit()
    
print('File Opened')

linelist = list()
for line in xfile:
    if 'From' in line and not 'From:' in line:
        # grabs email portion in line
        try:
            # Some "From" lines contain only 1 element
            email = line.split()[1]
        except:
            continue
        linelist.append(email)

print(linelist)
print('There were ' + str(len(linelist)) + ' lines in the file with From as the first word')

# Write a program to prompt fr a file name, and the read through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# 
# When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line
# to extract the floating-point number on the line. Count these lines and then compute
# the total of the spam confidence values from these lines. When you reach the end of the file,
# print out the average spam confidence

# prompt
#fname = input('Enter the file name: ')
fname = input('Enter the file name: ')

#easter egg
if fname == 'na na boo boo':
    print('NA NA BOO BOO TO YOU - You have been punk\'d!')
    quit()

try:
    xfile = open(fname)
except:
    print('File cannot be opened: ' + fname)
    quit()

# count = 0
# fvalue = 0
# for line in xfile:
#     if 'X-DSPAM-Confidence:' in line:
#         # Adds the float value found after the colon to the previous values
#         fvalue = fvalue + float(line[line.find(':')+1:].strip())
#         count = count + 1
# print(fvalue / count)

numlist = list()
for line in xfile:
    if 'X-DSPAM-Confidence:' in line:
        numlist.append(float(line[line.find(':')+1:].strip()))

print(sum(numlist) / len(numlist))
fname = input('Enter a file name: ')

try:
    xfile = open(fname)
except:
    print('no good')
    quit()

counts = dict()
for line in xfile:
#   "From " differentiates from "From:"
    if "From " in line:
        words = line.split()
        day = words[2]
        counts[day] = counts.get(day, 0) + 1

print(counts)
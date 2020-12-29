import urllib.request, urllib.parse, urllib.error

link = input('Enter web address: ')

if 'http://' not in link:
    link = 'http://' + link

try:
    fhand = urllib.request.urlopen(link)
except:
    print('Not a web address')
    quit()

document = ''
for line in fhand:
    document = document + line.decode()

print(document[:3000])
print(len(document[:3000]))
import socket

link = input('Enter Web Address: ')
hostname = link.split('/')[0]

print(hostname)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mysock.connect((hostname, 80))
except:
    print('not a web address')
    quit()

cmd = ('GET http://' + link + ' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()

# GET http://data.pr4e.org/romeo.txt HTTP/1.0
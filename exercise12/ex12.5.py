import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

doc = ''
while True:
    data = mysock.recv(1024)
    if len(data) < 1:
        break
    doc = doc + data.decode()
    # if '\r\n\r\n' in doc:
    #     print('hello')
    # print(data.decode(),end='')

sub = '\r\n\r\n'
# print doc AFTER these 4 characters
index = doc.find(sub) + 4

print(doc[index:])

mysock.close()

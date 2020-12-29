import socket

link = input('Enter Web Address: ')
hostname = link.split('/')[0]

print(hostname)

# create an INET, STREAMing socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # now connect to the web server on port 80 - the normal http port
    mysock.connect((hostname, 80))
except:
    print('not a web address')
    quit()

cmd = ('GET http://' + link + ' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

# empty string to store received data
document = ''
while True:
    data = mysock.recv(1024)
    if (len(data) < 1):
        break
    # bytes in data decoded to string and concat
    document = document + data.decode()
mysock.close()

print(document[:3000])
# print(len(document[:300]))

# GET http://data.pr4e.org/romeo.txt HTTP/1.0
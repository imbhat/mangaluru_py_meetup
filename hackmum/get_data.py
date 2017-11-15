import time
import socket


def get(path):
    s = socket.socket()
    s.connect(('localhost', 5000))

    request = 'GET %s HTTP/1.1\r\n\r\n' % path
    s.send(request.encode())

    chunks = list()
    while True:
        chunk = s.recv(4000)
        if chunk:
            chunks.append(chunk)
            continue
        break 

    data = b''.join(chunks).decode()
    return data


def main():
    start = time.time()
    data = get('/index')
    end1 = time.time()
    data = get('/read')
    end2 = time.time()
    print('First Task ran in %.2f seconds' % (end1 - start))
    print('Second Task ran in %.2f seconds' % (end2 - end1))
    print('Both Task ran in %.2f seconds' % (end2 - start))

main()

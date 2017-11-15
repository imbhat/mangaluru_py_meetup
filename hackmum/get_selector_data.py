import time
import socket
from selectors import EVENT_WRITE, EVENT_READ, DefaultSelector

selector = DefaultSelector()
n_jobs = 0

def get(path):
    global n_jobs
    n_jobs += 1
    s = socket.socket()
    s.setblocking(False)
    try:
        s.connect(('localhost', 5000))
    except BlockingIOError:
        pass

    callback = lambda: connected(s, path)
    selector.register(s.fileno(), EVENT_WRITE, data=callback)

def connected(s, path):
    chunks = list()
    request = 'GET %s HTTP/1.1\r\n\r\n' % path
    selector.unregister(s.fileno())
    s.send(request.encode())
    print("Connected to %s!" % path)
    selector.register(s.fileno(), EVENT_READ, data=lambda: readable(s, chunks))

def readable(s, chunks):
    global n_jobs

    chunk = s.recv(4096)
    if chunk:
        chunks.append(chunk)
    else: 
        selector.unregister(s.fileno())
        data = b''.join(chunks).decode()
        s.close()
        n_jobs -= 1
        print("This is data: %s" % data)
   

def main():
    global n_jobs
    start = time.time()
    get('/index')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
    get('/index')
    get('/read')
   
    while n_jobs:
        events = selector.select()
        for key, mask in events:
            callback = key.data
            callback()
    end2 = time.time()
    print('Task ran in %.3f seconds' % (end2 - start))

main()

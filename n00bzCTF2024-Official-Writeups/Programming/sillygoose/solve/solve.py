from pwn import *

p = process("python3 sillygoose.py".split())
l = 0
r = pow(10, 100)

def largeNumToString(n):
    ans = ""
    while n:
        ans = str(n % 10) + ans
        n //= 10
    return ans

while True:
    m = (l + r + 1) // 2
    p.sendline(largeNumToString(m).encode())
    res = p.recvline()
    if b'large' in res:
        r = m - 1
    elif b'small' in res:
        l = m + 1
    else:
        print(res)
        print(p.recvline())
        break

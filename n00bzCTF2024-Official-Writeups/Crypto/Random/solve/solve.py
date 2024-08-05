from pwn import *

n = 10

sample = ''

for i in range(n):
    sample += chr(ord('0') + i)

io = process('./server')
io.sendline(sample.encode())
scrambledsample = io.readline().decode('utf-8').strip()

io.close()

ans = [''] * n

for i in range(n):
    ans[ord(scrambledsample[i]) - ord('0')] = sample[i]

io = process('./server')
io.sendline(''.join(ans).encode())
io.readline()
print(io.read())

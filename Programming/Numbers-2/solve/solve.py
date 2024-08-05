from pwn import *
import math
import sympy
io = process('../src/chall.py')
for i in range(1,102):
	print(i,end='\r')
	if i == 101:
		io.interactive() # Get your flag!
	io.readuntil(b':')
	io.readline()
	to_solve = io.readuntil(b':')

	# Prime factors solve
	if b'prime' in to_solve:
		number = int(to_solve[37:len(to_solve)-1].decode())
		ans = sympy.primefactors(number)[-1]
		io.sendline(str(ans).encode())
		continue

		# Least common multiple solve
	elif b'least' in to_solve:
		x = int(to_solve[37:len(to_solve)-1].decode().split(' ')[0])
		y = int(to_solve[37:len(to_solve)-1].decode().split(' ')[2])
		ans = math.lcm(x,y)
		io.sendline(str(ans).encode())
		continue

		# Greatest common divisor solve
	elif b'divisor' in to_solve:
		x = int(to_solve[39:len(to_solve)-1].decode().split(' ')[0])
		y = int(to_solve[39:len(to_solve)-1].decode().split(' ')[2])
		ans = math.gcd(x,y)
		io.sendline(str(ans).encode())
		continue		

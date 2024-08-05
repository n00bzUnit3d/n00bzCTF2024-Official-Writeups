#!/usr/bin/env python3
import random
import math
import sympy
import time
print("Welcome to Numbers 2! Time to step up the game...")
start_time=int(time.time())
choice = ["prime factor","greatest common divisor","least common multiple"]
for i in range(1,101):
	time_taken = int(time.time()) - start_time
	if time_taken > 45:
		print("You took too long!")
		exit(0)
	print(f"Current round: {i} of 100")
	current_choice=random.choice(choice)
	if "common" in current_choice:
		x,y = random.randint(1,100+(100*i)),random.randint(1,100+(100*i))
		guess = int(input(f"Give me the {current_choice} of {x} and {y}: "))
		if "divisor" in current_choice:
			ans = math.gcd(x,y)
			if ans != guess:
				print("Wrong!")
				exit(0)
			elif ans == guess:
				print("Correct!")
				continue
		elif "least":
			ans = math.lcm(x,y)
			if ans != guess:
				print("Wrong!")
				exit(0)
			elif ans == guess:
				print("Correct!")
				continue


	else:
		x = random.randint(0,100+(100*i))
		guess = int(input(f"Give me the greatest {current_choice} of {x}: "))
		ans = sympy.primefactors(x)[-1]
		if ans != guess:
			print("Wrong!")
			exit(0)
		elif ans == guess:
			print("Correct!")
			continue

print(f"Good job! Here's your flag: {open('/flag.txt').read()}")

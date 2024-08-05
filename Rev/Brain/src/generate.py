import sympy
flag="n00bz{1_c4n_c0d3_1n_br41nf*ck!}"
# flag=""
bf_code=""
for i in flag:
	good_factors=[]
	factors=sympy.divisors(ord(i))
	if len(factors)%2==0:
		good_factors=[factors[int(len(factors)/2)]]
		good_factors.append(int(ord(i)/good_factors[0]))
		x="+"*good_factors[0]
		y="+"*good_factors[1]
		bf_code+=f">{x}[<{y}>-]<[-]"
	elif len(factors)%2!=0:
		good_factors=[factors[int(len(factors)/2)]]
		good_factors.append(int(ord(i)/good_factors[0]))
		x="+"*good_factors[0]
		y="+"*good_factors[1]
		bf_code+=f">{x}[<{y}>-]<[-]"

print(bf_code)
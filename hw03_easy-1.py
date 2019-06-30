def my_round(number, ndigits): 
	number = number*(10**ndigits) 
	number = number//1 
	return number/(10**ndigits) 
print(my_round(3.141592653589793238462643383279502884197, 2)) 
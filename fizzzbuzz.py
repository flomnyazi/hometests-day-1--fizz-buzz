def fizz_buzz(x):
	'''This is a function fizz_buzz that checks  divisiblity of a number x
	'''

 	if (x % 5==0) and (x %3 ==0):
 		return "FizzBuzz"
 		'''This function returns fizz_buzz when a number x is divisible by both 3 and 5'''
 	elif  x%5 ==0:
 		return "Buzz"
 	elif  x%3==0:
 		return "Fizz"
 	else:
 		return x

print (fizz_buzz(300))

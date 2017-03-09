def fizz_buzz(x):
	'''This is a function fizz_buzz that checks  divisiblity of a number x
	'''

 	if (x % 5==0) and (x %3 ==0):
 		return "FizzBuzz"
 		'''This function returns fizz_buzz when a number x is divisible by both 3 and 5'''
 	elif  x%5 ==0:
 		return "Buzz"
 		'''Function returns Buzz if number is divisible by 5'''

 	elif  x%3==0:
 		return "Fizz"
 		'''Function returns Fizz if number is divisible by 3'''
 	else:
 		return x
 		'''Function returns the number if not divisible by either  3, 5 or both 3 nad 5'''

print (fizz_buzz())

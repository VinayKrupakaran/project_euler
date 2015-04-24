#!/usr/bin/env python

#This program computes the largest palindrome made from the product 
#of two 3-digit numbers

def check_palin(num):
#This function checks if a number is a palindrome
	num_str = str(num) #convert the number to a string
	num_str = num_str[::-1] #reverse the string
	if num == int(num_str):
		return True

def main():
#Main function
	largest = limit = 0
	n1 = 0
	i = j = 999
	for i in xrange(999, 100, -1):
		for j in xrange(999, 100, -1):
			prod = i * j
			check = check_palin(prod)
			if check == True:
				if prod > largest:
					largest = prod
					limit = j
					n1 = i
					break
		if i < limit:
			break
	print '%d is the largest palindrome product with factors %d and %d' %(largest, n1, limit)

main()

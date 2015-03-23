#This program computes the difference between the sum of the squares and the square of the sum
#of the first one hundred natural numbers 

def Prob_6():
	sum_sq = sum_i = 0

	for i in xrange(1, 101):
		sum_sq += i * i
		sum_i += i

	#The problem can also be solved by using standard formulae:
	# sum of (1^2 + 2^2... n^2) = (n * n+1 * 2n + 1)/6
	# sum of (1 + 2... n) = (n * n+1)/2
	#n = 100
	#sum_sq = (n * (n+1) * ((2*n) + 1))/6
	#sum_i = (n * (n + 1))/2

	print '%d and %d are the square and normal sums' %(sum_sq, sum_i * sum_i)
	d = (sum_i*sum_i) - sum_sq
	print '%d is the difference' %d

sum_sq()

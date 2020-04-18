#!/usr/bin/env python3
# Daniel Schlicht - Cryptography Project 3
# linear_approx.py

sboxIn  = [0, 1, 2, 3, 4, 5, 6, 7]
sboxOut = [6, 5, 1, 0, 3, 2, 7, 4]
size = len(sboxIn)

# Calculates the normalized linear approximation N_L
def linearApprox(inputSum, outputSum):
	# keeps track of when X == Y
	total = 0;

	# iterate through the sbox
	for i in range(size):
		# mask the current row with the input/output sums to isolate
		# the bits you want to compare
		curInput = sboxIn[i] & inputSum
		curOutput = sboxOut[i] & outputSum
		
		# tally the '1's in each % 2, equivalent to XOR
		inVal = bin(curInput).count("1") % 2
		outVal = bin(curOutput).count("1") % 2
		
		# check if input and output are the same
		if inVal == outVal:
			total += 1
			
	# normalize the value of total
	total = total - size//2
	
	# add plus signs and space for formatting
	if total > 0:
		total = "+" + str(total)
	if total == 0:
		total = " " + str(total)
	
	return str(total)

# Print the table 
print("Normalized Linear Approximation Table: ")
print("   |", end="")
for i in range(size):
	print("  %d " %(i), end="")
print()
print("----" * len(sboxIn) + "---")
for row in range(size):
	print(" %d |" %(row), end="")
	for col in range(size):
		print(" " + linearApprox(row, col) + " ", end="")
	print("")
		

		
			
		
		
		
		
		
		
		
		
			

		
		
		

		
		
		
		

'''
# Determines the linear approximation given the input sum and output sum
def linearApprox(inSum, outSum):
		total = 0  # keep track of all 'yes's'
		# Go through the input and output table and xor the bits being compared
		for i in range(size):
			# Mask so we're only looking at the right bits
			inBits = sboxIn[i] & inSum
			outBits = sboxOut[i] & outSum
			# Xor them and tally if 0
			if(inBits ^ outBits == 0):
				total += 1
		# Normalize the approximations 
		#total = total - size//2		
		#if(total > 0):
			#total = "+" + str(total)
		#if(total == 0):
		#	total = " " + str(total)
			
		return str(total)
'''
'''	
# Build the table and print it
print("   | ", end=" ")
for i in range(size):
	print("  %d " %(i), end="")
print("")
print("-" * (len(sboxIn) * 4 + 5))
for row in range(size):
	print("   %d | " %(row), end="")
	for col in range(size):
		print(" " + linearApprox(row, col) + " ", end="")
	print("")
'''	
	



#!/usr/bin/python3

# Index is modulus_x, location is a list of primitive roots for modulus_x. 

# Implement a dictionary rather than a list (saves space because large primes become sparse). 

prim_roots_table = dict() # Currently table works up till prime 29.

prim_roots_table = {
	3: [2], 
	5: [2, 3], 
	7: [3, 5], 
	11: [2, 6, 7, 8],
	13: [2, 6, 7, 11],
	17: [3, 5, 6, 7, 10, 11, 12, 14],
	19: [2, 3, 10, 13, 14, 15],
	23: [5, 7, 10, 11, 14, 15, 17, 19, 20, 21],
	29: [2, 3, 8, 10, 11, 14, 15, 18, 19, 21, 26, 27],
	}

if __name__ == "__main__":
	print(prim_roots_table)
#!/usr/bin/python3

# my_mod_toolkit is a toolkit that needs to be developed. 
# prim_roots_table 
from my_mod_toolkit import prim_roots_table
import math
import re
from PrimitiveRoots import what_root_which_power
import numpy

def parse(problem_statement):
    # Parse strings like 'x^4 = 3 in Z/23Z'
    match = re.search(r"x\^(\d+)\s*=\s*(\d+)\s*in\s*Z/(\d+)Z", problem_statement)
    if not match:
        raise ValueError("Invalid format. Expected 'x^a = b in Z/mZ'")
    # Each gets turned from a string to an integer
    # Use tuple() because cannot assign map object to three vars
    x_power, quotient, modulus_x = tuple(map(int, match.groups()))
    return x_power, quotient, modulus_x

# Parse the input, get the ints stored. 
# x_power, quotient, modulus_x = parse('x^4 = 3 in Z/23Z')
# x_power = 4, quotient = 3, modulus_x = 23

# Check Primitive roots from table, get a list
# The (small) table works for primes 3 to 29 (TODO: increase table size)
# primitive_roots = my_mod_toolkit.prim_roots_table[modulus_x]
# primitive_roots = [5, 7, 10, 11, 14, 15, 17, 19, 20, 21]

# The program gets all root_power pairs under the cap tested, and increase the cap if empty, up till cap_of_cap, the absolute max you want the computer to test up to. 
def root_power_pairs(quotient, modulus_x, primitive_roots, cap = 30, cap_of_cap = 3*10**12):
    # Use the primitive root solver (written and tested) to get a good pair. Run with a higher cap each time if empty, until cap = 3*10**12 (customizable)
    # Start from cap = 30 (customizable)
    # cap = 30
    root_power_pairs = []
    while cap <= cap_of_cap:
        root_power_pairs = what_root_which_power(quotient, modulus_x, cap, primitive_roots)
        # Increase the cap if empty
        if len(root_power_pairs) == 0:
            # Increase by multiplying by 10
            cap *= 10
            continue
        return root_power_pairs
    # Now len(root_power_pairs) == 0 is still True, not found a pair. Will return error 
    print("Cannot find a suitable (root, power) pair. Try increasing cap_of_cap beyond the default 3*10**12. ") 
    return root_power_pairs
        
# pick_one_root_power_pair returns the pair with the smallest result = root**power. 
# root_power_pairs == [(7, 2), (19, 4)] with cap == 3000000
def pick_one_root_power_pair(root_power_pairs):
    # See which root_power_pairs is the smallest when root raised to the power (easier for handsolving onward). 
    root_power_pair_results = []
    # For each (root, power) pair in root_power_pairs, get the result of root**power, store in THE list (root_power_pair_results), 
    # root == 7, power == 2 in root_power_pairs == [(7, 2), (19, 4)]:
    for root, power in root_power_pairs:
        # root_power_pair_results.append(7 ** 2)
        root_power_pair_results.append(root ** power)
    # root == 19, power == 4 in root_power_pairs == [(7, 2), (19, 4)]:
        # root_power_pair_results.append(19 ** 4)
    # root_power_pair_results == [49, 130321]

    # get the argmin which is the index of the min element. That'll be the one. 
    # argmin takes a list, not the min value, because argmin finds the min then the index. 
    # index points to the int = root**power inside root_power_pair_results, but also points to the (root, power) pair in root_power_pairs. Orders are preserved. 
    # min_index = argmin(root_power_pairs, key = eval(root_power_pairs[i][0] ** root_power_pairs[i][1]))
    # min_index == numpy.argmin([49, 130321])
    # min_index == 0
    min_index = numpy.argmin(root_power_pair_results)
    # with the min root ** power, the index corresponds to the best choice for handsolving onward. 
    # list[index] gives content, which is a (root, power) pair
    # root_power_pairs[min_index = 0] == (7, 2)
    # return (7, 2)
    return root_power_pairs[min_index]

# Too complicated, no longer used; outline is in main()
# # Assume processed exponent equation in main()
# # modulus_y = modulus_x - 1
# # quotient_exp is the chosen power of the chosen primitive root
# # divisor_exp is the (x_power * y)
# def solve_with_exponents(divisor_exp, quotient_exp, modulus_y):
#     upstairs_modulus_y = modulus_y
#     # See if we can divide all of divisor, quotient, and modulus by some num. 
#     # TODO: Check if cd also works
#     # math.gcd(a,b) works.
#     gcd_divisor_modulus = math.gcd(divisor_exp, modulus_y)
    
#     # TODO: Check if the step below may sometimes be needed be done more than once. If so, must update gcd_divisor_modulus or make some other variable that keeps track of the total_downstairing_divisor, which we must multiply back in the end to enlarge the possibilites of ys. 
#     # divisor_exp, quotient_exp, and modulus_y and gcd_divisor_modulus can change. They are recoverable from their later values by multiplying back total_downstairing_divisor
    
#     total_downstairing_divisor = 1
    
#     # May run just one time, but set up such that it can run several times. 
#     # if gcd_divisor_modulus | quotient_exp:
#     while quotient_exp % gcd_divisor_modulus == 0:
#         total_downstairing_divisor *= gcd_divisor_modulus
#         # We can divide all three. 
#         divisor_exp //= gcd_divisor_modulus
#         quotient_exp //= gcd_divisor_modulus
#         modulus_y //= gcd_divisor_modulus
#         gcd_divisor_modulus = math.gcd(divisor_exp, quotient_exp)
#         # What do we need to reassign if looping back?
#         # quotient_exp, gcd_divisor_modulus at least; then total_downstairing_divisor too; 
    
    
        
#     # TODO: if the gcd(divisor_exp, modulus_y) == quotient_exp, then divide all three (divisor, modulus, quotient) by gcd(divisor, modulus), reducing the complexity, ensuring invertibility of the divisor (must be coprime with the modulus), and ensuring uniqueness of quotient_exp in the following few steps by downstairing. 
    
#     # Invert divisor
#     inverse_divisor = inverse_finder_mod(divisor, modulus_y)
    
#     # Multiplying inverse of divisor to both sides, 
#     # LHS becomes one (divisor times inverse of divisor in mod modulus_y),
#     divisor_exp = 1
#     # quotient becomes some num
#     quotient_exp *= inverse_divisor 
    
#     # Process the quotient: be 0 ≤ quotient < modulus_y
#     quotient_exp %= modulus_y
    
#     downstairs_quotient_exp = quotient_exp
#     downstairs_y = downstairs_quotient_exp
    
#     downstairs_modulus_y = modulus_y
    
#     # TODO: Going upstairs again, multiplying all three (divisor, quotient, modulus) by the number we divided it by
#     # Expand the possibilities of ys when upstairing
#     # divisor_exp *= total_downstairing_divisor
#     # quotient_exp *= total_downstairing_divisor
#     # modulus_y *= total_downstairing_divisor
    
#     # But the above step can be skipped, because we only need the upstairs_ys. 
#     # upstairs_modulus_y = modulus_y * total_downstairing_divisor is not needed because upstairs_modulus_y was stored at the beginning
    
#     upstairs_ys = upstairing_mod(downstairs_y, downstairs_modulus_y, upstairs_modulus_y)
    
#     # ys is a list of solved y-vals
#     return upstairs_ys
    
# inverse_finder_mod(divisor = 2, modulus_y = 11)
def inverse_finder_mod(divisor, modulus_y):
    # If multiplying two numbers returns 1 modulus_y, 
    # Then they are inverses of each other. 
    # For example, 2 * 2 = 1 mod 3, got 1. This means 2 and 2 are inverses mod 3. 
    # For each nonzero number in modulus_y, up till modulus_y, noninclusive
    # for num_in_modulus_y in range(1, modulus_y = 11):
    # for num_in_modulus_y in [1, 2, ..., 9, 10]:
    # for num_in_modulus_y == 1:
    for num_in_modulus_y in range(1, modulus_y):
        # num_in_modulus_y is multiplied by the divisor
        # Then modded to see if 1 is the result
        # if (num_in_modulus_y = 1 * divisor = 2) % (modulus_y = 11) == 1:
        # if 2 % 11 == 1:
        # if 2 == 1:
        # if False:
        # skip this iteration
        if (num_in_modulus_y * divisor) % modulus_y == 1:
            # If product == 1, then num_in_modulus_y is the inverse of divisor.
            inverse = num_in_modulus_y
            return inverse
    # for num_in_modulus_y == 2: # if False
    # for num_in_modulus_y == ...: # if False
    # for num_in_modulus_y == 6: # if False
        # if (num_in_modulus_y = 6 * divisor = 2) % (modulus_y = 11) == 1:
        # if (6 * 2) % 11 == 1:
        # if 12 % 11 == 1:
        # if 1 == 1:
        # if True:
            # inverse = num_in_modulus_y == 6
            # inverse = 6
            # return inverse == 6
            # return 6
# Summary: inverse_finder_mod(divisor = 2, modulus_y = 11) -> return inverse == 6
    
# Every nonzero num in a prime modulus must have an inverse, so no need to worry about the case where an inverse is not found. 

# Equivalence class in current mod,
# Captured in a larger mod. 
# Go upstair,
# class gets large, 
# each val is the same,
# back when they were downstairs.
# 6 mod 11 becomes 6 mod 22 and 17 mod 22 after "upstairing".
# When you “upstairs” from mod 11 to mod 22, every residue mod 11 corresponds to two residues mod 22 that differ by 11.
# upstairing_mod(y = 6, downstairs_modulus_y = 11, upstairs_modulus_y = 22)
def upstairing_mod(y, downstairs_modulus_y, upstairs_modulus_y):
    # val is single int, in the downstairs_modulus_y, the smaller quotient space
    
    # vals is list of ints
    ys = []
    # while y = 6 < upstairs_modulus_y = 22:
    # while 6 < 22:
    # while True:
    while y < upstairs_modulus_y:
        # ys.append(y = 6)
        # ys.append(6)
        # ys == [6]
        ys.append(y)
        # y += downstairs_modulus_y == 11
        # y += 11
        # y == 17
        y += downstairs_modulus_y
    # while y = 17 < upstairs_modulus_y = 22:
    # while 17 < 22:
    # while True:
        # ys.append(y = 17)
        # ys.append(17)
        # ys == [6, 17]
        # y += downstairs_modulus_y == 11
        # y += 11
        # y == 28
    # while y = 28 < upstairs_modulus_y = 22:
    # while 28 < 22:
    # while False:
        # break loop
    # these are the y values in upstairs_modulus_y so the larger quotient space
    # ys == [6, 17]
    return ys

# ys == [6, 17]
# csv == '6, 17'
def list_to_csv(ys):
    csv = ''
    # for 6 in [6]
    for y in ys[:-1]:
        # csv = '' + '6' == '6'
        csv += str(y)
        # csv = '6' + ', ' == '6, '
        csv += ', '
    # csv = '6, ' + '17' == '6, 17'
    csv += str(ys[-1])
    # csv == '6, 17'
    return csv

    
# ys is a list of y-vals, returned by solve_with_exponents
# get x = g**y. (in writing)
# g is the root found with pick_one_root_power_pair; first place in the tuple returned, so root_power_pairs[min_index][0]
# This modulus is the original modulus in the problem statement (Ex. 23 in x^4 = 3 mod 23), not the y-modulus, which is (23 - 1). 
def y_to_x(ys, root):
    xs_without_mod = [root**y for y in ys]
    return xs_without_mod
    
def x_to_x_mod(xs_without_mod, modulus_x):
    # Some xs are very big, over the modulus, so find the remainder at this mod. 
    # In handwriting, decompose the exponents with rules, 
    # but in code, computer is quick, so no need. 
    
    xs_mod = [x_without_mod % modulus_x for x_without_mod in xs_without_mod]
    # Modded x's
    return xs_mod

# x = root^y mod modulus_x, returned the optimized way. 
# ys a list of y
# root is the chosen primitive root
# modulus_x is in the question statement
# xs_mod = y_to_x_mod(ys = [6, 17], root = 7, modulus_x = 23) == [4, 19]
def y_to_x_mod(ys, root, modulus_x):
    # This step is optimized compared to y_to_x. Mod each time raising a power is better. 
    # (Don't calculate a huge number which then you mod separately.)
    xs_mod = []
    # each x = root ** each y
    # for 6 in [6, 17]:
    for y in ys:
        x = 1
        # root ** each y becomes two steps: (for in range(y))
        # for _ in range(6) == do this 6 times
        for _ in range(y):
            # -- 1 --
            # Step 1: multiply by the root
            # x *= 7 == 7
            x *= root
            # Step 2: mod by the modulus
            # x %= 23 == 7
            x %= modulus_x
            # -- 2 --
            # x *= 7 == 49
            # x %= 23 == 3
            # -- 3 --
            # x *= 7 == 21
            # x %= 23 == 21
            # -- 4 --
            # x *= 7 == 147
            # x %= 23 == 9
            # -- 5 --
            # x *= 7 == 63
            # x %= 23 == 17
            # -- 6 --
            # x *= 7 == 119
            # x %= 23 == 4
        # each x is then appended to xs_mod. Order preserved. 
        # xs_mod.append(4)
        xs_mod.append(x)
        # xs_mod == [4]
    # for 17 in [6, 17]:
        # x = 1
        # root ** each y becomes two steps: (for in range(y))
        # for _ in range(17) == do this 17 times
        # for _ in range(y):
            # -- 1 --
            # x *= 7 == 7
            # x %= 23 == 7
            # -- 2 --
            # x *= 7 == 49
            # x %= 23 == 3
            # -- 3 --
            # x *= 7 == 21
            # x %= 23 == 21
            # -- 4 --
            # x *= 7 == 147
            # x %= 23 == 9
            # -- 5 --
            # x *= 7 == 63
            # x %= 23 == 17
            # -- 6 --
            # x *= 7 == 119
            # x %= 23 == 4
            # -- 7 --
            # x *= 7 == 28
            # x %= 23 == 5            
            # -- 8 --
            # x *= 7 == 35
            # x %= 23 == 12
            # -- 9 --
            # x *= 7 == 84
            # x %= 23 == 15          
            # -- 10 --
            # x *= 7 == 105
            # x %= 23 == 13
            # -- 11 --
            # x *= 7 == 91
            # x %= 23 == 22            
            # -- 12 --
            # x *= 7 == 154
            # x %= 23 == 16
            # -- 13 --
            # x *= 7 == 112
            # x %= 23 == 20                
            # -- 14 --
            # x *= 7 == 140
            # x %= 23 == 2
            # -- 15 --
            # x *= 7 == 14
            # x %= 23 == 14            
            # -- 16 --
            # x *= 7 == 98
            # x %= 23 == 6
            # -- 17 --
            # x *= 7 == 42
            # x %= 23 == 19             
        # each x is then appended to xs_mod. Order preserved. 
        # xs_mod.append(19)
        # xs_mod == [4, 19]
        
    # Double for loop is better than large numbers.
    # These are already modded each step. 

    # xs_mod == [4, 19]
    return xs_mod
    
# Having xs_mod, we print nicely. 
# x mod modulus_x as requested. 
def print_solutions(xs_mod, modulus_x):
    print("Solutions of x:")
    for x_mod in xs_mod:
        print(f'{x_mod} mod {modulus_x}')

# One complete run: 
# x^4 = 3 mod 23
# 7^4y = 7^2 mod 23 
# mod x -> y
# 4y = 2 mod 22
# downstaring
# 2y = 1 mod 11
# gcd(2, 11) = 1
# 6 is the inverse of 2 in mod 11
# y = 6 mod 11
# upstairing
# y = 6, 17 mod 22
# mod y -> x
# x = 7^6, 7^17 mod 23
# Simplify
# x = 4, 19 mod 23

def main():
    # x^4 = 3 mod 23
    problem_statement = input('Input your problem statement exactly in the format of x^a = b in Z/mZ; (Ex. x^4 = 3 in Z/23Z).  Regular expressions automatically match your numbers. Only support prime moduli between and include 3 to 29.\n')
    # All integers stored, already converted in parse()
    # x_power, quotient, modulus_x = (4, 3, 23)
    # x_power == 4, quotient == 3, modulus_x == 23
    x_power, quotient, modulus_x = parse(problem_statement)
    
    # Get a list of primitive_roots for this modulus_x. prim_roots_table is a list
    # primitive_roots = prim_roots_table[modulus_x = 23]
    # primitive_roots == [5, 7, 10, 11, 14, 15, 17, 19, 20, 21]
    primitive_roots = prim_roots_table[modulus_x] 
    # Find the best root, power pair that equals the quotient, for handsolving (smallest result)
    # root, power = pick_one_root_power_pair(root_power_pairs(quotient = 3, modulus_x = 23, primitive_roots = [5, 7, 10, 11, 14, 15, 17, 19, 20, 21]))
    # root, power = pick_one_root_power_pair(root_power_pairs = [(7, 2), (19, 4)])
    # root, power = (7, 2) the smallest in product
    # root == 7, power == 2
    root, power = pick_one_root_power_pair(root_power_pairs(quotient, modulus_x, primitive_roots))
    
    # 7^4y = 7^2 mod 23
    # 'Rewrote problem statement as: \n 7^(4y) = 7^2 (mod 23)')
    # Rewrote problem statement as: 
    # 7^(4y) = 7^2 (mod 23)
    print(f'Rewrote problem statement as:\n{root}^({x_power}y) = {root}^{power} (mod {modulus_x})')
    
    # modulus_y == 22 = 23 - 1
    modulus_y = modulus_x - 1
    
    # mod x -> y
    # 4y = 2 mod 22
    # 'Exponent equality: 4y = 2 (mod 22)'
    print(f'Exponent equality: {x_power}y = {power} (mod {modulus_y})')
    
    # downstaring
    # downstaring_factor = gcd(4, 22) == 2
    downstaring_factor = math.gcd(x_power, modulus_y)
    
    # power is quotient. math.gcd(x_power, modulus_y) should divide power. 
    # downstaring_factor is the gcd. 
    # If gcd doesn't divide power then the original equation has no solution. 
    # return 'no solution' with an explanation
    # 'gcd(x_power, modulus_x - 1) which is {downstaring_factor} does not divide the power {power} to which the primitive root {root} is raised.' 
    # The 
    # Represent doesn't divide: 
    # downstaring_factor doesn't divide power => power cannot be divided by the downstaring_factor without a remainder => there'll be remainders. 
    # if power / downstaring_factor != power // downstaring_factor:
    # If remainder is not zero: downstaring_factor does not divide power. 
    # if power == 2 % downstaring_factor == 2 != 0:
    # if 2 % 2 != 0:
    # if 0 != 0:
    # if False:
    # skip to else:
    if power % downstaring_factor != 0:
        # No solution
        print(f'No solution. gcd(x_power = {x_power}, modulus_x - 1 = {modulus_y}) == {downstaring_factor} ∤ {power} (the power to which the primitive root ({root}) is raised).' )
        return 
    # Remainder is zero, downstaring_factor does divide power, has solutions. 
    # The solution count equals the downstaring_factor. 
    # 'Has solutions. gcd(x_power = 4, modulus_x - 1 = 22) == 2 | 2 (the power to which the primitive root (7) is raised).'
    else:    
        print(f'Has solutions. gcd(x_power = {x_power}, modulus_x - 1 = {modulus_y}) == {downstaring_factor} | {power} (the power to which the primitive root ({root}) is raised).')
    
    # x_power = 4 // 2 == 2
    x_power //= downstaring_factor
    # power = 2 // 2 == 1
    power //= downstaring_factor
    # modulus_y = 22 // 2 == 11
    downstairs_modulus_y = modulus_y // downstaring_factor
    
    # Changed from 4y = 2 mod 22
    # Each term interger-divided by downstaring_factor
    # Downstaired equality: {x_power = 2}y = {power = 1} (mod {downstairs_modulus_y = 11})
    # Downstaired equality: 2y = 1 (mod 11)
    print(f'Downstaired equality: {x_power}y = {power} (mod {downstairs_modulus_y})')
    
    # Verify x_power and modulus_y are coprime (x_power can be inverted in modulus_y)
    # assert gcd(2, 11) == 1
    # assert 1 == 1
    # assert True
    assert math.gcd(x_power, downstairs_modulus_y) == 1
    # No AssertionError
    # 'gcd(x_power = {x_power = 2}, downstairs_modulus_y = {downstairs_modulus_y = 11}) == 1'
    # 'gcd(x_power = 2, downstairs_modulus_y = 11) == 1'
    print(f'gcd(x_power = {x_power}, downstairs_modulus_y = {downstairs_modulus_y}) == 1')
    print(f'x_power and downstairs_modulus_y are verified to be coprime.')
    # 'Thus, x_power can be inverted in downstairs_modulus_y; {x_power = 2} modulo {downstairs_modulus_y = 11} has an inverse.'
    # 'Thus, x_power can be inverted in downstairs_modulus_y; 2 modulo 11 has an inverse.'
    print(f'Thus, x_power can be inverted in downstairs_modulus_y; {x_power} modulo {downstairs_modulus_y} has an inverse.')
    
    # find inverse
    # # inverse = inverse_finder_mod(x_power = 2, downstairs_modulus_y = 11) == 6
    # inverse = inverse_finder_mod(2, 11) == 6
    inverse = inverse_finder_mod(x_power, downstairs_modulus_y)
    
    # '{inverse = 6} is the inverse of {x_power = 2} modulo {downstairs_modulus_y = 11}, so multiply {inverse = 6} to each side; y will have coefficient 1.
    # 6 is the inverse of 2 modulo 11, so multiply 6 to each side; y will have coefficient 1.
    print(f'{inverse} is the inverse of {x_power} modulo {downstairs_modulus_y}, so multiply {inverse} to each side; y will have coefficient 1.')
    
    # isolate y (multiply each side by the inverse)
    # y = 6 mod 11
    # x_power = 2 * 6 mod 11 == 1 (Always gets inverted back to 1)
    x_power = 1 
    # power *= inverse == 1 * 6 == 6
    power *= inverse
    # power == 6 % 11 == 6
    power %= modulus_y
    # 'Inverted-the-divisor downstairs equality: y = {power = 6} (mod {downstairs_modulus_y = 11})'
    # Inverted-the-divisor equality: y = 6 (mod 11)
    print(f'Inverted-the-divisor downstairs equality: y = {power} (mod {downstairs_modulus_y})')
    
    # upstairing, get ys
    # y = 6, 17 mod 22
    # upstairs_modulus_y = 11 * 2 == 22
    upstairs_modulus_y = downstairs_modulus_y * downstaring_factor
    # possibly redundant: 
    modulus_y = upstairs_modulus_y
    # downstairs_modulus_y == 11
    # ys = upstairing_mod(6, 11, 22) == [6, 17]
    ys = upstairing_mod(power, downstairs_modulus_y, upstairs_modulus_y)
    # Process ys as a string to print nicely
    # ys_string =  list_to_csv([6, 17]) == '6, 17'
    ys_string = list_to_csv(ys)
    
    # Upstaired equality: y = {power} (mod {upstairs_modulus_y})
    print(f'Upstaired equality: y = {ys_string} (mod {upstairs_modulus_y})')
    
    # mod y -> x
    # ys to xs
    # x = 7^6, 7^17 mod 23
    # xs_exp_form == ['7^6' '7^17']
    xs_exp_form = [f'{root}^{y}' for y in ys]
    # xs_exp_form_string = '7^6, 7^17'
    xs_exp_form_string = list_to_csv(xs_exp_form)
    # Solutions of x: x = 7^y = 7^6, 7^17 (mod 23)
    print(f'Unsimplified solutions of x: x = {root}^y = {xs_exp_form_string} (mod {modulus_x})')
    
    # xs_mod = y_to_x_mod([6, 17], 7, 23) == [4, 19]
    xs_mod = y_to_x_mod(ys, root, modulus_x)
    
    # # For demonstration purpose: split into two steps (not optimum)
    # # xs = y_to_x([6, 17], 7) == [7 ** 6, 7 ** 17] == [117649, 232630513987207]
    # # TODO: Optimize by combining with the mod step to prevent overflowing (but little worry about this)
    # xs = y_to_x(ys, root)
    #
    # # Simplify
    # # xs then to xs_mod, which fit inside 0 ≤ xs_mod ≤ modulus_x
    # # x = 4, 19 mod 23
    # # xs_mod = x_to_x_mod([117649, 232630513987207], 23) == [4, 19]
    # xs_mod = x_to_x_mod(xs, modulus_x)
    
    # Print solutions in the format of '{x_mod} mod {modulus_x}' 
    # like '7 mod 23'
    # xs_mod_strings = list_to_csv([4, 19]) == '4, 19'
    xs_mod_strings = list_to_csv(xs_mod)
    # Final solutions: x = 4, 19 (mod 23)
    print(f'Simplified solutions of x: x = {xs_mod_strings} (mod {modulus_x})')
    
if __name__ == "__main__":
    main()

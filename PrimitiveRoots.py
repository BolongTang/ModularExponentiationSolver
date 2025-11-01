def what_root_which_power(quotient = 6, modulus = 7, cap = 3000, primitive_roots = [3,5]):
    # quotient = 10, modulus = 11, cap = 3000, primitive_roots = [2,6,7,8]
    # For x ** 9 = 6 mod 7,
    # 6 is quotient
    # 7 is modulus
    # primitive roots are 3, 5
    # 3 as base works, because 3 ** 3 = 27 equals to 6 mod 7 == 27 mod 7. 
    # Thus x = 3 ** y, x ** 9 = 3 ** (9 * y)
    # GOAL: find a power of one of the the primitive roots that match the 
    # rewrite of the quotient according to the modulus
    # If primitive roots are (2, 6, 7, 8), a rewrite of 32 = 2 ** 5 works because 2 in roots and 2 is base. 

    # Rewrite of the quotient according to the modulus. Rewrite 10 mod 11 becomes 10 + 11k. 
    # quotient = 10 # Customizable
    # modulus = 11 # Customizable
    # quotient_rewrites = [] # Rewritten quotient
    # cap = 3000 # Search up till this number, capping both the rewrite and the powers of the roots. 

    # Below the cap, go up. Rewrite it with modulus, each time adding one. 10 mod 11 becomes 21 mod 11.
    # while quotient < cap:
    #     quotient_rewrites.append(quotient)
    #     quotient += modulus

    # primitive_roots = [2,6,7,8] # Found from the table according to a specific modulus. 
    roots_powers = [] # Stores lists. Each list has the powers of the primitive root in the corresponding location. 
    # If roots are [2,6,7,8], root_powers[0] gives powers of 2, [1] gives powers of 6. 
    for root in primitive_roots: # 2
        root_power = [] # 2 ** 1, 2 ** 2, 2 ** 3, ..., till cap. 
        power = 1
        while root ** power < cap:
            root_power.append(root ** power)
            power += 1
        roots_powers.append(root_power)

    # See if any power of the primitive root is in the quotient_rewrites
    # If roots are [2,6,7,8], search 2 first, index is zero (for later access)
    # Loop through root_power of 2, so 2, 4, 8, 16, ... till cap.
    # If one match something in the primitive roots, then it is 
    # A candidate to choose. 

    # TODO: do direct computation on 2**5 % 11 == 10 each time, 
    # rather than computing all multiples of the quotient, to save space.

    # Delete quotient_rewrites, delete append to quotient_rewrites,
    # Leave primitive roots powers section, 
    # Implement loop through powers, check each equaling quotient when modding the modulus. 2**5 % 11 == 10
    root_power_pairs = []

    for i in range(len(roots_powers)):
        # i tracks the root we're on, shared between root_powers and primitive_roots. 
        # i points to 2 and the list of 2's powers. 
        root_powers = roots_powers[i]
        power = 1
        for root_power in root_powers:
            if root_power % modulus == quotient:
            # Return the root and its power. 
            # Rewrite quotient with the root to the power. So 5 ** 34. 
            # Rewrite x with root to y. So x = 5 ** y. 
            # At i=0, the power is 1. At i=1, the power is 2. Thus return one more than i. 
                root_power_pairs.append((primitive_roots[i], power))
            power += 1
    
    return root_power_pairs

def main():
    quotient = int(input("What's your quotient? Input an integer. (Ex. The 6 in x ** 9 = 6 mod 7) \n"))
    modulus = int(input("What's your modulus? Input an integer. (Ex. The 7 in x ** 9 = 6 mod 7)\n"))
    primitive_roots = [int(root) for root in (input("What are the primitive roots of this modulus? Check the table. Input all numbers at once with a space between each number. (Ex. For mod 7, input 3 5 with a space in between.)\n")).split()]
    cap = int(input("What number do you want to search up to? Input an integer. (Ex. The cap of the 6 mod 7 set, which is {..., -1, 6, 13, 20, 27, 34, 41, ...}. The program searches up from the inputted quotient to this cap. Increase the cap if the 'Choices:' section is empty.)\n"))
    print("\nChoices:")
    for root, power in what_root_which_power(quotient, modulus, cap, primitive_roots):
        print(f"root: {root}, power: {power}")
    print("\nQuotient = root ** power; root is g in x = g^y. (Ex. Rewrite x ** 9 = 6 mod 7 as 3^(9 * y) = 3^3 mod 7.)")
    print("Next step: Equate exponents, mod (modulus - 1). Solve for y, the plug back for x (may have several solutions).")

if __name__ == "__main__":
    main()
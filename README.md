# Modular Exponentiation Solver
Modular Exponentiation Solver solves x^4 = 3 in Z/23Z and its likes with step-by-step guidance, and formats the solutions like x = 4, 19 (mod 23)
# Example Run inputting x^4 = 3 in Z/23Z when prompted
Input your problem statement exactly in the format of x^a = b in Z/mZ; (Ex. x^4 = 3 in Z/23Z).  Regular expressions automatically match your numbers. Only support prime moduli between and include 3 to 29.

x^4 = 3 in Z/23Z

Rewrote problem statement as: 

7^(4y) = 7^2 (mod 23)

Exponent equality: 4y = 2 (mod 22)

Has solutions. gcd(x_power = 4, modulus_x - 1 = 22) == 2 | 2 (the power to which the primitive root (7) is raised).

Downstaired equality: 2y = 1 (mod 11)

gcd(x_power = 2, downstairs_modulus_y = 11) == 1

x_power and downstairs_modulus_y are verified to be coprime.

Thus, x_power can be inverted in downstairs_modulus_y; 2 modulo 11 has an inverse.

6 is the inverse of 2 modulo 11, so multiply 6 to each side; y will have coefficient 1.

Inverted-the-divisor downstairs equality: y = 6 (mod 11)

Upstaired equality: y = 6, 17 (mod 22)

Unsimplified solutions of x: x = 7^y = 7^6, 7^17 (mod 23)

Simplified solutions of x: x = 4, 19 (mod 23)

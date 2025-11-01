from unittest import main, TestCase
from PrimitiveRoots import what_root_which_power

# Use assertIn and not assertEqual because there are multiple choices of combinations of primitive root and power that will satisfy being bases. 
class testPrimitiveRoots(TestCase):
    def test1(self):
        self.assertIn((3, 3), 
                      what_root_which_power(quotient = 6, modulus = 7, cap = 3000, primitive_roots = [3,5]))
    
    def test2(self):
        self.assertIn((3, 2), 
                      what_root_which_power(quotient = 2, modulus = 7, cap = 3000, primitive_roots = [3,5]))
    
    def test3(self):
        self.assertIn((6, 2), 
                      what_root_which_power(quotient = 3, modulus = 11, cap = 3000, primitive_roots = [2, 6, 7, 8]))
        
    def test4(self):
        self.assertIn((2, 6), 
                      what_root_which_power(quotient = 7, modulus = 19, cap = 3000, primitive_roots = [2, 3, 10, 13, 14, 15]))
        
if __name__ == "__main__":
    main()
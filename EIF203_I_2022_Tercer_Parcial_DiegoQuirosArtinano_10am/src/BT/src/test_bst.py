"""
 loriacarlos@gmail.com
 EIF203 I-2022
 Testing BST

"""
from bst import BST # Our BST module (bst.py)

import random       # for random data generation
import pprint as pp # Pretty print of lists, dictionaries, tuples
random.seed(666)    # We fixed the seed in order to allways get the same sample
# Main testing
if __name__ == "__main__":
    print("*** Testing BST Trees (EIF203 I-2022) ***")
    ################################################################
    # Setup test case
    # A BST
    bst = BST()
    # Print it, it is empty
    print('>>> BST before insertions = ', end='')
    pp.pprint(bst.to_dict(), indent = 4)
    #################################################################
    # Generate a random sample and insert it into bst
    sample_range = range(10, 100, 5)
    sample_size = 10
    data = [n for n in random.sample(sample_range, sample_size)]
    print(f">>> Data to insert {data}")
    # Test random insertion
    print()
    for n in data:
        print(f">>>Inserting data={n}")
        bst.insert(n)
    # Convert BST to dictionary for a prettier print out
    print()
    print('>>> BST (as dict) after insertions = ')
    pp.pprint(bst.to_dict(),indent = 4)
    print()
    print(f">>> BST height = {bst.height}")
    print(f">>> BST search({10}) = {bst.search(10)}")
    print(f">>> BST search({666}) = {bst.search(666)}")
    print(f">>> BST min = {bst.min()}")
    print(f">>> BST Data in order: {bst.in_order()}")
    
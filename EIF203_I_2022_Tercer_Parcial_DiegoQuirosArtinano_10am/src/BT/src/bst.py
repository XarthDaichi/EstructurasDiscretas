"""
 loriacarlos@gmail.com
 EIF203 I-2022
 See btree.BTree 
 Binary Search Tree (BST) demo for teaching purposes
 BST.BNode: Binary Node, represents the actual logic (search, insert, ...). It inherits from BTree.BNode
 BST: is a BTree extended to become a Binary Search Tree
 
"""

from functools import total_ordering # total_ordering adds operators for comparisons, automatically
import warnings                      # Tool for handling warnings

from btree import BTree # Normal Binary Tree

class BST(BTree):
    """
        Class representing a simple Binary Search Tree.
        Extends BTree with BST capabilities assimig BNode has them
        As BTree does, it delegates logic to BST.BNode
    """
############### BNode ############################
    @total_ordering # This allows compasisons (eg. <=, !=, ...) among BNodes
    class BNode(BTree.BNode):
            """
            Class representing a simple Binary Search Node (BNode)
            Contains (should contains) logic required for  common used operations
            A BST just delegates  functionality to BNode
            """
            
            def __init__(self, data=None, parent=None, left=None, right=None):
                for node in (parent, left, right): # Check if given each is a BNode
                    if node: 
                        assert(isinstance(node, BST.BNode))
                super().__init__(data, left, right)
                self.__parent = parent # parent BNode
                self.__super = super(BST.BNode, type(self)) # to allow access to super property (hook)
            
            def __set_super_property(self, attr, value): #hook for updating a property
                getattr(self.__super, attr).fset(self, value)
            @property
            def parent(self):
                return self.__parent
            @parent.setter
            def parent(self, p):
                assert(isinstance(p, BST.BNode))
                self.__parent = p
            @property
            def left(self):
                return super().left
            @left.setter
            def left(self, node):
                assert(isinstance(node, BST.BNode))
                self.__set_super_property('left', node)
                self.parent = self
            @property
            def right(self):
                return super().right
            @right.setter
            def right(self, node):
                assert(isinstance(node, BST.BNode))
                self.__set_super_property('right', node)
                self.parent = self
            
            # To allow BNode == and < comparisons      
            def __eq__(self, other):
                if self is other: return True
                if not isinstance(other, BST.BNode): return NotImplemented
                return self.data == other.data
                
            def __lt__(self, other):
                if self is other: return False
                if not isinstance(other, BST.BNode): return NotImplemented
                return self.data < other.data
######################################## BST proper body ###################################
            # BNode  proper logic   
            def insert(self, node):
                """
                    Classic BST insertion
                    Always returns (it) self
                """
                # Check for duplicate key (data)
                if node == self:
                    warnings.warn(f"BST.BNode.insert: Duplicated Key {node}. Insert ignored!")
                    return self  
                if node < self:
                    # Insert into the left 
                    if self.left: 
                        return self.left.insert(node)
                    self.left = node
                    return self
                # Insert into the right
                if self.right: 
                    return self.right.insert(node)
                self.right = node
                return self
                
            def search(self, data):
                """
                    Binary searches data in Tree
                    Returns True if found
                    Returns None if not
                """
                if self == data:
                    return True  
                if data < self:
                    if self.left: 
                        return self.left.search(data)
                    else: return None
                if self.right: 
                    return self.right.search(data)
                return None
                
            def min(self):
                """ 
                    Finds the minimum node 
                """
                #warnings.warn('BST.BNode.min not implemented')
                m = self.data
                next = self
                while next.left:
                    next = next.left
                    m = next.data
                return m
                
            def in_order(self):
                """
                    Returns the list of elements in order 
                """
                def to_inorder_list(n):
                    if not n: return []
                    if n.is_leaf: return [n.data]
                    return n.in_order()
                if self.is_leaf: return []
                all_nodes = to_inorder_list(self.left)
                all_nodes.append(self.data)
                all_nodes.extend(to_inorder_list(self.right))
                return all_nodes
            ############################################################
            # For external representation
            def to_dict(self):
                """
                    Converts the tree into a dictionary for printing purposes
                    Output starts with the header as shown:
                    {'data':None, 'left': dict of the root, 'right':None}
                    Each dict : {'data':Any object, 
                                 'left': dict of the left child, 
                                 'right': dict of the right child }
                """
                def dict_it(t):
                    if not t: return None
                    return t.to_dict()
                if self.is_leaf():
                    return {'data':self.data}
                return {'data': self.data, 'left': dict_it(self.left), 'right': dict_it(self.right) }
                
            def __str__(self):
                if self.is_leaf(): 
                    return str(self.data)
                return f"{self.data}({self.left}, {self.right})"
                
            def __repr__(self):
                if self.is_leaf():
                    return f"BNode(data={self.data})"
                return f"BNode(data={self.data}, left={self.left.__repr__()}, right={self.right.__repr__()})"

###################### BST Logic ############################
  
    def __init__(self):
        super().__init__(header = BST.BNode()) # Inits the header
        
    def insert(self, data):
        if not isinstance(data, BST.BNode): # cast it if required
            data = BST.BNode(data)
        if self.is_empty():
            self.root().left = data
        else:
            self.root().left.insert(data)
        return self
            
    def search(self, data):
        if self.is_empty():
            return None
        if not isinstance(data, BST.BNode): # cast it if required
            data = BST.BNode(data)
        return self.root().left.search(data)
        
    def in_order(self):
        if self.is_empty(): return []
        return self.root().left.in_order()
        
    def min(self):
        if self.is_empty():
            return None
        return self.root().left.min()
        
    def to_dict(self):
        """
            To convert Tree into a dictionary
        """
        if self.is_empty(): return {}
        return self.root().left.to_dict()

############################## A little Testing ###################
def test_1():
    bst = BST()
    print(f"bst is empty? --> {bst.is_empty()}")
    data_list = [666, 555, 333, 444, 777]
    print(f'bst insert {data_list}', )
    for data in data_list:
        print(f'Inserting {data}')
        bst.insert(data)
    pp.pprint(bst.to_dict(), indent = 4)
    print(f'bst height --> {bst.height}')
    print(f'Search 555 in bst --> {bst.search(555)}')
    
    
if __name__ == "__main__":
    import pprint as pp # pretty-print Python structures
    test_1()
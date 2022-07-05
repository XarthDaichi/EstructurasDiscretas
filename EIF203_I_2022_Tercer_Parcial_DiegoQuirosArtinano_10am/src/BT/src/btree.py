"""
 loriacarlos@gmail.com
 EIF203 I-2022
 Demo Binary Tree for Demo purposes
"""


class BTree: # Binary Tree
    """
        Class representing a simple Binary tree
        All logic is delegated (bypased) to BNode
        It contains a header (__header) that:
        either
            a) __header is None meaning Tree is empty
            or 
            b) __header is a BNode which is the actual root of the tree
    """
    class BNode: # Binary Node
        """
        Class representing a Binary Node
        Contains minimal logic/structure required for binary  operations
        BNode has data:object (the data in node), left:BNode and right:BNode
        
        """
        def __init__(self, data=None, left=None, right=None):
            self.__data = data
            self.__left = left
            self.__right = right
        @property
        def data(self):
            return self.__data
        @data.setter
        def data(self, data):
            self.__data = data
        @property
        def left(self):
            return self.__left
        @left.setter
        def left(self, node):
            self.__left = node
            
        @property
        def right(self):
            return self.__right
        @right.setter
        def right(self, node):
            self.__right = node
            
        def is_leaf(self):
            return not (self.left or self.right)
        @property
        def height(self):
            def h(t):
                return 0 if t is None else t.height
            return 0 if self.is_leaf() else 1 + max(h(self.left), 
                                                    h(self.right))
        
        def __str__(self):
            return str(self.data) if self.is_leaf() else f"{self.data}({self.left}, {self.right})"
        
        def __repr__(self):
            return f"BNode(data={self.data}, left={self.left.__repr__()}, right={self.right.__repr__()})"
############################### BTree Body ############################
    def __init__(self, header=None, data = None):
        if header is None:
            header = BTree.BNode()
        self.__set_root(header, data)
        
    def root(self):
        return self.__header
        
    def __set_root(self, header, data=None):
        self.__header = header
        self.__header.data = data
        
    def is_empty(self):
        return not self.__header.left
        
    @property
    def height(self):
        if self.is_empty(): return 0
        return self.root().left.height
    
    def __str__(self):
        return str(self.root().left)
    
    def __repr__(self):
        return repr(self.root().left)
        
    @property
    def left(self):
        if self.is_empty(): return None
        return self.root().left
    @left.setter
    def left(self, tree):
        assert(isinstance(tree, BTree))
        self.__header.left = tree.root()
    
    @property
    def right(self):
        if self.is_empty(): return None
        return self.root().right #BTree(BTree.BNode(left=self.root().right))
    @right.setter
    def right(self, tree):
        assert(isinstance(tree, BTree))
        self.__header.right= tree.root()

########################## TO DO #############################           
def print_inverse_polish(Tree):
    """
        Prints the polish inverse notation for the BTree tree
        to do!!
        Don't google it. Do it by yourself alone
    """
    print("print_inverse_polish not implemented!")
    
########################## Testing ############################
def test_1():
    leafX = BTree(data="x")    # leafX = x
    leafY = BTree(data="y")    # leafY = y
    leaf666  = BTree(data=666) # leaf666 = 666
    
    treePlus = BTree(data='+')
    treePlus.left = leafX
    treePlus.right = leafY # treePlus = +(x, y)
    
    treeTimes = BTree(data='*') 
    treeTimes.left = treePlus
    treeTimes.right = leaf666 # treeTimes = *(+(x, y), 666)
    
    mainTree = BTree(data="**")
    mainTree.left = treeTimes
    mainTree.right = treePlus # mainTree = **(*(+(x, y), 666), +(x, y))
    
    print(f"{mainTree=:}") 
    print(f"{mainTree.height=:}") # 3
    
    print_inverse_polish(mainTree)
    
if __name__ == "__main__": 
    test_1()

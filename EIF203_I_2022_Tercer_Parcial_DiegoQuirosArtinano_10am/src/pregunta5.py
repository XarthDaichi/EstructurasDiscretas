'''
Nombre: Diego Quiros Artinano
Cedula: 901150326 / ID-Universidad: 315071
NRC: 41712
'''

from bst import BST

def intersection(Tree1, Tree2):
    newBST = BST()
    nodeT1 = Tree1.root()
    nodeT2 = Tree2.root()

    if Tree1.search(nodeT2):
        newBST.insert(nodeT2)
    if Tree2.search(nodeT1):
        newBST.insert(nodeT1)

    newBST.insert(intersection(Tree1.left, Tree2))
    newBST.insert(intersection(Tree1.right, Tree2))
    newBST.insert(intersection(Tree2.left, Tree1))
    newBST.insert(intersection(Tree2.right, Tree1))

    return newBST

    

    


import sys
sys.setrecursionlimit(10000)
input = sys.stdin.read

inp = list(map(lambda x:x.replace('\x1a',''),input().splitlines()))
inp = list(map(int,inp)) # 정수 변환해줘야한다


class Tree:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

    
def insert_bst(root,value):
    if root == None:
        return Tree(value)
    
    if value < root.value:
        root.left = insert_bst(root.left,value)
    else:
        root.right = insert_bst(root.right,value)
    return root

def construct_bst_input_preorder(preorder):
    root = Tree(preorder[0])
    for v in preorder[1:]:
        insert_bst(root,v)
    return root

def postorder_print(tree):
    if tree == None:
        return None
    postorder_print(tree.left)
    postorder_print(tree.right)
    print(tree.value)


input_tree = construct_bst_input_preorder(inp)
postorder_print(input_tree)



import sys
sys.setrecursionlimit(100000)
input = sys.stdin.read

class Tree:
    def __init__(self,l,r,v):
        self.l = l
        self.r = r
        self.v = v

def maketree(inS,inE,poS,poE):
    ####### 서브트리없음
    if inS > inE or poS > poE:
        return None
    # 후위순회 끝이 루트가된다
    root_val = postorder[poE]
    root = Tree(None,None,root_val)
    # inorder를 그 값 중심으로 나누어서 분할
    root_idx = inorder.index(root_val)

    size = root_idx-inS
    # inorder는 루트중심으로
    # postorder는 size 이용, 끝값은 이미 루트로 쓰임
    root.l = maketree(inS,root_idx-1,poS,poS+size-1)
    root.r = maketree(root_idx+1,inE,poS+size,poE-1)
    return root

def preorder(tree):
    if tree== None:
        return
    print(tree.v,end=" ")
    preorder(tree.l)
    preorder(tree.r)
    return

inp = input().replace('\x1a','').splitlines()
n = int(inp[0])
inorder = list(map(int,inp[1].split()))
postorder = list(map(int,inp[2].split()))


res = maketree(0,n-1,0,n-1)

preorder(res)


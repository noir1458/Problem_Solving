import sys
input = sys.stdin.readline

class Treenode:
    def __init__(self,val=0,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

n=int(input())
inorder=list(map(int,input().split()))
postorder=list(map(int,input().split()))


def make_tree(inorder,postorder):
    idx = {val:idx for idx,val in enumerate(inorder)}
    post_idx = len(postorder)-1

    def divide(in_start, in_end):
        nonlocal post_idx
        if in_start > in_end:
            return None
        
        # postorder에서 뒤의것이 루트
        root_val = postorder[post_idx]
        root = Treenode(root_val)
        # inorder에서 인덱스 찾기
        in_idx = idx[root_val]
        # postorder에서 루트에 쓴건 빼기
        post_idx -= 1

        # postorder에서 뒤에서부터 구성중이므로 우측 먼저 구성
        # in_idx 중심으로 앞뒤로 좌우 트리가 된다
        root.right = divide(in_idx+1,in_end)
        root.left = divide(in_start, in_idx-1)
        return root

    return divide(0,len(inorder)-1)

# preorder
def preorder(root):
    if root==None:
        return
    print(root.val,end=' ')
    preorder(root.left)
    preorder(root.right)

root = make_tree(inorder,postorder)
preorder(root)
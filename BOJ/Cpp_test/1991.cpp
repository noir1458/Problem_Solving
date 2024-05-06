#include <iostream>
#include <bits/stdc++.h>

using namespace std;

typedef struct Node{
    char data;
    struct Node* left;
    struct Node* right;
} Node;

Node* MakeNode(char root){
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->data = root;
    newNode->left = NULL;
    newNode->right = NULL;
    return newNode;
}

void connect(Node* node, Node* add){
    if(node->left != NULL){
        if (node->left->data == add->data){
            free(node->left);
            node->left = add;
        }
        else{
            connect(node->left,add);
        }
    }

    if(node->right != NULL){
        if (node->right->data == add->data){
            free(node->right);
            node->right = add;
        }
        else{
            connect(node->right,add);
        }
    } 
}

void preorder(Node* node){
    cout << node->data;
    if(node->left != NULL)
        preorder(node->left);
    if(node->right != NULL)
        preorder(node->right);
}

void inorder(Node* node){
    if(node->left != NULL)
        inorder(node->left);
    cout << node->data;
    if(node->right != NULL)
        inorder(node->right);
}

void postorder(Node* node){
    if(node->left != NULL)
        postorder(node->left);
    if(node->right != NULL)
        postorder(node->right);
    cout << node->data;
}


int main() {
	cin.tie(0); cout.tie(0); // fastio
	ios::sync_with_stdio(0); // fastio
	// 풀이 작성
    int N;
    cin >> N;

    char root,l,r;
    cin >> root >> l >> r;
    Node* Root = MakeNode(root);
        if (l != '.'){
            Node* Left =  MakeNode(l);
            Root->left = Left;
        }
        if (r != '.'){
            Node* Right =  MakeNode(r);
            Root->right = Right;
        }


    for (int i = 0; i < N-1; i++)
    {   
        cin >> root >> l >> r;
        Node* Add = MakeNode(root);
        if (l != '.'){
            Node* Left =  MakeNode(l);
            Add->left = Left;
        }
        if (r != '.'){
            Node* Right =  MakeNode(r);
            Add->right = Right;
        }
        connect(Root,Add);
    }
    preorder(Root);
    cout << endl;
    inorder(Root);
    cout << endl;
    postorder(Root);
	return 0;
}

#include <stdio.h>
#include <stdlib.h>

typedef struct Tree{
	int data;
	int color;//1 = red, 0 = black
	struct Tree * parent;
	struct Tree * left;
	struct Tree * right;
}Tree;
typedef struct RBTree{
	Tree * root;
	Tree * NIL;
}RBTree;
void insert(RBTree * t,Tree * temp);
void rightRotate(RBTree * t,Tree * temp);
void leftRotate(RBTree * t, Tree * temp);
void fixup(RBTree * t,Tree * pt);
void inorder(RBTree * t,Tree * node);
int treeDepth(RBTree * t,Tree * r);
int blackHeight(RBTree * t,Tree * r);
Tree * newTreeNode(int data);
RBTree * newRBTree();
int isBlack(Tree * r);
void secondLargest(RBTree * t,Tree * r,int *c);
int main(){
	printf("Input being read from file and make sure that the numbers are separated by a space. Please input the number of elements being inserted: \n");
	int num; 
	scanf("%d",&num);
	int data;
	FILE *file;
	file = fopen("list.txt","r");
	RBTree * t = newRBTree();
	printf("The values being read in: \n");
	for(int i = 0;i < num;i++)
	{
		
		fscanf(file,"%d ",&data);
		
		Tree * node = newTreeNode(data);
		printf("%d ",node->data);

		insert(t,node);
		

	}
	printf("\n\nIn-order traversal of the tree:\n");
	inorder(t,t->root);
	printf("\n");

	printf("\nThe height of the red black tree is %d.\n",treeDepth(t,t->root));

	printf("\nThe black height of the red and black tree is %d.\n",blackHeight(t,t->root));
	int c = 0;
	secondLargest(t,t->root,&c);
	fclose(file);
}
void secondLargest(RBTree * t, Tree * r,int *c)
{
	if(r == t->NIL || *c >= 2)
	{
		return;
	}
	secondLargest(t,r->right,c);

	*c += 1;

	if(*c == 2)
	{
		printf("\nThe second largest element of the tree is %d.\n",r->data);
		return;
	}
	secondLargest(t,r->left,c);

}
int isBlack(Tree * r)
{
	if(r->color == 0)
	{
		return 1;
	}
	else
	{
		return 0;
	}
}
int blackHeight(RBTree * t,Tree * r)//returns -1 if the black height isn't equal
{
	if(r == t->NIL)
	{
		return 0;
	}
	int leftH = blackHeight(t,r->left);
	int rightH = blackHeight(t,r->right);
	int add = isBlack(r);
	if(rightH == -1 || leftH == -1 || leftH != rightH)
	{
		return -1;
	}
	else
	{
		return leftH + add;
	}
}
RBTree * newRBTree(){
	RBTree * t = malloc(sizeof(RBTree));
	Tree * nilNode = malloc(sizeof(Tree));
	nilNode->left = NULL;
	nilNode->right = NULL;
	nilNode->parent = NULL;
	nilNode->color = 0;
	nilNode->data = 0;
	t->NIL = nilNode;
	t->root = t->NIL;

	return t;
}
Tree * newTreeNode(int data)
{
	Tree * node = malloc(sizeof(Tree));
	node->left = NULL;
	node->right = NULL;
	node->parent = NULL;
	node->data = data;
	node->color = 1;
	return node;
}
int treeDepth(RBTree * t,Tree * r)
{
	if(r != t->NIL)
	{
		int dep1 = treeDepth(t,r->left);
		int dep2 = treeDepth(t,r->right);
		if(dep1 > dep2){
			return dep1 + 1;
		}
		else
		{
			return dep2 + 1;
		}
	}
	else
	{
		return 0;
	}
}
void inorder(RBTree * t,Tree * node)
{
	if(node != t->NIL)
	{
		inorder(t,node->left);
		if(node->color == 1)
		{
			printf("%d-R;",node->data);
		}
		else
		{
			printf("%d-B;",node->data);
		}
		inorder(t,node->right);
	}
}

void fixup(RBTree * t,Tree * pt)
{
	while(pt->parent->color == 1)
	{
		if(pt->parent == pt->parent->parent->left){
			Tree * uncle = pt->parent->parent->right;
		
			if(uncle->color == 1)
			{
				pt->parent->color = 0;
				uncle->color = 0;
				pt->parent->parent->color = 1;
				pt = pt->parent->parent;
			}
		
			else{// case 2 or 3
				if(pt == pt->parent->right){//case 2
					pt = pt->parent;
					leftRotate(t,pt);
				}
				//case 3
				pt->parent->color = 0;
				pt->parent->parent->color = 1;
				rightRotate(t,pt->parent->parent);
			}
		}
		else{
			Tree * uncle = pt->parent->parent->left;
			if(uncle->color == 1)
			{
				pt->parent->color = 0;
				uncle->color = 0;
				pt->parent->parent->color = 1;
				pt = pt->parent->parent;
			}
			else{
				if(pt == pt->parent->left){
					pt = pt->parent;
					rightRotate(t,pt);
				}
				pt->parent->color = 0;
				pt->parent->parent->color = 1;
				leftRotate(t,pt->parent->parent);
			}
		}
	}
	t->root->color = 0;
}

void insert(RBTree * t, Tree * temp){
	Tree * p = t->NIL;//variable for the parent of the added node
	Tree * x = t->root;//temp variable

	while(x != t->NIL){
		p = x;
		if(temp->data < x->data){
			x = x->left;
		}
		else
		{
			x = x->right;
		}
	}
	temp->parent = p;
	if(p == t->NIL){
		t->root = temp;
	}
	else if(temp->data < p->data)
	{
		p->left = temp;
	}
	else
	{
		p->right = temp;
	}
	temp->right = t->NIL;
	temp->left = t->NIL;

	fixup(t,temp);
	
}
void rightRotate(RBTree * t,Tree * temp)
{
	Tree * left = temp->left;
	temp->left = left->right;
	if(left->right != t->NIL)
	{
		left->right->parent = temp;
	}
	left->parent = temp->parent;
	if(temp->parent == t->NIL)
	{
		t->root = left;
	}
	else if(temp == temp->parent->right)
	{
		temp->parent->right = left;
	}
	else
	{
		temp->parent->left = left;
	}
	left->right = temp;
	temp->parent = left;
}
void leftRotate(RBTree * t,Tree * temp)
{
	Tree * right = temp->right;
	temp->right = right->left;
	if(right->left != t->NIL)
	{
		right->left->parent = temp;
	}
	right->parent = temp->parent;
	if(temp->parent == t->NIL)
	{
		t->root = right;
	}
	else if(temp == temp->parent->left)
	{
		temp->parent->left = right;
	}
	else
	{
		temp->parent->right = right;
	}
	right->left = temp;
	temp->parent = right;
}






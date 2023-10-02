#include "lab12.h"
struct BST{
	Client * client;
	struct BST *left,*right;
};
//This function initializes and creates a BST and returns it.Returns NULL if malloc fails
BST * initBST()
{
	BST * tree;
	tree = malloc(sizeof(BST));
	if(tree == NULL)
	{
		return NULL;
	}
	tree->left = NULL;//sets left,right, and client pointers to NULL
	tree->right = NULL;
	tree->client = NULL;
	return tree;
}
//This function takes a BST and returns the size of the BST
size_t BSTSize(BST *tree)
{
	if(tree == NULL)
	{
		return 0;
	}
	else
	{
		return BSTSize(tree->left) + 1 + BSTSize(tree->right);
	}

}
//This function frees all of the members of the tree
void freeBST(BST * tree)
{
	if(tree == NULL)
	{
		return ;
	}
	freeBST(tree->left);//uses recursion to traverse through the entire tree and to free each member
	freeBST(tree->right);
	free(tree);
}
//This function recursively inserts the given struct pointer onto the tree using the same compare function as with before. It will return 1 on success and 0 on failure.
int insertClient(BST * tree,Client * client)
{
	tree = insert(tree,client);//calls insert to insert the client into the tree
	if(tree == NULL)//checks to see if our insertion worked
	{
		return 0;
	}
	else
	{
		return 1;
	}
}
//This function takes a BST and a client and inserts it into the tree and returns the tree
BST * insert(BST * tree,Client * client)
{
	if(tree == NULL)
	{
		BST * temp;
		temp = newTree(client);
		return temp;
	}
	if(compareClients(client,tree->client) < 0)//checks to see if client is < tree->client
	{
		tree->left = insert(tree->left,client);
	}
	else if(compareClients(client,tree->client) > 0)//checks to see if client is  > tree->client
	{
		tree->right = insert(tree->right,client);
	}
	return tree;
}
//This function performs a recursive binary search on the given tree. This function will return 1 if the struct is found or 0 if not.
int searchClients(BST * tree,Client * query)
{
	if(compareClients(query,tree->client) == 0)//checks to see if they are equal
	{
		return 1;
	}
	else if(compareClients(query,tree->client) > 0)//checks to see if query is greater than the current stem
	{
		return searchClients(tree->right,query);
	}
	else if(compareClients(query,tree->client) < 0)//checks to see if query is less than the current stem
	{
		return searchClients(tree->left,query);
	}
	return 0;	
}


//This function prints the tree in order using recursion
void inOrderPrintClients(BST * tree)
{
	flatten(tree,0);//Calls a function to recursively print the tree in order
}
//This function takes a tree and prints the contents of the tree in order
void flatten(BST * t,int index)
{
	if(t != NULL)
	{
		flatten(t->left,index);
		printf("Client %d: accountNumber: %lu, accountWorth: %f, daysActive %d\n",index,t->client->accountNumber,t->client->accountWorth,t->client->daysActive);
		index++;
		flatten(t->right,index);
	}
}
//This function creates a new leaf for the BST to be used to insert into the tree
BST * newTree(Client * c)
{
	BST * t = malloc(sizeof(BST));
	t->client = c;//puts the client into the t and sets the left and right pointers to NULL
	t->left = t->right = NULL;
	return t;
}
//This function compares two structs given by their accountWorth members. It will return a 1 if a > b, -1 if a < b, and 0 if they are both equal
int compareClients(Client * a,Client * b)
{
	if(a->accountWorth > b->accountWorth)//checks to see if a > b
	{
		return 1;
	}
	if(a->accountWorth < b->accountWorth)//checks to see if a < b
	{
		return -1;
	}
	return 0;//returns 0 if they are equal
}
//This function is used to test code
Client * readClientArray(FILE *fp)
{
	Client * client;
	client = malloc(sizeof(client));
	if(client == NULL)
	{
		return NULL;
	}
	else
	{
		fscanf(fp,"%lu %f %d",&client->accountNumber,&client->accountWorth,&client->daysActive);
	}
	return client;	
}

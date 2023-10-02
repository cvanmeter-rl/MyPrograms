#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef struct BST BST;

// Complexity: O(1)
BST* initBST();

// Complexity: O(n)
size_t BSTSize(BST *tree);

// Complexity: O(n)
void freeBST(BST *tree);

#define SECT_F

typedef struct {
	unsigned long accountNumber;
	float accountWorth;
	int daysActive;
} Client;
int compareClients(Client *a,Client *b);
BST * newTree(Client * c);
void flatten(BST * t, int index);
BST * insert(BST * tree,Client * client);
// Complexity: O(log(n))
int insertClient(BST *tree, Client *client);

// Complexity: O(log(n))
int searchClients(BST *tree, Client *query);

// Complexity: O(n)
void inOrderPrintClients(BST *tree);

Client * readClientArray(FILE *fp);//This function is used to test cod
int recBin(int first,int last,BST * tree, Client * query);

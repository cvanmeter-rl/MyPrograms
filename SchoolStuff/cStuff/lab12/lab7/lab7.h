#include <stdio.h>
#include <stdlib.h>

// partial typedef, so the Node type can contain itself
typedef struct Node Node;

struct Node {
	Node *next;
	void *data;
};

typedef struct {
	Node *head;
	int size;
} List;

List* initList();
int getSize(List *list);
void freeList(List *list);
void* getAtIndex(List *list, int index);

#define SECT_F
int insertBefore(List *list, void *object, void *sentinel);
int hasDuplicates(List *list, void *object);
void* removeAfter(List *list, void *sentinel);

typedef struct{//struct used to test code in main
	int empID,jobType;
	float salary;
}Employee;
Employee * readEmployeeArray(FILE *fp);//function used to read employee structs for testing code
Node * createNode(void * object);
Node * addItem(Node * list,void * object);
int insertAtHead(void * object,List * list);


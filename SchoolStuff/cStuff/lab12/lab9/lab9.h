#include <stdio.h>
#include <stdlib.h>


// partial typedef, so you can define your own list type
typedef struct List List;

typedef struct nodestruct{
	void * object;
	struct nodestruct * next;
	struct nodestruct * previous;
}Node;
struct List{
	Node * head;
	Node * tail;
	int size;
};
// COMPLEXITY: O(1)
List* initList();
// COMPLEXITY: O(1)
int getSize(List *list);
// COMPLEXITY: O(n)
void* getAtIndex(List *list, int index);
// COMPLEXITY: O(n)
void freeList(List *list);

#define SECT_F
// COMPLEXITY: O(1)
int insertAtTail(List *list, void *object);
// COMPLEXITY: O(1)
void* getHead(List *list);
// COMPLEXITY: O(n)
void* removeHead(List *list);

//Employee struct used to test code
typedef struct{
	int empID,jobType;
	float salary;
}Employee;

Node * createNode(void * object);
Node * addItem(Node * list,void * object);
Employee * readEmployeeArray(FILE *fp);//used to test code

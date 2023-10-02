#include <stdio.h>
#include <stdlib.h>
#include <float.h>
typedef struct{
	unsigned long accountNumber;
	float accountWorth;
	int daysActive;
}Client;

typedef struct Queue Queue;
typedef struct nodestruct{
	void * c;
	float accountWorth;
	struct nodestruct * next;
	struct nodestruct * previous;
}Node;
struct Queue{
	Node * head;
	Node * tail;
	int size;
};
// Complexity: O(1)
Queue* initPQ();
// Complexity: O(n)
void freePQ(Queue *pq);

/* Priority:
 *	In an ascending priority queue, the "maximum" element is the next to dequeue,
 *	whereas in a descending priority queue, the "minimum" element is next.
 */

 #define SECT_F

 // Complexity: O(n)
 int insertClientDescendingPQ(Queue *pq, Client *client);
 // Complexity: O(1)
 Client* peekMinClient(Queue *pq);
 // Complexity: O(1)
 Client* deQueueMinClient(Queue *pq);

 Node * createNode(void * object);
 void * getAtIndex(int index,Queue * pq);//used to test code
 Client * readClientArray(FILE *fp);//This function is used to test code

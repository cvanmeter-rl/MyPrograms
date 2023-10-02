#include "lab10.h"
//This function initializes the priority queue in O(1) time and returns NULL if malloc fails
Queue * initPQ()
{
	Queue * queue;
	queue = malloc(sizeof(Queue));//allocates memory for the queue
	Node * dummyNodeHead = malloc(sizeof(Node));//creates and allocates memory for 2 dummy nodes
	Node * dummyNodeTail = malloc(sizeof(Node));
	if(queue && dummyNodeTail && dummyNodeHead)//checks to see if malloc succeeded
	{
		
		queue->size = 0;//sets size to 0
		dummyNodeHead->next = NULL;//initializes and sets the 2 dummy nodes to point to NULL
		dummyNodeHead->previous = NULL;
		dummyNodeHead->accountWorth = FLT_MAX; //This is a max boundary 

		dummyNodeTail->next = NULL;
		dummyNodeTail->previous = NULL;
		dummyNodeTail->accountWorth = -FLT_MAX;//This is a minimum boundary
		queue->head = dummyNodeHead;//sets head and tail to the dummy nodes
		queue->tail = dummyNodeTail;
	
		return queue;
	}
	else
	{
		return NULL;
	}
}
//This function frees all memeory associated with the PQ. 
void freePQ(Queue *pq)
{
	Node * temp;//temp variable used to free the PQ
	while(pq->head != NULL)
	{
		temp = pq->head;
		pq->head = pq->head->next;
		free(temp);
	}
	pq->head = NULL;//sets head tail to NULL and size to 0
	pq->tail = NULL;
	pq->size = 0;
	free(pq);
}
//This function inserts the given struct pointer into the priority queue based upon the accountWorth member in O(n) time. Returns 0 on success and 1 on failure.
int insertClientDescendingPQ(Queue *pq,Client *client)
{
	Node * insert = createNode(client);//Node to be inserted into PQ
	insert->accountWorth = client->accountWorth;
	if(pq->size == 0)//special case if size is 0
	{
		pq->head->next = insert;//dummy node points to insert
		insert->previous = pq->head;//insert previous points to head dummy node
		insert->next = pq->tail;//insert next points to dummy node tail
		pq->tail->previous = insert;//tail previous points to insert
		pq->size++;
	}
	else
	{
		Node * temp = pq->head;//temp variable used to interate and compare in the PQ
		for(int i = 0;i <= pq->size;i++)
		{
			if((insert->accountWorth <= temp->accountWorth) && (insert->accountWorth >= temp->next->accountWorth))//checks to see if the client can be inserted in the correct position
			{
				insert->next = temp->next;//puts insert inbetween the two elements in the PQ
				temp->next->previous = insert;
				temp->next = insert;
				insert->previous = temp;
				pq->size++;
				return 0;
			}
			temp = temp->next;
		}
	}
	return 1;
}
//This function returns the object which is next to dequeue without removing it, in O(1) time.Returns NULL if there is nothing in the PQ
Client * peekMinClient(Queue *pq)
{
	if(pq->size == 0)//returns NULL if the pq is empty
	{
		return NULL;
	}
	else
	{
	return (pq->head->next->c);//returns the client object 
	}
}
//This function dequeues and returns the object which is next to dequeue in O(1) time
Client * deQueueMinClient(Queue *pq)
{
	Node * temp = pq->head->next;//temp variable that holds the Node to be removed
	Client * Obj = temp->c;//holds object to be returned
	pq->head->next = pq->head->next->next;//sets head to the item past the one being removed
	pq->head->next->previous = pq->head;//sets the previous of the item after the one being removed to the dummy Node head
	pq->size--;//decrements size
	free(temp);//frees the removed Node
	return Obj;
}
//This function creates a Node for the passed void * object
Node * createNode(void * object)
{
	Node * p;
	p = malloc(sizeof(Node));
	if(p)
	{
		p->c = object;
		p->next = NULL;
		p->previous = NULL;
	}
	return p;
}
//This function is used to test code
Client * readClientArray(FILE *fp)
{
	Client * c;
	c = malloc(sizeof(Client));
	if(c == NULL)
	{
		return NULL;
	}
	else
	{
		fscanf(fp,"%lu %f %d",&c->accountNumber,&c->accountWorth,&c->daysActive);
	}
	return c;
}
//this function is used to test code
void * getAtIndex(int index,Queue * pq)
{
	if(index > pq->size - 1 || index < 0)
	{
		return NULL;
	}
	else
	{
		Node * p = pq->head->next;
		for(int i = 0; i < index;i++)
		{
			p = p->next;
		}
		return p->c;
	}
}

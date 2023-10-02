#include "lab10.h"
int main()
{
	
	FILE *file;
	file = fopen("employee.txt","r");
	
	int ec;
	Queue * pq;
	
	pq = initPQ();
	
	
	printf("Size = %d\n",pq->size);

	
	Client *c;

	for(int i = 0;i < 5;i++)
	{
		c = malloc(sizeof(Client));
		c = readClientArray(file);
		printf("Reading from file: %lu %f %d\n",c->accountNumber,c->accountWorth,c->daysActive);
		ec = insertClientDescendingPQ(pq,c);
		printf("ec = %d size = %d\n",ec,pq->size);
	}
	
	printf("After Inserting At Head:\n");
	Node * temp = pq->head->next;
		
	c = peekMinClient(pq);
	c = deQueueMinClient(pq);
	c = deQueueMinClient(pq);
	c = deQueueMinClient(pq);
	c = deQueueMinClient(pq);
	c = deQueueMinClient(pq);
	for(int i = 0; i < pq->size;i++)
	{
		c = getAtIndex(i,pq);	
		printf("size = %d Client: accountNumber: %lu accountWorth: %f daysActive: %d \n",pq->size,c->accountNumber,c->accountWorth,c->daysActive);
		temp = temp->next;
	}
	freePQ(pq);
	fclose(file);
	
}

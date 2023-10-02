#include "lab12.h"
int main()
{
	FILE *file;
	file = fopen("employee.txt","r");
	Client * client;
	

	BST * tree;
	tree = initBST();
	int ec = 0;
	for(int i = 0;i<5;i++)
	{
		client = malloc(sizeof(Client));
		client = readClientArray(file);
		printf("emp[%d] - accountNumber: %lu,accountWorth = %f,daysActive = %d\n",i,client->accountNumber,client->accountWorth,client->daysActive);
		printf("hello");
		ec = insertClient(tree,client);
		printf("ec = %d\n",ec);
	}
	//inOrderPrintClients(tree);



	freeBST(tree);
}

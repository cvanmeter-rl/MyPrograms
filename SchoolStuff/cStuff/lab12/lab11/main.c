#include "lab11.h"
int main()
{
	FILE *file;
	file = fopen("employee.txt","r");
	Client * client;
	
	Client *array;
	
	array = createArray(5,sizeof(Client));

	for(int i = 0;i<5;i++)
	{
		client = malloc(sizeof(Client ));
		client = readClientArray(file);
		printf("emp[%d] - accountNumber = %lu,accountWorth = %f,daysActive = %d\n",i,client->accountNumber,client->accountWorth,client->daysActive);
		array[i] = *client;
		
	}
	printf("Size: %ld\n",arraySize(array));
	size_t a;
	client = &array[2];
	a = searchClients(array,client);
	printf("%lu %f %d\n",client->accountNumber,client->accountWorth,client->daysActive);
	printf("%ld",a);
	freeArray(array);	
}

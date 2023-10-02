#include "lab11.h"
//This function takes the number of elements and the size of the data type desired.
void * createArray(size_t size,size_t elemSize)
{
	int * array;
	array = malloc(size*elemSize+sizeof(size_t));
	array[0] = size;//hides the size infront of the array
	if(array == NULL)//checks to see if malloc failed
	{
		return 0;
	}
	else
	{
		return(void *)(array + 1);//returns the array of client structs
	}
}
//This function returns the array size
size_t arraySize(void * array)
{
	return ((unsigned int *)array)[-1];
}
//This function frees the array
void freeArray(void * array)
{
	array = (int *)array - 1;
	free(array);//frees the array
	array = NULL;
}
//This function compares two structs given by their accountWorth members. It should return a strictly negative number if a < b, a strictly positive number if a > b, or 0 if they are equal.
int compareClients(Client *a,Client * b)
{
	if(a->accountWorth > b->accountWorth)//Checks to see if a > b
	{
		return 1;
	}
	if(a->accountWorth < b->accountWorth)//checks to see if a < b
	{
		return -1;
	}
	return 0;//returns 0 if they are equal
}
//This function performs a binary search on the given struct array using recursion. This function will return the index of the query struct when it is located, or SIZE_MAX on error.

size_t searchClients(Client *array,Client * query)
{
	int first = 0;//The first element will always be 0
	int last = arraySize(array) - 1;//Gets the last element of the array
	while(first <= last)
	{
		int mid = (first+last)/2;
		if(compareClients(query,&array[mid]) > 0)
		{
			first = mid + 1;
		}
		else if(compareClients(query,&array[mid]) < 0)
		{
			last = mid - 1;
		}
		else
		{
			return mid;
		}
	}
	return SIZE_MAX;

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

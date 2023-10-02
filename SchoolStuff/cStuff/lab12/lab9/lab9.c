#include "lab9.h"


/*
 * This function returns an initialized list pointer. Returns NULL if malloc fails.
*/
List * initList()
{
	List * list;
	list = malloc(sizeof(List));//allocates space for list
	list->head = malloc(sizeof(Node));//allocates space for head
	list->tail = malloc(sizeof(Node));//allocates space for tail
	if(list || list->head || list->tail)//checks to make sure malloc succeeded
	{
		list->size = 0;//sets size to 0
		return list;
	}
	else
	{
		return NULL;//returns NULL if malloc fails
	}
}

//This function takes a list pointer and returns the number of elements currently in the list
int getSize(List * list)
{
	return (list->size);
}

/* This function takes a list pointer and desired index and returns the object at the given index in the list. This function returns NULL if the index passed can't be found or is an invalid index  */
void * getAtIndex(List * list,int index)
{
	if(index > list->size - 1 || index < 0)//checks to make sure the index is valid
	{
		return NULL;
	}
	else
	{
		Node * p = list->head;//Node used to traverse through list
		for(int i = 0;i < index;i++)//loop used to traverse through list
		{
			p = p->next;
		}
		return p->object;//returns object at the desired index
	}	
}
/*This function unitializes a list and frees all memeory allocated for it.*/
void freeList(List * list)
{
	Node * temp;//temp Node used to help free the items in the list
	while(list->head != NULL)//while loop used to traverse through list
	{
		temp = list->head;//temp used to hold the current item in list
		list->head = list->head->next;//traverse to the next item in list
		free(temp);//free the item in the list
	}
	list->head = NULL;//sets head to NULL
	list->tail = NULL;//sets tail to NULL
	list->size = 0;//sets size to 0
	free(list);//frees the list

}
/*This function inserts the given object at the tail of the list in O(1) time. Returns 1 on success,else 0*/
int insertAtTail(List * list,void * object)
{
	Node * insert = createNode(object);//Node that holds the object that is being inserted at tail
	if(list->size == 0)//special case if there is nothing in the list
	{
		list->head = insert;//sets head to the Node since its the only item in list
		list->tail = list->head;//tail and head will be set to the same Node since there is only 1 item in list
		list->size++;//increments size
		return 1;
	}
	else//This for every other case when the list isn't empty
	{
		list->tail->next = insert;//sets previous tail to point towards new tail
		list->tail = insert;//sets the new tail to insert
		list->size++;
		return 1;
	}
	return 0;
}
/*This function returns the object at the head of the list in O(1) time.*/
void * getHead(List * list)
{
	return(list->head->object);//returns the object at the head of the list
}
/*This function removes and returns the object at the head of the list in O(n) time.This function returns NULL if there is nothing able to be removed.*/
void * removeHead(List * list)
{
	void * Obj;//This holds the object at the head of the list
	Node * remove = list->head;//sets remove to the Node being removed
	Obj = remove->object;//sets Obj to the object of the Node being removed
	if(list->size == 0)//Checks to see if the list is empty and if so it returns NULL because nothing can be removed
	{
		return NULL;
	}
	else if(list->size == 1)//special case if there is only 1 item in the list
	{
		//Node * remove;//temp variable used to hold the info of the Node that is being removed
		//remove = list->head;//sets remove to the Node being removed
		//Obj = remove->object;//sets Obj to the object of the Node being removed
		list->head = NULL;//sets head to NULL
		list->tail = NULL;//sets tail to NULL
		list->size--;//decrements size by 1
		free(remove);//frees the Node being removed
		return Obj;
	}
	else//This works for every other case
	{
		//Node * remove;//temp variable
		//remove = list->head;//sets remove to the Node being removed;
		//Obj = remove->object;//sets Obj to the object of the Node being removed
		list->head = list->head->next;//moves the head of the list to the next item in the list
		list->head->previous = NULL;//sets the new head previous to NULL
		list->size--;//decrements size by 1
		free(remove);//frees the Node being removed
		return Obj;
	}
}
//This function creates a NULL with the given object inside it
Node * createNode(void * object)
{
	Node * p;//Node created for object
	p = malloc(sizeof(Node));
	if(p)//checks to see fi malloc succeded
	{
		p->object = object;
		p->next = NULL;
		p->previous = NULL;
	}
	return p;
}
//This function is used to test code 
Employee * readEmployeeArray(FILE *fp)
{
	Employee * employee;
	employee = malloc(sizeof(Employee));
	if(employee == NULL)
	{
		return NULL;
	}
	else
	{
		fscanf(fp,"%d %d %f",&employee->empID,&employee->jobType,&employee->salary);
	}
	return employee;
}

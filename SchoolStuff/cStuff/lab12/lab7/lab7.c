#include "lab7.h"
/* readEmployeeArray:This function is used to read employee values and store them into a struct. This function is used solely for testing in main.
*/
Employee * readEmployeeArray(FILE *fp)
{
	Employee *employee;
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
/*
createNode: This function creates a Node and puts the object being passed into the struct as well as setting the next to NULL.
object: This is the information that is being stored in the Node.
*/
Node * createNode(void * object)
{
	Node * p;//Node that is being created and will be returned
	p = malloc(sizeof(Node));//allocates memory for the node
	if(p)//if malloc succeeds the object will be placed within the node
	{
		p->data = object;
		p->next = NULL;
	}
	return p;
}
/*
addItem: This function takes a Node and an object and creates a new Node for the object and places it infront of the list that was passed to it.
list: This is the head of the list where the new object Node will be placed infront of.
object: This is the object that will be used to create a new Node and placed infront of list.
*/
Node * addItem(Node * list,void * object)
{
	Node * p;//new Node for object
	p = createNode(object);//Node is created
	p->next = list;//places the Node infront of Node list
	return p;
}
/*
This function takes a linked list and attempts to insert the given object before the specified sentinel object in the list. If the sentinel object doesn't exist on the list, the object should be inserted at the end of the list. This function will return 1 on success and 0 on failure.
*/
int insertBefore(List *list,void *object,void *sentinel)
{
	Node *temp = list->head;//temp variable used to traverse through the linked list
	int c;//holds a count
	Node *hold = list->head;//hold variable used to get the Node before sentinel
	Node * obj = createNode(object);//creates a Node for the object
	for(int i = 0;i<getSize(list);i++)//for loop used to interate through the linked list
	{
		if(getAtIndex(list,i) == sentinel)//checks to see if the object at the current Node is the same as the sentinel object
		{
			c = i-1;//count is set to the index infront of the sentinel object Node
			for(int j = 0;j<c;j++)//for loop used to get the hold Node to the Node before sentinel
			{
				hold = hold->next;
			}
			hold->next = obj;//sets the Node before sentinal to point at obj
			obj->next = temp;//sets obj->next to the Node with sentinel in it
			list->size += 1;//increases the size by 1
			return 1;//returns 1 since we found the sentinel object and were able to insert the object
		}
		temp = temp->next;//goes to the next Node in the list
	}
	temp->next = obj;//sets the previous last list element to obj which is the new last element in the list
	obj->next = NULL;//sets obj->next to NULL because it is at the end of the list
	list->size += 1;//increments size by 1
	if(obj->next != NULL)//if obj->next isn't equal to NULL that means that the sentinel object was never found and that there was an error in placing the object at the end of the list.
	{
		return 0;
	}
	else//Returns 1 if the object was succesfully placed at the end of the list
	{
		return 1;//returns 1 since we were able to insert it
	}
}
/*
removeAfter: This function takes a linked list and removes the object which appears after the specified sentinel object in the list. If the sentinel object doesn't exist on the list, nothing will be removed. This function returns the object to the user.The function returns the sentinel object if the sentinel object isnt in the linked list or if the sentinel values is at the end of the linked list.
*/
void * removeAfter(List * list,void * sentinel)
{
	Node *temp = list->head;//temp Node used to traverse through the linked list.
	void * holdObj;//holds the object that is being removed
	for(int i = 0;i < getSize(list);i++)//for loop used to interate through the linked list
	{
		if(getAtIndex(list,i) == sentinel)//checks to see if the sentinel object is in the linked list
		{
			if(temp->next != NULL)//checks to make sure that the sentinel value isnt at the end of the list
			{
				holdObj = getAtIndex(list,i+1);//holds the object that is being removed
				temp->next = temp->next->next;//removes the Node with the object in it
				list->size -= 1;//reduces the size by 1
				return holdObj;//returns the object of the node that is being removed
			}
			else//Returns sentinel if the sentinel value is at the end of the list because that means that there is nothing to be removed after the sentinel object.
			{
				return sentinel;
			}
		}
		temp = temp->next;//goes to the next Node in the linked list

	}
	return sentinel;
}
/*
hasDuplicates: This function takes a linked list and returns 1 if the give object is on the list more than once, or 0 otherwise.
*/
int hasDuplicates(List * list,void * object)
{
	int count = 0;//count variable used to count the number of duplicates
	for(int i = 0;i < getSize(list);i++)//for loop to go throught the whole linked list
	{
		if(getAtIndex(list,i) == object)//checks to see if any of the objects in the linked list are duplicates of the object passed to the function.
		{
			count++;//increments count if there is a duplicate
		}
	}
	if(count >= 2)//if count is greater than or equal to 2 there are duplicates and it will return 1
	{
		return 1;
	}
	else
	{
		return 0;//returns 0 if there are no dupliacates
	}
}
/*
This function initializes and returns a linked list.This function returns NULL if malloc fails
*/
List * initList()
{
	List * list;//linked list to be returned
	list = malloc(sizeof(List));//allocates space for the list
	list->head = malloc(sizeof(Node));//allocates space for the Node head
	if(list || list->head)//checks to make sure malloc succeeded
	{
		list->size = 0;//sets size to 0 since there is nothing in the list
		return list;
	}
	else
	{
		return NULL;//returns NULL if malloc failed for either list or list->head
	}

}
/*
freeList: This function takes a linked list and frees all memory allocated for the list. 
*/
void freeList(List *list)
{
	free(list->head);//frees the memory for the head in the list struct
	free(list);//frees the memory for list
}
/*
getSize: This function takes a linked list and returns the number of elements on the list
*/
int getSize(List *list)
{
	return (list->size);//returns the number of elements in the list
}
/*
getAtIndex: This function takes a linked list and returns the object at the given index, or NULL on error.
index: This desired location to be retrieved
*/
void * getAtIndex(List * list,int index)
{
	if(index > list->size - 1)//checks to see if the index passed is greater than the number of elements in list
	{
		return NULL;//returns NULL if the index is greater than the number of elements in list
	}
	else
	{
		Node *p = list->head;//sets a Node to the first Node in the list
		for(int i = 0;i < index;i++)//interates all the way through the linked list to the desired location
		{
			p = p->next;//goes to the next Node in the linked list
		}
		return p->data;//returns the object at the desired index
	}
}
/*
insertAtHead:This function takes an object and a list and creates a Node for the passed object and places that Node at the head of the list.Returns 1 on failure and 0 on success
*/
int insertAtHead(void * object,List * list)
{
	if(getSize(list) == 0)//special case for if the list is empty.
	{
		list->head = createNode(object);//sets the head of the list to the Node for object.
		list->size++;//increments size by 1
	}
	else
	{
		list->head = addItem(list->head,object);//creates and adds the Node for the object at the head of the list
		list->size++;//increments size by 1
	}
	if(list->head == NULL)//checks to see if the head of the list is NULL 
	{
		return 1;//returns 1 for a failure
	}
	else
	{
		return 0;//returns 0 for success
	}
}



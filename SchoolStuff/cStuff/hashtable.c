#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define HASH_SIZE 97

typedef struct linkedList{
	char key[100];
	char value[100];
	struct linkedList * previous;
	struct linkedList * next;
}linkedList;

typedef struct{
	linkedList * entries[HASH_SIZE];
}hashTable;

hashTable newTable();
int simpleHash(char s[100]);
int getIndex(char s[100]);
void addEntry(hashTable * table,char key[100],char value[100]);
void appendHead(linkedList * a,linkedList * append);
void cleanUpLinkedList(linkedList * a);
void cleanUpTable(hashTable * table);
void removeFriend(hashTable * table,char key[100],char value[100]);
void findFriends(hashTable * table,char key[100]);
int checkFriends(hashTable * table,char key[100],char value[100]);
void print_linked_list(linkedList * a);
void printHashTable(hashTable table);
void removeNext(linkedList * a);
void removePrevious(linkedList * a);

int main(){
	printf("%s\n","Input");
	char input1 = 'A';
	char input2[100];
	char input3[100];
	scanf("%c",&input1);

	hashTable table = newTable();
	
	while(input1 != 'X')
	{
		switch(input1)
		{
			case 'P':
				scanf("%s",input2);
				addEntry(&table,input2,input2);
				break;
			case 'F':
				scanf("%s %s",input2,input3);
				addEntry(&table,input2,input3);
				addEntry(&table,input3,input2);//added two entries so that if you search for either person they both come up as friends for one another
				break;
			case 'L':
				scanf("%s",input2);
				findFriends(&table,input2);
				break;
			case 'U':
				scanf("%s %s",input2,input3);
				removeFriend(&table,input2,input3);
				removeFriend(&table,input3,input2);
				break;
			case 'Q':
				scanf("%s %s",input2,input3);
				int c = checkFriends(&table,input2,input3);
				if(c == 1)
				{
					printf("Output: Yes\n");
				}
				else
				{
					printf("Output: No\n");
				}
				break;

		}
		scanf("%c",&input1);
	}
	printHashTable(table);
	cleanUpTable(&table);
}

void printHashTable(hashTable table)
{
	for(int i = 0;i < HASH_SIZE; ++i)
	{
		print_linked_list(table.entries[i]);
	}
	return;
}

void print_linked_list(linkedList * a)
{
	if(a == NULL)
	{
		printf("[]\n");
		return;
	}
	linkedList * t = a;
	printf("[(%s, %s)",t->key,t->value);
	t = t->next;
	while(t != NULL)
	{
		printf("-->(%s,%s)",t->key,t->value);
		t=t->next;
	}
	printf("]\n");
}

void removeNext(linkedList * a)
{
	if(a->next != NULL)
	{
		linkedList * temp = a->next;
		a->next = a->next->next;
		free(temp);
	}
	else
	{
		printf("Nothing to remove!\n");
	}

}

void removePrevious(linkedList * a)
{
	if(a->previous != NULL)
	{
		linkedList * temp = a->previous;
		a->previous = a->previous->previous;
		if(a->previous != NULL)
		{
			a->previous->next = a;
		}
		free(temp);
		if(a->next == NULL)
		{
			printf("This key has no next\n");
		}
	}
	else
	{
		printf("Nothing to remove!\n");
	}
}

//Returns a 1 if the two people are friends and a 0 if they aren't friends
int checkFriends(hashTable * table,char key[100],char value[100])
{
	int index = getIndex(key);
	linkedList * a = table->entries[index];
	while(a != NULL)//added a->next != NULL to ignore the initial record of just the person's name
	{
		if(strcmp(a->value,value) == 0)
		{
			return 1;
		}
		a = a->next;
	}
	return 0;
}

void findFriends(hashTable * table,char key[100])
{
	int index = getIndex(key);
	linkedList  * a = table->entries[index];
	printf("Output: ");
	while(a != NULL && a->next != NULL)//added a->next != NULL to ignore the initial record of just the person's name
	{
		printf("%s ",a->value);
		a = a->next;
	}
	printf("\n");
}

void removeFriend(hashTable * table,char key[100],char value[100])
{
	int index = getIndex(key);
	linkedList * a = table->entries[index];
	while(a != NULL)
	{
		if(strcmp(a->value,value) == 0 && strcmp(a->key,key) == 0)
		{
			a = a->previous;
			if(a == NULL)
			{
				a = table->entries[index];
				a = a->next;
				if(a == NULL)
				{
					cleanUpLinkedList(table->entries[index]);
				}
				removePrevious(a);
				table->entries[index] = a;
			}
			else
			{
				removeNext(a);
			}
		}
		a = a->next;
	}
}

//Creates the hash table with all empty entries. The number of entries is fixed
hashTable newTable(){
	hashTable h;
	for(int i = 0;i < HASH_SIZE;++i)
	{
		h.entries[i] = NULL;	
	}
	return h;	
}
//puts the new friend after the initial entry of the person record
void appendHead(linkedList * a,linkedList * append)
{
	if(append->next == NULL)
	{
		append->previous = a->previous;
		a->previous = append;
		append->next = a;
	}
}

//Adds an entry based on the hash of the key.
//accounts for collision by using chaining
void addEntry(hashTable * table,char key[100],char value[100])
{
	int index = getIndex(key);
	if(table->entries[index] != NULL)
	{
		//collision occurred
		linkedList * a = table->entries[index];
		while(a != NULL)
		{
			//we found the key
			if(strcmp(a->key,key) == 0 && strcmp(a->value,value) == 0)
			{
				strcpy(a->value,value);
				break;
			}
			else
			{
				a = a->next;
			}
			if(a == NULL)
			{
				a = (linkedList *)malloc(sizeof(linkedList));
				strcpy(a->key,key);
				strcpy(a->value,value);
				appendHead(table->entries[index],a);
				table->entries[index] = a;
			}
		}
	}
	else
	{
		//There was no collision
		table->entries[index] = (linkedList *)malloc(sizeof(linkedList));
		strcpy(table->entries[index]->key,key);
		strcpy(table->entries[index]->value,value);
		if(table->entries[index] == NULL)
		{
			printf("Error\n");
		}
	}
}

//This function gets the index of an entry 
int getIndex(char s[100])
{
	return simpleHash(s);
}

//A simple hash where the order doesnt affect the hash value
int simpleHash(char s[100])
{
	int i = 0;
	int hash = 0;
	while(i < 100 && s[i] != '\0')
	{
		hash = (hash + (s[i] % 128)) % HASH_SIZE;
		i++;
	}
	return hash;
}

void cleanUpLinkedList(linkedList * a)
{
	linkedList * delete = a;
	while(delete != NULL)
	{
		linkedList * next = delete->next;
		free(delete);
		delete = next;
	}
}

void cleanUpTable(hashTable * table)
{
	for(int i = 0; i < HASH_SIZE;++i)
	{
		if(table->entries[i] != NULL)
		{
			cleanUpLinkedList(table->entries[i]);
			table->entries[i] = NULL;
		}
	}
}

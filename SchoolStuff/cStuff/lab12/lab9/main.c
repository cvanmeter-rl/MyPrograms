#include "lab9.h"
int main()
{
	FILE *file;
	file = fopen("employee.txt","r");

	int ec;
	List * list;
	list = initList();
	printf("Size = %d\n",getSize(list));

	
	Employee *emp;
	for(int i = 0;i < 5;i++)
	{
		emp = malloc(sizeof(Employee));
		emp = readEmployeeArray(file);
		printf("Reading from file: %d %d %f\n",emp->empID,emp->jobType,emp->salary);
		ec = insertAtTail(list,emp);
		//ec = insertHead(emp,list);
		printf("ec = %d size = %d\n",ec,getSize(list));
	}
	
	//emp = removeHead(list);
	//emp = removeHead(list);
	//emp = removeHead(list);
	//emp = removeHead(list);
	//emp = removeHead(list);
	
	/*
	emp = removeTail(list);
	emp = removeTail(list);
	emp = removeTail(list);
	emp = removeTail(list);
	emp = removeTail(list);
	*/
	printf("After Inserting At Head:\n");
	for(int i = 0;i < getSize(list);i++)
	{
		emp = getAtIndex(list,i);
		printf("size = %d emp: empID: %d jobType: %d salary: %f \n",getSize(list),emp->empID,emp->jobType,emp->salary);
	}
	freeList(list);
	fclose(file);
}

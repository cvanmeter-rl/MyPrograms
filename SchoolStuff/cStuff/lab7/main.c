#include "lab7.h"
int main()
{
	FILE *file;
	file = fopen("employee.txt","r");

	List * list;
	list = initList();
	printf("size after init = %d\n",getSize(list));

	int ec;
	Employee *emp;
	for(int i = 0;i<5;i++)
	{
		emp = malloc(sizeof(Employee));
		emp = readEmployeeArray(file);
		printf("Reading from file: %d %d %f\n",emp->empID,emp->jobType,emp->salary);
		ec = insertAtHead(emp,list);
		printf("ec = %d size = %d\n",ec,getSize(list));
	}
	for(int i = 0;i < 5;i++)
	{
		emp = getAtIndex(list,i);
		printf("size = %d emp: empID: %d jobType: %d salary: %f \n",getSize(list),emp->empID,emp->jobType,emp->salary);
	}
	printf("Duplicates: %d\n",hasDuplicates(list,emp));
	freeList(list);
	fclose(file);
}

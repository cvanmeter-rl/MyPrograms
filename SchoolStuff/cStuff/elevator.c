#include <stdio.h>
#include <stdlib.h>



int main()
{
	int floors,start,goal,up,down;
	printf("Enter in the floors, start, goal, up, and down separated by a space\n");
	scanf("%d %d %d %d %d",&floors,&start,&goal,&up,&down);
	int flag = 0;
	int array[100];
	int index = 0;
	int maxSteps = abs(start-goal);
	int count = 0;
	int i;
	while(1)
	{
		array[index++] = start;
		if(start == goal)
		{
			break;
		}
		else if(goal > start)
		{
			start += up;
		}
		else if(goal < start)
		{
			start -= down;
		}
		count++;

		if(count > maxSteps)
		{
			flag = 1;
			break;
		}
	}
	if(flag == 1)
	{
		printf("Use the stairs.");
	}
	else
	{
		array[index++] = start;
		for(i = 0;i < count;i++)
		{
			printf("%d->",array[i]);
		}
		printf("%d\n",array[i]);
	}
	return 0;
}

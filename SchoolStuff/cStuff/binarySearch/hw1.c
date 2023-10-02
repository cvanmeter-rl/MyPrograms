#include <stdio.h>
#include <time.h>


int binarySearch(char filename[],int target);
int main()
{
	
	printf("data1.txt outputs:\n");
	binarySearch("data1.txt",19);
	binarySearch("data1.txt",225);
	binarySearch("data1.txt",705);

	printf("\n");
	
	printf("data2.txt outputs:\n");
	binarySearch("data2.txt",128);
	binarySearch("data2.txt",5756);
	binarySearch("data2.txt",9982);
	
	printf("\n");

	printf("data3.txt outputs:\n");
	binarySearch("data3.txt",1997);
	binarySearch("data3.txt",20680);
	binarySearch("data3.txt",23887);
	
	printf("\n");

	
	printf("data4.txt outputs:\n");
	binarySearch("data4.txt",68189);
	binarySearch("data4.txt",921111);
	binarySearch("data4.txt",935099);
	
}
int binarySearch(char filename[],int target)
{
	clock_t start,end, algoStart;
	start = clock();
	double timeTaken = 0.0;
	double algoTime = 0.0;

	FILE *file;
	int low = 0;
	int mid;
	int high = 0;
	int array[100000];
	int interationCount = 0;

	file = fopen(filename,"r");
	while(!feof(file))
	{
		fscanf(file,"%d ",&array[high]);
		high++;
	}
	high--;
	algoStart = clock();	
	while(low <= high)
	{

		mid = low + ((high - low) / 2);
		if(interationCount < 4)
		{
			printf("Interation %d: low: %d, high %d\n",interationCount+1,low,high);
			interationCount++;
		}
		if(array[mid] == target)
		{
			printf("%d was found at index %d.\n",target,mid);
			end = clock();			
			timeTaken =   (double)(end - start)/CLOCKS_PER_SEC;
			algoTime = (double)(end - algoStart)/CLOCKS_PER_SEC;
			printf("All Time: %f ms\n",timeTaken* 1000.0);
			printf("Algo Time: %f ms\n",algoTime* 1000.0);


			return mid;
		}

		if(array[mid] < target)
		{
			low = mid + 1;
		}
		else
		{
			high = mid - 1;
		}
	}
	printf("%d was not found in the text file.\n",target);
	fclose(file);

	end = clock();
	timeTaken =  (double)(end - start)/CLOCKS_PER_SEC;
	algoTime = (double)(end - algoStart)/CLOCKS_PER_SEC;
	printf("All Time:%f ms\n",timeTaken * 1000.0);
	printf("Algo Time: %f ms\n",algoTime * 1000.0);
	
	return -1;

}

//Course:cs1050 Semester:Fall 2020 Lab:E Author:Christian VanMeter Pawprint:cbvhkg//Course:cs1050 Semester:Fall 2020 Lab:E Author:Christian VanMeter Pawprint:cbvhkg
#include <stdio.h>
#define SIZE 256
void MultArrays(int array1[],int array2[],int array3[],int size)//multiplies the values in array1 and array2 and stores the values in array 3
{
    for(int i = 0;i < size;i++)
    {
        array3[i] = array1[i]*array2[i];
    }
}
int InitializeArray(int array[],int start,int limit,int increment)//initializes and assigns the correct values in the array and returns the size of the array
{
    int size = 0;
    if(start > limit)
    {
        for(int i = start; i >= limit;i += increment)
        {
            array[size] = i;
            size++;
        }
    }
    else
    {
        for(int i = start;i <= limit;i += increment)
        {
        array[size] = i;
        size++;
        }
    }
    return size;
}
void printArray(int array[],int size)//prints the contents of the array
{
    static int arrayNumber = 1;
    for(int i = 0; i < size;i++)
    {
        printf("Array %d Element %d = %d \n",arrayNumber,i,array[i]);
    }
    arrayNumber++;
    if(arrayNumber > 3)
    {
        arrayNumber = 1;
    }
}
int  min(int size1,int size2)
{
    if(size1 > size2)
    {
        return size2;
    }
    else
    {
        return size1;
    }
}

int main(void)
{
int size = 0;//stores the size of the array which is equal for all 3 arrays;
int a[SIZE];//3 arrays that are used for initializing and multiplying the values in array a and b and storing the values in c.
int b[SIZE];
int c[SIZE];

printf("First Array: \n");
size = InitializeArray(a,-20,0,2);
printArray(a,size);

size = InitializeArray(b,5,55,5);
printArray(b,size);

MultArrays(a,b,c,size);
printArray(c,size);

printf("Second Array: \n");
size = InitializeArray(a,-30,-57,-3);
printArray(a,size);

size = InitializeArray(b,70,133,7);
printArray(b,size);

MultArrays(a,b,c,size);
printArray(c,size);

int size1 = 0;//tracks the size of array a
int size2 = 0;//tracks the size of array b
int minSize = 0;//holds the value of the size that has to be used for the arrays
printf("******BONUS******* Third Array: \n");
size1 = InitializeArray(a,90,-100,-10);
size2 = InitializeArray(b,-90,-45,5);

minSize = min(size1,size2);
MultArrays(a,b,c,minSize);

printArray(a,size1);
printArray(b,size2);
printArray(c,minSize);
}

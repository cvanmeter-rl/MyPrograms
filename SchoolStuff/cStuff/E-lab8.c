//Course:cs1050 Semester:Fall 2020 Lab:8 group E  Author:Christian VanMeter Pawprint:cbvhkg//Course:cs1050 Semester:Fall 2020 Lab:E Author:Christian VanMeter Pawprint:cbvhkg
#include <stdio.h>
#define SIZE 256



void GetTwoStrings(char String1[],char String2[]);
void GetIntArray(int *IntArray,int *size);
void PrintOutput(char String1[],char String2[],int numArray[],int size);
int main(void)
{
    printf("***********************\n* Welcome to Lab 8    *\n***********************\n");
    char String1[SIZE];
    char String2[SIZE];
    GetTwoStrings(String1,String2);

    int numArray[SIZE];
    int size = 0;
    GetIntArray(numArray,&size);

    PrintOutput(String1,String2,numArray,size);
}

void GetTwoStrings(char String1[],char String2[])//Gets 2 strings from the user
{
    printf("Please enter a string: ");
    scanf("%s",String1);
    printf("Please enter another string: ");
    scanf("%s",String2);
}

void GetIntArray(int *IntArray,int *size)//gets the integer array elements from the user
{
    printf("Please enter positive integers, and -1 to end\n");
    while(*IntArray != -1)
    {
        printf("element #%d: ",*size);
        scanf("%d",IntArray);
        IntArray++;
    size++;
    }
}
void PrintOutput(char String1[],char String2[],int numArray[],int size)//prints the 2 strings and integers entered from the user
{
    printf("The first string you entered:\n%s\n",String1);
    printf("The secodn string you entered:\n%s\n",String2);
    printf("Array elements you entered: \n");
    for(int i = 0;i < size;i++)
    {
        printf("array[%d]=%d",i,numArray[i]);
    }

}

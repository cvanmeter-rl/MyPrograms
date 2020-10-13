//Course:cs1050 Semester:Fall 2020 Lab:7 group E  Author:Christian VanMeter Pawprint:cbvhkg
#include <stdio.h>
#define ROWS 3
#define COLUMNS 12
#define CUTOFFS 3 //represents the columns and rows for Cutoffs

void PrintScores(int array[][COLUMNS])//prints the test scores for the students
{
    for(int i = 0;i < ROWS;i++)
    {
        printf("Row %d: ",i);
        for(int j = 0;j < COLUMNS;j++)
        {
            printf("%d ",array[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}
void PrintCutoffs(int array[][CUTOFFS])//prints the grade cutoffs
{
    for(int i = 0;i < CUTOFFS;i++)
    {
        printf("Row %d: ",i);
        for(int j = 0;j < CUTOFFS;j++)
        {
            printf("%d ",array[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}

void CalculateLetterGrades(int scores[][COLUMNS],int Cutoffs[][CUTOFFS])//calculates the letter grade for each student and prints their grades
{
    for(int i = 0;i < COLUMNS;i++)//interates through columns of scores
    {
        printf("Student %d: ",i);
        for(int j = 0;j < ROWS;j++)//interates through rows of scores
        {
            if(j == 0)//goes through this if we are looking at cs1050 scores
            {
                    if(scores[j][i] < Cutoffs[CUTOFFS-1][j])
                    {
                        printf("F ");
                    }
                    else if(scores[j][i]>=Cutoffs[CUTOFFS-1][j] && scores[j][i]<Cutoffs[CUTOFFS-2][j])
                    {
                        printf("C ");
                    }
                    else if(scores[j][i]>=Cutoffs[CUTOFFS-1][j] && scores[j][i]<Cutoffs[CUTOFFS-3][j])
                    {
                        printf("B ");
                    }
                    else
                    {
                        printf("A ");
                    }
            }
            else if(j == 1)//goes through this if we are looking at math 1500 scores
            {
                if(scores[j][i] < Cutoffs[CUTOFFS-1][j])
                    {
                        printf("F ");
                    }
                    else if(scores[j][i]>=Cutoffs[CUTOFFS-1][j] && scores[j][i]<Cutoffs[CUTOFFS-2][j] )
                    {
                        printf("C ");
                    }
                    else if(scores[j][i]>=Cutoffs[CUTOFFS-1][j] && scores[j][i]<Cutoffs[CUTOFFS-3][j])
                    {
                        printf("B ");
                    }
                    else
                    {
                        printf("A ");
                    }

            }
            else//goes through this if we are looking at english 1000 grades
            {
                   if(scores[j][i] < Cutoffs[CUTOFFS-1][j])
                    {
                        printf("F ");
                    }
                    else if(scores[j][i]>=Cutoffs[CUTOFFS-1][j] && scores[j][i]<Cutoffs[CUTOFFS-2][j] )
                    {
                        printf("C ");
                    }
                    else if(scores[j][i]>=Cutoffs[CUTOFFS-1][j] && scores[j][i]<Cutoffs[CUTOFFS-3][j])
                    {
                        printf("B ");
                    }
                    else
                    {
                        printf("A ");
                    }
 
            }
        }
        printf("\n");
    }
}

int main(void)
{
    int Cutoffs[3][3] = {{90,95,85},{85,85,80},{70,65,70}};/*Array that holds the cutoff for the grades*/
    int scores[ROWS][COLUMNS] = {{72,95,93,98,99,47,97,85,96,94,98,76},{68,88,97,77,92,32,99,95,91,90,98,82},{62,95,86,98,90,27,85,91,99,85,90,98}};/*Array that holds the scores*/

    printf("Here are the scores: \n");
    PrintScores(scores);

    printf("Here are the grade cutoffs: \n");
    PrintCutoffs(Cutoffs);
    
    printf("Here are the grades: \n");
    CalculateLetterGrades(scores,Cutoffs);
}

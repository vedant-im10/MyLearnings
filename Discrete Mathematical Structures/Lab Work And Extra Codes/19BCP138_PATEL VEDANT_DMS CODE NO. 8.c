//
//  main.c
//
//  Create a program to find the path matrix using Warshall’s algorithm.
//
//  Created by VEDANT on 25/11/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */
// Header Files included for the Program
#include<stdio.h>
#include<conio.h>
// Making the total no. of vertices and edges available globally entered by the User
int v, e, i, j, counter;
void pathMatrixWarshallAlgorithm(int a[v][v]);
void printMatrix(int a[v][v]);

int main()
{
    printf("Enter the total no. of vertices of the Graph : ");
    scanf("%d",&v);
    printf("Note : Graph must be directed\n");
    printf("Enter the total no. of edges of the Graph : ");
    scanf("%d",&e);

    int a[v][v];
    for(i=0;i<v;i++)
    {
        for(j=0;j<v;j++)
        {
            a[i][j] = 0;
        }
    }
    printf("Enter %d edges now :\n",e);
    for(i=0;i<e;i++)
    {
        int source, destination;
        printf("Enter the source : ");
        scanf("%d",&source);
        printf("Enter the destination : ");
        scanf("%d",&destination);
        a[source][destination] = 1;
    }

    pathMatrixWarshallAlgorithm(a);

    return 0;
}
void pathMatrixWarshallAlgorithm(int a[v][v])
{
    int temp1[v][v], temp2[v][v];
    for(i=0;i<v;i++)
    {
        for(j=0;j<v;j++)
        {
            temp1[i][j] = a[i][j];
            temp2[i][j] = 0;
        }
    }
    for(counter=0;counter<=v;counter++)
    {
        if(counter==0)
        {
            printf("Matrix P%d of the Graph is :\n",counter);
            printMatrix(a);
        }
        else
        {
            printf("Matrix P%d of the Graph is :\n",counter);
            for(i=0;i<v;i++)
            {
                for(j=0;j<v;j++)
                {
                    temp2[i][j] = (temp1[i][j] || (temp1[i][counter-1] && temp1[counter-1][j]));
                }
            }
            for(i=0;i<v;i++)
            {
                for(j=0;j<v;j++)
                {
                    temp1[i][j] = temp2[i][j];
                }
            }
            printMatrix(temp1);
        }
    }
    printf("Path Matrix of the Graph is :\n");
    printMatrix(temp1);
}
void printMatrix(int a[v][v])
{
    for(i=0;i<v;i++)
    {
        for(j=0;j<v;j++)
        {
            printf("%d ",a[i][j]);
        }
        printf("\n");
    }
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

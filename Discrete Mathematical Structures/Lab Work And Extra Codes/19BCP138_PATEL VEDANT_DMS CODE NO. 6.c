//
//  main.c
//
//  Create a program to find the path matrix using powers of the Adjacency matrix. 
//
//  Created by VEDANT on 05/11/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */
// Header Files included for the Program
#include<stdio.h>
#include<conio.h>

// Making vertices and edges available globally to the program entered by the User
int v, e, i, j, k, counter;
void pathMatrixAdjacencyPowers(int a[v][v]);
void printMatrix(int a[v][v]);

int main()
{
    printf("Enter the no. of vertices of the Graph : ");
    scanf("%d",&v);
    printf("Note : Edges of the Graph should be directed\n");
    printf("Enter the no. of edges of the Graph : ");
    scanf("%d",&e);
    printf("Enter %d edges now\n",e);

    int a[v][v];
    for(i=0;i<v;i++)
    {
        for(j=0;j<v;j++)
        {
            a[i][j] = 0;
        }
    }
    for(i=0;i<e;i++)
    {
        int source, destination;
        printf("Enter the source : ");
        scanf("%d",&source);
        printf("Enter the destination : ");
        scanf("%d",&destination);
        a[source][destination] = 1;
    }

    pathMatrixAdjacencyPowers(a);

    return 0;
}
void pathMatrixAdjacencyPowers(int a[v][v])
{
    int temp1[v][v], temp2[v][v], sum[v][v], ans[v][v];
    for(i=0;i<v;i++)
    {
        for(j=0;j<v;j++)
        {
            temp1[i][j] = a[i][j];
            temp2[i][j] = 0;
            sum[i][j] = a[i][j];
            ans[i][j] = 0;
        }
    }
    for(counter=1;counter<=v;counter++)
    {
        if(counter==1)
        {
            printf("Total no. of paths of Length %d\n",counter);
            printMatrix(a);
        }
        else
        {
            for(i=0;i<v;i++)
            {
                for(j=0;j<v;j++)
                {
                    temp2[i][j] = 0;
                    for(k=0;k<v;k++)
                    {
                        temp2[i][j] += temp1[i][k]*a[k][j];
                    }
                }
            }
            for(i=0;i<v;i++)
            {
                for(j=0;j<v;j++)
                {
                    sum[i][j] += temp2[i][j];
                    temp1[i][j] = temp2[i][j];
                }
            }
            printf("Total no. of paths of Length %d\n",counter);
            printMatrix(temp2);
        }
    }
    printf("Total no. of paths of Length from %d to %d are : \n",1,v);
    printMatrix(sum);
    for(i=0;i<v;i++)
    {
        for(j=0;j<v;j++)
        {
            if(sum[i][j] != 0)
            {
                ans[i][j] = 1;
            }
            else
            {
                ans[i][j] = 0;
            }
        }
    }
    printf("Path Matrix of the Graph is :\n");
    printMatrix(ans);
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

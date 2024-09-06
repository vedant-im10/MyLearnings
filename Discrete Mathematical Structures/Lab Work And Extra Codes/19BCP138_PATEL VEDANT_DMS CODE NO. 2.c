//
//  main.c
//
//  Create a program to find the degree of each vertex of an undirected graph.
//
//  Created by VEDANT on 28/10/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */
#include<stdio.h>
#include<conio.h>
int main()
{
    int v, e, i, j;
    printf("Enter the total vertices of Graph : ");
    scanf("%d",&v);
    printf("Enter the total edges  of Graph : ");
    scanf("%d",&e);

    int arr[v][v];

    for(i=0; i<v; i++)
    {
        for(j=0; j<v; j++)
        {
            arr[i][j] = 0; // Intialize all the elements of arr[][] to 0
        }
    }
    printf("Enter %d edges (Space-Separated) now\n",e);
    printf("Note : The edge and vertex set starts from 0\n");
    for(i=0; i<e; i++)
    {
        int temp1, temp2;
        scanf("%d%d",&temp1,&temp2);
        arr[temp1][temp2] = 1;
        arr[temp2][temp1] = 1;
    }
    printf("Printing the adjacency matrix now\n");
    for(i=0; i<v; i++)
    {
        for(j=0; j<v; j++)
        {
            printf("%d ",arr[i][j]);
        }
        printf("\n");
    }
    printf("Degree of each vertex is :\n");
    for(i=0; i<v; i++)
    {
        int temp3 = 0;
        for(j=0; j<v; j++)
        {
            if(arr[i][j]==1)
            {
                temp3++;
            }
        }
        printf("Degree of Node %d is %d",i,temp3);
        printf("\n");
    }
    return 0;
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */


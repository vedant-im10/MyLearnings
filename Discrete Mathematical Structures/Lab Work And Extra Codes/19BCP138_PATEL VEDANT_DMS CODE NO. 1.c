//
//  main.c
//
//  Create a program for checking of Isomorphism of two graphs.
//
//  Created by VEDANT on 27/10/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */
#include<stdio.h>
#include<conio.h>
int main()
{
    int v1, e1, v2, e2, i, j, k;

    printf("Enter no. of vertices of graph 1 : ");
    scanf("%d",&v1);
    printf("Enter no. of edges of graph 1 : ");
    scanf("%d",&e1);

    int arr1[v1][v1];
    for(i=0; i<v1; i++)
    {
        for(j=0; j<v1; j++)
        {
            arr1[i][j] = 0;
        }
    }
    printf("Enter %d edges (separated by space) :\n",e1);
    printf("Edge set and vertex set should start from 0\n");

    for(i=0; i<e1; i++)
    {
        int temp1, temp2;
        scanf("%d%d",&temp1,&temp2);
        arr1[temp1][temp2] = 1;
        arr1[temp2][temp1] = 1;
    }
    printf("Printing Adjacency Matrix of Graph 1 :\n");
    for(i=0; i<v1; i++)
    {
        for(j=0; j<v1; j++)
        {
            printf("%d ",arr1[i][j]);
        }
        printf("\n");
    }

    printf("Enter no. of vertices of graph 2 : ");
    scanf("%d",&v2);
    printf("Enter no. of edges of graph 2 : ");
    scanf("%d",&e2);

    int arr2[v2][v2];
    for(i=0; i<v1; i++)
    {
        for(j=0; j<v1; j++)
        {
            arr2[i][j] = 0;
        }
    }
    printf("Enter %d edges (separated by space) :\n",e2);
    printf("Edge set should start from 0\n");

    int temp3, temp4;
    for(i=0; i<e1; i++)
    {
        scanf("%d%d",&temp3,&temp4);
        for(j=0; j<v1; j++)
        {
            for(k=0; k<v1; k++)
            {
                arr2[temp3][temp4] = 1;
                arr2[temp4][temp3] = 1;
                break;
            }
            break;
        }
    }
    printf("Printing  Adjacency Matrix of Graph 2 :\n");
    for(i=0; i<v1; i++)
    {
        for(j=0; j<v1; j++)
        {
            printf("%d ",arr2[i][j]);
        }
        printf("\n");
    }

    int flag = 0;
    if(v1==v2)
    {
        if(e1==e2)
        {
            for(i=0; i<v1; i++)
            {
                for(j=0; j<v1; j++)
                {
                    if(arr1[i][j]==arr2[i][j])
                    {
                        flag = 1;
                    }
                    else
                    {
                        flag = 0;
                        break;
                    }
                }
                if(flag==0)
                {
                    break;
                }
            }
            
        }
        else
        {
            flag = 0;
        }
    }
    else
    {
        flag = 0;
    }
    if(flag==1)
    {
        printf("Both the graphs are equal so they are ISOMORPHIC\n");
    }
    else
    {
        printf("Graphs are not equal so they are not ISOMORPHIC\n");
    }
    return 0;
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

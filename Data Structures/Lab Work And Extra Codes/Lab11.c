//
//  main.c
//
//  Write a program to find DFS traversal of a given graph. 
//
//  Created by VEDANT on 04/12/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */
// DFS algorithm in C

#include <stdio.h>
#include <stdlib.h>

void DFS(int);
int G[10][10],visited[10],n;    //n is no of vertices and graph is sorted in array G[10][10]
 
void main()
{
    int i,j;
    printf("Enter number of vertices:");
   
	scanf("%d",&n);
 
    //read the adjecency matrix
	printf("\nEnter adjecency matrix of the graph:");
   
	for(i=0;i<n;i++)
       for(j=0;j<n;j++)
			scanf("%d",&G[i][j]);
 
    //visited is initialized to zero
   for(i=0;i<n;i++)
        visited[i]=0;
 
    DFS(0);
}
 
void DFS(int i)
{
    int j;
	printf("\n%d",i);
    visited[i]=1;
	
	for(j=0;j<n;j++)
       if(!visited[j]&&G[i][j]==1)
            DFS(j);
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

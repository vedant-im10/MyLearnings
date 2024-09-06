//
//  main.c
//
//  Create a program to find the chromatic number using Welch-Powell algorithm.
//
//  Created by VEDANT on 27/11/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */
// Header Files included for the Program
#include<stdio.h>
#include<conio.h>
#include<stdbool.h>
int v, e, i, j, c;
void graphColoring(int graph[v][v]);
bool graphColoringUtil(int graph[v][v], int color[v], int index);
bool isSafe(int graph[v][v], int color[v], int colorToAssign, int index);
void printSolution(int color[v]);

int main()
{
    printf("Enter the total number of vertices of the Graph : ");
    scanf("%d",&v);
    printf("Note : Graph must be undirected Graph\n");
    printf("Enter the total number of edges of the Graph : ");
    scanf("%d",&e);

    int graph[v][v];
    for(i=0;i<v;i++)
    {
        for(j=0;j<v;j++)
        {
            graph[i][j] = 0;
        }
    }
    printf("Enter %d edges now\n",e);
    for(i=0;i<e;i++)
    {
        int source, destination;
        printf("Enter the source : ");
        scanf("%d",&source);
        printf("Enter the destination : ");
        scanf("%d",&destination);
        graph[source][destination] = 1;
        graph[destination][source] = 1;
    }

    graphColoring(graph);

    return 0;
}
bool isSafe(int graph[v][v], int color[v], int colorToAssign, int index)
{
    for(i=0;i<v;i++)
    {
        if(graph[index][i]==1 && colorToAssign==color[i])
        {
            return false;
        }
    }
    return true;
}
bool graphColoringUtil(int graph[v][v], int color[v], int index)
{
    if(index==v)
    {
        return true;
    }
    for(c=1;c<=10;c++)
    {
        if(isSafe(graph,color,c,index))
        {
            color[index] = c;
            if(graphColoringUtil(graph,color,index+1) == true)
            {
                return true;
            }
        }
    }
    return false;
}
void graphColoring(int graph[v][v])
{
    int color[v];
    for(i=0;i<v;i++)
    {
        color[i] = 0;
    }
    graphColoringUtil(graph,color,0);

    // Printing the Colors Assigned to the vertices
    printSolution(color);
}
void printSolution(int color[v])
{
    int chromaticNumber = 0;
    printf("Colors assigned to each of the vertices are : \n");
    for(i=0;i<v;i++)
    {
        if(color[i] > chromaticNumber)
        {
            chromaticNumber = color[i];
        }
        printf("Node %d : Color %d\n",i,color[i]);
    }
    printf("Chromatic Number of this Graph is : %d",chromaticNumber);
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

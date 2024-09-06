//
//  main.c
//
//  Create a program to find the minimum spanning tree of a connected graph using Kruskal’s algorithm.
//
//  Created by VEDANT on 04/11/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */
// Header Files included for the Program
#include<stdio.h>
#include<conio.h>
#include<stdbool.h>

struct graph
{
    int source;
    int destination;
    int weight;
};
typedef struct graph Graph;

// Making total vertices and edges available globally entered by the User
int v, e, i, j;
void kruskalsMST(Graph arr[e]);
int findParent(int v,int parent[v]);
void printMST();

int main()
{
    printf("Enter the total no. of vertices : ");
    scanf("%d",&v);
    printf("Enter the total no. of edges : ");
    scanf("%d",&e);

    // Creating Array of type struct as per our requirement
    Graph arr[e];
    printf("Enter %d edges now along with their source, destination and weight\n",e);
    for(i=0;i<e;i++)
    {
        printf("Enter the source : ");
        scanf("%d",&arr[i].source);
        printf("Enter the destination : ");
        scanf("%d",&arr[i].destination);
        printf("Enter their weight : ");
        scanf("%d",&arr[i].weight);
    }

    kruskalsMST(arr);

    return 0;
}
void kruskalsMST(Graph arr[e])
{
    // Sorting the Array now on the basis of weights
    Graph temp;
    for(i=0;i<e-1;i++)
    {
        bool sorted = true;
        // Using Bubble Sort to sort all the edges based on weights
        for(j=0;j<e-i-1;j++) // Optimization done here for sorting
        {
            if(arr[j].weight > arr[j+1].weight)
            {
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                sorted = false;
            }
        }
        if(sorted)
        {
            break;
        }
    }
    //Our Array is now sorted on the basis of weight
    for(i=0;i<e;i++)
    {
        printf("Source : %d, Destination : %d, Weight : %d\n",arr[i].source,arr[i].destination,arr[i].weight);
    }

    // Creating Parent Array for every vertex
    int parent[v];
    for(i=0;i<v;i++)
    {
        // Initially the Parent of every vertex is the vertex itself
        parent[i] = i;
    }
    // Creating output Array and it will have (v-1) vertices in it
    Graph output[v-1];

    int count = 0;
    int i = 0;
    // When the total vertices in output Array reaches to (v-1) we will stop and it will be our MST.
    while(count!=v-1)
    {
        Graph currentEdge = arr[i];

        // Check if we can add the currentEdge to the MST or not
        int sourceParent = findParent(currentEdge.source,parent);
        int destinationParent = findParent(currentEdge.destination,parent);

        if(sourceParent != destinationParent)
        {
            // Edge is safe to add in the MST
            output[count] = currentEdge;
            parent[sourceParent] = destinationParent;
            count++;
        }
        i++;
    }
    printMST(output);
}
int findParent(int v,int parent[v])
{
    if(parent[v] == v)
    {
        return v;
    }
    return findParent(parent[v],parent);
}
void printMST(Graph output[v-1])
{
    // Printing the final output Array
    printf("Edges included in the MST along with their Weights are :\n");
    int totalCost = 0;
    for(i=0;i<v-1;i++)
    {
        totalCost = totalCost + output[i].weight;
        if(output[i].source < output[i].destination)
        {
            printf("Source : %d, Destination : %d, Weight : %d\n",output[i].source,output[i].destination,output[i].weight);
        }
        else
        {
            printf("Source : %d, Destination : %d, Weight : %d\n",output[i].destination,output[i].source,output[i].weight);
        }
    }
    printf("Total Cost of MST is %d",totalCost);
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

//
//  main.c
//
//  Create a program to find the distance and diameter of a graph G entered by the user.
//
//  Created by VEDANT on 28/10/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<stdbool.h>
#define MAX 100

struct graph
{
    int V;
    struct list *array;
};
struct list
{
    struct node *head;
};
struct node
{
    int data;
    struct node *next;
};
struct queue
{
    int ele[MAX];
    int front,rear;
};

typedef struct graph Graph;
typedef struct list List;
typedef struct node Node;
typedef struct queue Queue;

Graph* graph;
Queue q;

Graph* createGraph(int v);
Node* createNode(int dest);
void addEdge(int src, int dest);
int isEmpty(void);
int isFull(void);
void enqueue(int x);
void dequeue(void);
int peek(void);
int Distance(int x);
void Diameter();

int main()
{
    q.front = -1;
    q.rear = -1;
    int v, e, i, V;
    printf("Enter the total no. of vertices of the Graph : ");
    scanf("%d",&v);
    printf("Enter the total no. of edges of the Graph : ");
    scanf("%d",&e);

    graph = createGraph(v);

    printf("Note : Graph should be undirected Graph\n");
    printf("Enter %d edges now :\n",e);
    for(i=0;i<e;i++)
    {
        int source, destination;
        printf("Enter the source : ");
        scanf("%d",&source);
        printf("Enter the destination : ");
        scanf("%d",&destination);
        addEdge(source,destination);
    }

    Diameter();

    return 0;
}
Graph* createGraph(int v)
{
	int v, i;
    Graph* temp;
    temp = (Graph* )malloc(sizeof(Graph));
    temp->v = v;
    temp->array = (List* )malloc(v*sizeof(List));
    for(i=0;i<v;i++)
    {
        temp->array[i].head = NULL;
    }
    return temp;
}
Node* createNode(int dest)
{
    Node* temp;
    temp = (Node* )malloc(sizeof(Node));
    temp->data = dest;
    temp->next = NULL;
    return temp;
}
void addEdge(int src, int dest)
{
    Node* new_node;
    new_node = createNode(dest);
    new_node->next = graph->array[src].head;
    graph->array[src].head = new_node;

    new_node = createNode(src);
    new_node->next = graph->array[dest].head;
    graph->array[dest].head = new_node;
}
int isEmpty(void)
{
    if(q.front==-1 && q.rear==-1 || q.front > q.rear)
    {
        return 1;
    }
    return 0;
}
int isFull(void)
{
    if(q.rear==MAX-1)
    {
        return 1;
    }
    return 0;
}
void enqueue(int x)
{
    q.front = 0;
    if(!isFull())
    {
        q.rear++;
        q.ele[q.rear] = x;
    }
}
void dequeue(void)
{
    if(q.front == q.rear)
    {
        q.front = -1;
        q.rear = -1;
    }
    if(!isEmpty())
    {
        q.front++;
    }
}
int peek(void)
{
    if(!isEmpty())
    {
        return (q.ele[q.front]);
    }
}
int Distance(int x)
{
    int v = graph->V;
    int var = x;
    bool visited[v];
    int distance[v];

    for(int i=0;i<v;i++)
    {
        visited[i] = false;
        distance[i] = 0;
    }
    visited[x] = true;
    enqueue(x);

    while(!isEmpty())
    {
        x = peek();
        dequeue();

        Node *temp;
        temp = graph->array[x].head;
        while(temp)
        {
            int val = temp->data;
            if(!visited[val])
            {
                visited[val] = true;
                enqueue(val);
                distance[val] = distance[x]+1;
            }
            temp = temp->next;
        }
    }
    for(int i=0;i<v;i++)
    {
        if(var <= i)
        {
            printf("Distance between %d and %d is : %d.\n",var,i,distance[i]);
        }
    }
    return distance[x];
}
void Diameter()
{
    int diam = 0;
    int v = graph->V;
    for(int i=0;i<v;i++)
    {
        int temp = Distance(i);
        if(temp > diam)
        {
            diam = temp;
        }
    }
    printf("Diameter of the Graph is : %d.",diam);
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

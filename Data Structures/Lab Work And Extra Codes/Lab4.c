//
//  main.c
//  Write a menu driven program  to implement SLL(Singly Link List) with operations as belows:
//  1.Insert  2.Insert after given node  3.Delete a given node  4.Delete a node at given position
//       5.Delete all nodes  6.Traverse(Print LL)  7.Print Total Number of nodes
//
//  Created by VEDANT on 07/10/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

#include <stdio.h>
#include<stdlib.h>

struct node
{
    int value;
    struct node* ptr;
};

typedef struct node node;

void traverse(node* H)
{
    if (H == NULL)
        printf("\nNOTHING TO SHOW\n");
    node* temp;
    temp = H;
    while(temp != NULL)
    {
        printf("%d \t",temp->value);
        temp=temp->ptr;
    }
}

node* insertAtFront(node* H,int V)
{
    node* NewNode;
    NewNode=(struct node*)malloc(sizeof(node));
    NewNode->value=V;
    NewNode->ptr=H;
    return NewNode;
}

node* insertafter(node* H, int V, int v)
{
    node* NewNode,* temp;
    NewNode=(struct node*)malloc(sizeof(node));
    if(NewNode == NULL)
    {
        perror("malloc");
        exit(-1);
    }
    temp=H;
    NewNode->value=V;
    if(H->ptr == NULL)
    {
        H->ptr=NewNode;
        NewNode->ptr=NULL;
        return H;
    }
    while(temp->value != v && temp->ptr != NULL)
    {
        temp=temp->ptr;
    }
    if(temp->ptr == NULL)
        {
            if(temp->value == v)
            {
                NewNode->ptr=NULL;
                temp->ptr=NewNode;
                return H;
            }
            else
            {
                printf("NOt FOUNd \n");
                return H;
            }
        }
        else
        {
            NewNode->ptr=temp->ptr;
            temp->ptr=NewNode;
            return H;
        }
}


node* deletenode(node* H,int V)
{
    node* temp, * ntd;

    if(H==NULL)
    {
        printf("List Empty !!!\n");
        return H;
    }
    else
    {
        if(H->value==V)         //first node delete
        {
            if(H->ptr==H)         //only one node
            {
                free(H);
                return NULL;
            }
            else                   // going till the last node and updating ptr
            {
                temp=H;

                while(temp->ptr != NULL)
                {
                    temp=temp->ptr;
                }

                temp->ptr = H->ptr;
                free(H);
                return temp->ptr;
            }
        }
        else                //deletion at other place
        {
            temp=H;

            while(temp->ptr != NULL  &&  temp->ptr->value !=V)
            {
                temp=temp->ptr;
            }

            if(temp->ptr == NULL)
            {
                printf("NOT FOUND \n");
                return H;
            }
            else
            {
                ntd=temp->ptr;
                temp->ptr=temp->ptr->ptr;
                free(ntd);
                return H;
            }
        }
    }
}

node* deleteAll(node* H)
{
    node *temp;

    while(H != NULL)
    {
        temp = H;
        H = H -> ptr;

        free(temp);
    }

    printf("\nSUCCESSFULLY DELETED ALL NODES OF LINKED LIST\n");
    return H;
}

int count(node* H) {
    int count = 0;
    node* temp;
    temp = H;
    while (temp != 0) {
      count++;
      temp = temp -> ptr;
    }
    printf("\nNo Of Items In Linked List : %d\n", count);
    return count;
}


int main()
{
    node* Head = NULL;
    int choice, num, pos;
    printf("SINGLY LINKED LIST OPERATIONS\n");
    do
    {
        printf("\n1. INSERT AT FRONT");
        printf("\n2. INSERT AFTER OPERATION ");
        printf("\n3. DELETE A NODE");
        printf("\n4. DELETE ALL NODES ");
        printf("\n5. TRAVERSE ");
        printf("\n6. TOTAL NODES ");
        printf("\n7. EXIT ");
        printf("\n\nENTER YOUR CHOICE : ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("\nEnter the value of the node: ");
                scanf("%d", &num);
                Head = insertAtFront(Head, num);
                break;

            case 2:
                printf("Enter the position: ");
                scanf("%d", &pos);
                printf("\nEnter the value of the node: ");
                scanf("%d", &num);
                Head = insertafter(Head, num, pos);
                break;

            case 3:
                printf("\nEnter the value of the node: ");
                scanf("%d", &num);
                Head = deletenode(Head, num);
                break;

            case 4:
                Head = deleteAll(Head);
                break;

            case 5:
                traverse(Head);
                break;

            case 6:
                count(Head);
                break;

            case 7:
                break;
        }
    } while (choice != 7);
    return 0;
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

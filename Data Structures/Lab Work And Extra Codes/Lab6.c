//
//  main.c
//  Write a menu driven program to implement Doubly Link List with the following operations:
//   (i) Insert_Beginning (ii) Insert End (iii) Insert_After_Key (iv) Delete_At (v) Traverse (vi) Reverse Traverse.
//
//  Created by VEDANT on 15/10/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
struct node
{
    int data;
    struct node *prev;
    struct node *next;
};
typedef struct node Node;

Node* createNode()
{
    Node* newNode;
    newNode = (Node*)malloc(sizeof(Node));
    printf("Enter data of the node : ");
    scanf("%d",&newNode->data);
    newNode->prev = NULL;
    newNode->next = NULL;
    return newNode;
}
Node* insertBeginning(Node* head, Node* newNode)
{
    if(head!=NULL)
    {
        newNode->next = head;
        head->prev = newNode;
        head = newNode;
    }
    else
    {
        head = newNode;
    }
    return head;
}
Node* insertEnd(Node* head, Node* newNode)
{
    if(head!=NULL)
    {
        Node* temp;
        temp = head;
        while(temp->next!=NULL)
        {
            temp = temp->next;
        }
        temp->next = newNode;
        newNode->prev = temp;
    }
    else
    {
        head = newNode;
    }
    return head;
}
void insertAfterKey(Node* head, Node* newNode, int key)
{
    if(head!=NULL)
    {
        Node *temp, *var;
        temp = head;
        while(temp->next!=NULL && temp->data!=key)
        {
            temp = temp->next;
        }
        if(temp->data==key && temp->next!=NULL)
        {
            var = temp->next;
            temp->next = newNode;
            newNode->prev = temp;
            newNode->next = var;
            var->prev = newNode;
        }
        if(temp->data==key && temp->next==NULL)
        {
            insertEnd(head,newNode);
        }
        else
        {
            printf("Key not found. So can not insert the data\n");
        }
    }
    else
    {
        printf("Linked List is empty\n");
    }
}
Node* deleteBeginning(Node* head)
{
    if(head!=NULL)
    {
        if(head->next!=NULL)
        {
            Node *temp;
            temp = head;
            head = temp->next;
            temp->prev = NULL;
            head->prev = NULL;
            free(temp);
        }
        else
        {
            head = NULL;
            free(head);
        }
    }
    else
    {
        printf("Linked List is empty\n");
    }
    return head;
}
Node* deleteEnd(Node* head)
{
    if(head!=NULL)
    {
        if(head->next!=NULL)
        {
            Node *temp;
            temp = head;
            while(temp->next!=NULL)
            {
                temp = temp->next;
            }
            temp->prev->next = NULL;
            temp->prev = NULL;
            free(temp);
        }
        else
        {
            head = NULL;
            free(head);
        }
    }
    else
    {
        printf("Linked List is empty\n");
    }
    return head;
}
void deleteAt(Node* head, int position)
{
    Node *temp, *var;
    temp = head;
    int i = 0;
    while(i < position && temp!=NULL)
    {
        temp = temp->next;
        i++;
    }
    if(temp->next!=NULL)
    {
        var = temp;
        temp->prev->next = temp->next;
        temp->next->prev = temp->prev;
        free(var);
    }
    else
    {
        temp->prev->next = NULL;
        free(temp);
    }
}
void traverse(Node* head)
{
    if(head!=NULL)
    {
        Node* temp;
        temp = head;
        while(temp!=NULL)
        {
            printf("%d\n",temp->data);
            temp = temp->next;
        }
    }
    else
    {
        printf("Linked List is empty\n");
    }
}
void reverseTraverse(Node* head)
{
    if(head!=NULL)
    {
        Node* temp;
        temp = head;
        while(temp->next!=NULL)
        {
            temp = temp->next;
        }
        while(temp!=NULL)
        {
            printf("%d\n",temp->data);
            temp = temp->prev;
        }
    }
    else
    {
        printf("Linked List is empty\n");
    }
}

int main()
{
    Node *head, *newNode;
    head = createNode();
    int tillTrue = 1, choice, key, position = 0;
    while(tillTrue)
    {
        printf("...............\n");
        printf("1. Insert beginning Operation\n");
        printf("2. Insert end Operation\n");
        printf("3. Insert after key Operation\n");
        printf("4. Delete beginning Operation\n");
        printf("5. Delete end Operation\n");
        printf("6. Delete at position Operation\n");
        printf("7. Traverse Operation\n");
        printf("8. Reverse Traverse Operation\n");
        printf("9. Exit\n");
        printf("...............\n");
        printf("Enter your choice : ");
        scanf("%d",&choice);
        switch(choice)
        {
            case 1:
                newNode = createNode();
                head = insertBeginning(head,newNode);
                traverse(head);
                break;
            case 2:
                newNode = createNode();
                head = insertEnd(head,newNode);
                traverse(head);
                break;
            case 3:
                printf("Enter the key after which you want to insert the data : ");
                scanf("%d",&key);
                newNode = createNode();
                insertAfterKey(head,newNode,key);
                traverse(head);
                break;
            case 4:
                head = deleteBeginning(head);
                traverse(head);
                break;
            case 5:
                head = deleteEnd(head);
                traverse(head);
                break;
            case 6:
                printf("Enter the position at which you want to delete the data : ");
                scanf("%d",&position);
                deleteAt(head,position);
                traverse(head);
                break;
            case 7:
                traverse(head);
                break;
            case 8:
                reverseTraverse(head);
                break;
            case 9:
                exit(0);
            default:
                printf("Invalid Operation\n");
        }
    }
    return 0;
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

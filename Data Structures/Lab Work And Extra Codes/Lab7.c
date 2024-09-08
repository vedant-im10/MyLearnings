//
//  main.c
//  Write a menu driven program to implement the following Queue operations using Linked List: (i) Enque (ii) Deque (iii) Traverse
//
//  Created by VEDANT on 19/10/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

#include <stdio.h>
#include <stdlib.h>

struct node
{
    int value;
    struct node* next;
};

typedef struct node node;

node* create_node(void)
{
    node* new_node;
    int no;
    printf("\nEnter the info for new node: ");
    scanf("%d",&no);
    new_node = (node *) malloc(sizeof(node));
    new_node->value=no;
    new_node->next=NULL;
    return new_node;
}

void traverse(node* head)
{
    if (head == NULL)
        printf("\nNOTHING TO SHOW\n");
    node* temp;
    temp = head;
    while(temp != NULL)
    {
        printf("%d \t",temp->value);
        temp=temp->next;
    }
}

node* enqueue(node* head, node* new_node)
{
    if (head != NULL)
    {
        node *ptr = head;
        while (ptr->next != NULL) {
            ptr = ptr->next;
        }
        ptr->next = new_node;
        new_node->next = NULL;
        return head;
    }
    else {
        head = new_node;
        return head;
    }
}

node* dequeue(node* head)
{
    if (head != NULL)
    {
        node *tmp = head;
        head = head->next;
        free(tmp);
        return head;
    }
    else
        printf("Queue does not exist.");
    return NULL;
}


int main() {
    node *head, *new_node;
    int choice;
    printf("Creating head node... ");
    head = create_node();
    traverse(head);
    printf("\nQUEUE OPERATIONS\n");
    do
    {
        printf("\n1. ENQUEUE OPERATION");
        printf("\n2. DEQUEUE OPERATION");
        printf("\n3. TRAVERSE");
        printf("\n4. EXIT");
        printf("\n\nENTER YOUR CHOICE : ");
        scanf("%d", &choice);
        switch (choice)
        {
            case 1:
                new_node = create_node();
                enqueue(head, new_node);
                traverse(head);
                break;
                
            case 2:
                head = dequeue(head);
                traverse(head);
                break;
                
            case 3:
                traverse(head);
                break;
                
            case 4:
                break;
        }
    } while (choice != 4);
    return 0;
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

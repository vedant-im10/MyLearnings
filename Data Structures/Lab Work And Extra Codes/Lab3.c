//
//  main.c
//  WAP to check given string(user input) is palindrome or not using stack.
//
//  Created by VEDANT on 07/10/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define MAX 50

int top = -1, front = 0;
int stack[MAX];
void push(char);
void pop(void);

int main()
{
    int i, choice;
    char s[MAX], b;
    printf("CHECK PALINDROME\n");
    while (1)
    {
        printf("\n1. Enter String\n2. Exit\n");
        printf("\nEnter your choice: ");
        scanf("%d", &choice);
        switch (choice)
        {
        case 1:
            printf("Enter the String: ");
            scanf("%s", s);

            for (i = 0; s[i] != '\0'; i++)
            {
                b = s[i];
                push(b);
            }

            for (i = 0; i < (strlen(s)/2); i++)
            {
                if (stack[top] == stack[front])
                {
                    pop();
                    front++;
                }
                else
                {
                    printf("\n%s is not a palindrome\n", s);
                    break;
                }
            }

            if ((strlen(s) / 2)  ==  front)
                printf("\n%s is palindrome\n",  s);
            front  =  0;
            top  =  -1;
            break;

        case 2:
            exit(0);

        default:
            printf("Enter correct choice\n");
        }
    }
    return 0;
}

/* to push a character into stack */
void push(char a)
{
    top++;
    stack[top]  =  a;
}

/* to delete an element in stack */
void pop(void)
{
    top--;
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

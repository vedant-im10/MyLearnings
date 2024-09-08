//
//  main.c
/*  WAP to implement Infix to Postfix converter which takes an infix expression
    and generates corresponding postfix expression as the output.
*/
//  Created by VEDANT on 07/10/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */
#include <stdio.h>
#include <string.h>
#include <math.h>
#define SIZE 20
struct stack
{
    char ele[SIZE];
    int top;
};
typedef struct stack STACK;
STACK s;
int isFull(void);
int isEmpty(void);
char pop(void);
void push(char new_ele);
int priority(char x);
void main()
{
    char exp[20];
    s.top=-1;
    char x;
    int i=0;
    printf("Enter Expression:\n");
    gets(exp);
    while(exp[i] != '\0')
    {
        if((exp[i] >='A' && exp[i] <='Z') || (exp[i] >= '0' && exp[i] <= '9'))
        {
            printf("%c", exp[i]);
        }
        else if(exp[i] == '(')
        {
            push(exp[i]);
        }
        else if(exp[i] == ')')
        {
            while((x=pop()) != '(')
            {
                printf("%c",x);
            }
        }
        else
        {
            while(priority(exp[i]) <= priority(s.ele[s.top]) && exp[i] != '\0')
            {
                printf("%c",pop());
            }
            push(exp[i]);
        }
        i++;
    }
    while(s.top != -1)
    {
        printf("%c",pop());
    }
}
int isFull(void)
{
    if(s.top == SIZE-1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int isEmpty(void)
{
    if(s.top == -1)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
void push(char new_ele)
{
    if(!isFull())
    {
        s.ele[++s.top] = new_ele;
    }
}
char pop(void)
{
    if(!isEmpty())
    {
        return s.ele[s.top--];
    }
    else
    {
        return -1;
    }
}
int priority(char x)
{
    if(x == '(')
    {
        return 0;
    }
    if(x == '+' || x== '-')
    {
        return 1;
    }
    if(x == '*' || x == '/')
    {
        return 2;
    }
    if(x == '$')
    {
        return 3;
    }
    return 0;
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */


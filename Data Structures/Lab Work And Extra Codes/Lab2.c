//
//  main.c
//  Write a menu driven program to Implement stack using Array with underflow and overflow conditions and operations as below:
//       1.Push  2.PoP  3.Traverse(Print all elements)
//
//  Created by VEDANT on 22/09/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

#include <stdio.h>
#define MAX 10
struct stack{
    int top;
    int ele[MAX];
};
typedef struct stack STACK;
STACK s;
int isEmpty(void);
int isFull(void);
void push(int new_ele);
int pop(void);
int peek(void);
void traverse(void);

void main(){
    int choice;
    int option=1;
    s.top=-1;
    int num;

while(option){
    printf("1-PUSH\n");
    printf("2-POP\n");
    printf("3-PEEK\n");
    printf("4-TRAVERSE\n");
    printf("5-EXIT\n");
    printf("Enter your choice:");
    scanf("%d",&choice);
    switch(choice){
        case 1: printf("Enter the element to be pushed\n");
                 scanf("%d",&num);
        push(num);
        break;
        case 2: num=pop();
        if(num!=-1){
            printf("The element popped is: %d \n",num);}
        else {
            printf("The element cannot be popped\n");

        }
        break;
        case 3: printf("The top most value is: %d \n",peek());
        break;
        case 4: traverse();
        break;
        case 5: return;
        break;

    }
    printf("Type 1 to continue");
    scanf("%d", &option);
}
}
int isEmpty(void){
    if(s.top==-1){
        return 1;
    }
    else{
        return 0;
    }
}
int isFull(void){
    if(s.top==MAX-1){
        return 1;
    }
    else{
        return 0;
    }
}
void push(int new_ele){
if(!isFull()){
     s.ele[++s.top]=new_ele;
}
}
int pop(void){
    if(!isEmpty()){
       return (s.ele[s.top--]);
    }
    else{
        return -1;
    }
}
int peek(void){
     return (s.ele[s.top]);
}
void traverse(void){
    if(!isEmpty()){
        for(int i=s.top; i>=0;i--){
            printf(" %d\n",s.ele[i]);
        }
    }
    else{
        printf("Stack underflow\n");
    }
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

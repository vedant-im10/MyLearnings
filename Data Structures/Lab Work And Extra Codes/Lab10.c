//
//  main.c
//
//  Write a program to evaluate a Postfix expression using stack.
//
//  Created by VEDANT on 10/11/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

#include <stdio.h>
#define MAX 20
#include <math.h>
#include <string.h>

struct stack{
    int top;
    char ele[MAX];
};
typedef struct stack STACK;
STACK s;
int isFull(void);
int isEmpty(void);
void push(int new_ele);
int pop(void);
int evaluate(int op1,int op2,char x);

int main(){
    s.top=-1;
    char exp[20];
    int i=0,ans;
    int op1,op2;
    printf("Enter the expression:");
    gets(exp);
    while(exp[i] != '\0'){
        if(exp[i]>='0'&& exp[i]<='9'){
            push(exp[i]-48);

        }
        else {
            op2=pop();
            op1=pop();
            ans=evaluate( op1,op2, exp[i]);
            push(ans);
        }
        i++;
    }
    printf("The Answer is %d",pop());
    return 0;


}
int isFull(void){
    if(s.top==MAX-1){
        return 1;
    }
    else{
        return 0;
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
void push(int new_ele){
    if(!isFull()){
        s.ele[++s.top]=new_ele;
    }
}
int pop(void){
    if(!isEmpty()){
        return s.ele[s.top--];
    }
    else{
        return -1;
    }
}
int evaluate(int op1,int op2,char x){
    if(x=='+'){
        return(op1+op2);
    }
    if(x=='-'){
        return(op1-op2);
    }
    if(x=='*'){
        return(op1*op2);

    }
    if(x=='/'){
        return(op1/op2);
    }
    if(x=='$'){
        return pow(op1,op2);
    }
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

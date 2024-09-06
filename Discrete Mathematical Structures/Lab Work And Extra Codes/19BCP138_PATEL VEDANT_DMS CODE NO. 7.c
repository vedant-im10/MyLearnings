//
//  main.c
//
//  Create a program to find the Lexicographic order of an ordered rooted tree.
//
//  Created by VEDANT on 24/11/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */
// Header Files included for the Program
#include<stdio.h>
#include<conio.h>
#include<stdbool.h>
int main()
{
    // Declaring variable for the total vertices of the Tree
    int vertices, i, j;
    printf("Enter the total number of vertices of the Tree : ");
    // Taking user input of vertices
    scanf("%d",&vertices);

    // Declaring a float array
    float arr[vertices];
    // Initializing the elements of array to 0
    for(i=0;i<vertices;i++)
    {
        arr[i] = 0;
    }
    // Taking user input for all the vertices
    printf("Enter %d vertices now of the ordered rooted Tree\n",vertices);
    printf("Note : Enter all vertices in space separated format by pressing the Enter key\n");
    for(i=0;i<vertices;i++)
    {
        scanf("%g",&arr[i]);
    }

    // Using Bubble Sort algorithm for sorting the vertices
    for(i=0;i<vertices;i++)
    {
        bool sorted = true;
        for(j=0;j<vertices-1-i;j++)
        {
            if(arr[j] > arr[j+1])
            {
                float temp;
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
    // Printing the Lexicographic order of the ordered rooted Tree
    printf("Lexicographic order of an ordered rooted tree is :\n");
    for(i=0;i<vertices;i++)
    {
        printf("%g\n",arr[i]);
    }
    return 0;
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

//
//  main.c
//  WAP for multiplication of two 2D arrays and store result in third 2D array.
//
//  Created by VEDANT on 07/09/20.
//  Copyright © 2020 VEDANT. All rights reserved.
//
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */
#include <stdio.h>
#define MAX 100

// Declare rows and columns for the matrix
int r1, r2, c1, c2;

// Function to print matrix
void printMatrix(int M[][MAX], int rowSize, int colSize)
{
    for (int i = 0; i < rowSize; i++) {
        for (int j = 0; j < colSize; j++){
            printf("%d ", M[i][j]);
         }
        printf("\n");
    }
}

// Function to calculate the multiplication of two arrays
void array_multiply(int A[][MAX], int B[][MAX])
{
    int i, j, k;

    // Matrix to store the result
    int C[MAX][MAX];

    // Check if multiplication is Possible
    if (r2 != c1) {
        printf("Not Possible\n");
        return;
    }

    // Multiply the two
    for (i = 0; i < r1; i++) {
        for (j = 0; j < c2; j++) {
            C[i][j] = 0;
            for (k = 0; k < r2; k++)
                C[i][j] += A[i][k] * B[k][j];
        }
    }

    // Print the result
    printf("\nThe multiplication is: \n\n");
    printMatrix(C, r1, c2);
}

int main() {

    int A[MAX][MAX], B[MAX][MAX];

    // Read size of Matrix A from user
    printf("Enter the number of rows of First Matrix: ");
    scanf("%d", &r1);
    printf("Enter the number of columns of First Matrix: ");
    scanf("%d", &c1);

    // Read the elements of Matrix A from user
    printf("\nEnter elements for 1st Matrix: \n\n");
    for(int i=0; i<r1; i++) {
        for (int j=0; j<c1; j++) {
            printf("Enter the value for A[%d][%d] : ", i+1, j+1);
            scanf("%d",&A[i][j]);
        }
    }

    // Read size of Matrix B from user
    printf("\nEnter the number of rows of Second Matrix: ");
    scanf("%d", &r2);
    printf("Enter the number of columns of Second Matrix: ");
    scanf("%d", &c2);

    // Read the elements of Matrix B from user
    printf("\nEnter elements for 2nd Matrix: \n\n");
    for(int i=0; i<r2; i++) {
        for (int j=0; j<c2; j++) {
            printf("Enter the value for B[%d][%d] : ", i+1, j+1);
            scanf("%d",&B[i][j]);
        }
    }

    // Print the Matrix A
    printf("\n\nFirst Matrix: \n\n");
    printMatrix(A, r1, c1);

    // Print the Matrix B
    printf("\nSecond Matrix: \n\n");
    printMatrix(B, r2, c2);

    // Find the product of the 2 matrices
    array_multiply(A, B);

    return 0;
}
/* BY PATEL VEDANT H. - 19BCP138 - COMPUTER BRANCH */

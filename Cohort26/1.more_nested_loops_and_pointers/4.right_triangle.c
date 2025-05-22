#include <stdio.h>

int main(void) {
    int i, j;
    int height = 5;
    
    for (i = 1; i <= height; i++) { // Outer loop for rows
        for (j = 1; j <= i; j++) { // Inner loop for columns
            printf("*");
        }
        printf("\n"); // Move to the next line
    }
    return 0;
}
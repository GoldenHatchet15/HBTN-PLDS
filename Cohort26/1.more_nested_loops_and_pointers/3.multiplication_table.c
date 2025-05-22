#include <stdio.h>

int main(void) {

    int i, j;
    
    for (i = 1; i <= 5; i++) { // Outer loop for rows
        for (j = 1; j <= 5; j++) { // Inner loop for columns
            printf("%d\t", i * j);
        }
        printf("\n"); // Move to the next row
    }
    return 0;
}
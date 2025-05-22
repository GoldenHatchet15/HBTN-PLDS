#include <stdio.h>

int main(void) {

    int i, j;
    // Outer loop for rows
    for (i = 1; i <= 5; i++) {
        // Inner loop for columns
        for (j = 1; j <= 5; j++) {
    
            printf("%d ", j);
    
        }
    
        printf("\n");
    
    }
    
    return 0;
}
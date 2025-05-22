#include <stdio.h>

int main() {
    
    int i,j;
    // outer loop for hours
    for(i = 0; i < 24; i++){ 

        // inner loop for minutes
        for(j = 0;j < 60; j++){

            printf("*");

        }

        printf("\n");
        
    }
    return 0;
}








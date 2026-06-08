// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *arr;
    int i, size, index = 0;
    
    
    printf("Enter the size of the arr\n");
    scanf("%d", &size);
    /* Step 1: Allocate memory for 5 integers */
    arr = malloc(size * sizeof(int));

    /* Step 2: Check if malloc succeeded */
    if (arr == NULL){
        printf("Failed Allocation");
        return 1;
    }
    /* Step 3: Assign values (e.g., arr[0] = 10, ..., arr[4] = 50) */
    for(i=0; i < size; i++){
        printf("Enter value for the slot %d: \n", i + 1);
        scanf("%d", &arr[i]);
    }
    /* Step 4: Print the values */
    printf("Numbers Entered: ");
    for(i=0; i < size; i++){
        printf("%d", arr[i]);
        if (i < size - 1){
            printf(", ");
        }
    }
    printf("\n");
    /* Step 5: Free the memory */
    free(arr);

    return 0;
}

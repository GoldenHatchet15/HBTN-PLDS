
#include <stdio.h>


int main(void) {
   
    // Declare an integer variable
    int num = 98;
    
    // Declare a pointer variable
    int *p = &num;
    
    // Print the value of num
    printf("Value of num: %d\n", num);
    
    // Print the address of num
    printf("Address of num: %p\n", &num);
    
    // Print the value of num using pointer
    printf("Value using pointer: %d\n", *p);
   
    return 0;
}



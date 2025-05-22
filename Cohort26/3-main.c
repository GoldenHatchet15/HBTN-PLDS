#include "3-calc.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * main - Entry point of the program
 * @argc: The number of command-line arguments
 * @argv: An array of command-line arguments
 * Return: 0 on success, or an error code on failure
 */
int main(int argc, char *argv[])
{
    int num1, num2, result;
    int (*op_func)(int, int);

    /* Check if the number of arguments is correct */
    if (argc != 4)
    {
        printf("Error\n");
        exit(98);
    }

    /* Convert arguments to integers */
    num1 = atoi(argv[1]);
    num2 = atoi(argv[3]);

    /* Get the appropriate function for the operator */
    op_func = get_op_func(argv[2]);

    /* Check if the operator is valid */
    if (op_func == NULL)
    {
        printf("Error\n");
        exit(99);
    }

    /* Handle division by zero */
    if ((*argv[2] == '/' || *argv[2] == '%') && num2 == 0)
    {
        printf("Error\n");
        exit(100);
    }

    /* Perform the operation and print the result */
    result = op_func(num1, num2);
    printf("%d\n", result);

    return (0);
}
#include <stdio.h>
#include <assert.h>
#include <string.h>

/*
To compile and run tests:
gcc solution.c test_solution.c -o test_solution && ./test_solution
*/

char* largestGoodInteger(char* num);

int main() {
    assert(strcmp(largestGoodInteger("6777133339"), "777") == 0);  
    assert(strcmp(largestGoodInteger("2300019"), "000") == 0);    
    assert(strcmp(largestGoodInteger("42352338"), "") == 0);

    printf("All tests passed!\n");
    return 0;
}

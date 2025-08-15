#include <assert.h>
#include <stdio.h>
#include <stdbool.h>

/*
To compile and run tests:
gcc solution.c test_solution.c -o test_solution && ./test_solution
*/

bool isPowerOfFour(int n); 

int main() {
    assert(isPowerOfFour(16) == true);  
    assert(isPowerOfFour(5) == false);    
    assert(isPowerOfFour(1) == true);

    printf("All tests passed!\n");
    return 0;
}


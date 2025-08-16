#include <assert.h>
#include <stdio.h>
#include <stdbool.h>

/*
To compile and run tests:
gcc solution.c test_solution.c -o test_solution && ./test_solution <-- mac
gcc solution.c test_solution.c -o test_solution && test_solution.exe <-- windows
*/

int maximum69Number(int n); 

int main() {
    assert(maximum69Number(9669) == 9969);  
    assert(maximum69Number(9996) == 9999);    
    assert(maximum69Number(9999) == 9999);

    printf("All tests passed!\n");
    return 0;
}
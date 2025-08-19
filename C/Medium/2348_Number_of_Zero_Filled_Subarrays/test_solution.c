#include <stdio.h>
#include <assert.h>
#include <string.h>

/*
To compile and run tests:
gcc solution.c test_solution.c -o test_solution && ./test_solution <-- mac
gcc solution.c test_solution.c -o test_solution && test_solution.exe <-- windows
*/

long long zeroFilledSubarray(int* nums, int numsSize);

int main() {

    printf("Running tests...\n");

    int case1[] = {1,3,0,0,2,0,0,4};
    assert(zeroFilledSubarray(case1, 8) == 6);

    int case2[] = {0,0,0,2,0,0};
    assert(zeroFilledSubarray(case2, 6) == 9);  

    int case3[] = {2,10,2019};
    assert(zeroFilledSubarray(case3, 3) == 0);

    printf("All tests passed!\n");

    return 0;
}

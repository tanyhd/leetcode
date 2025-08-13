#include <assert.h>
#include <stdio.h>
#include <stdbool.h>

bool isPowerOfThree(int n); 

int main() {
    assert(isPowerOfThree(27) == true);  
    assert(isPowerOfThree(0) == false);    
    assert(isPowerOfThree(-1) == false);

    printf("All tests passed!\n");
    return 0;
}


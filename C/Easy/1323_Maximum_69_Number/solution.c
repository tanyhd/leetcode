#include <stdbool.h>
#include <stdio.h>

int maximum69Number (int num) {
    int size = 0;
    int temp = num;

    while (temp % 10 != 0) {
        size++;
        temp = temp / 10;
    }

    int numArray[size];
    int i = 0;
    while (num % 10 != 0) {
        numArray[i] = num%10;
        i++;
        num = num / 10;
    }

    int result = 0;
    bool hasChange = false;
    for (int i = size-1; i >= 0; i--) {
        if (!hasChange && numArray[i] == 6) {
            result = (result * 10) + 9;
            hasChange = true;
        } else {
            result = (result * 10) + numArray[i];
        }
    }
    return result;
}
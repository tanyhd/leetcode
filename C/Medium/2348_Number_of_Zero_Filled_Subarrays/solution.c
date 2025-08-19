long long zeroFilledSubarray(int* nums, int numsSize) {
    int count = 0;
    long long countTotal = 0;
    for (int i = 0; i < numsSize; i++) {
        if (nums[i] == 0) {
            count += 1;
            countTotal += count;
        } else {
            count = 0;
        }
    }
    return countTotal;
}
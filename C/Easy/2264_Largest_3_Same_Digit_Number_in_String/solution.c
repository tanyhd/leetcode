
char* largestGoodInteger(char* num) {
    int maxCount = -1;

    for (int i = 1; num[i+1] != '\0'; i++ ) {
        if (num[i-1] == num[i] && num[i] == num[i+1]) {
            int v = num[i] - '0';
            if (v > maxCount) {
                maxCount = v;
            }
        }
    }

    if (maxCount == -1) {
        return "";
    }

    static char charDigit[4];
    charDigit[0] = maxCount + '0';
    charDigit[1] = maxCount + '0';
    charDigit[2] = maxCount + '0';
    charDigit[3] = '\0';
    return charDigit;
}
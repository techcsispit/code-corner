#include <stdio.h>

void intToRoman(int num) {
    int val[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    const char *syms[] = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    for (int i = 0; i < 13; i++) {
        while (num >= val[i]) {
            printf("%s", syms[i]);
            num -= val[i];
        }
    }
    printf("\n");
}

int main(void) {
    int n;
    if (scanf("%d", &n) == 1) {
        intToRoman(n);
    }
    return 0;
}

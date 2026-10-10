#include <stdio.h>

int main(void) {
    int n;
    scanf("%d", &n);
    long long a = 0, b = 1;
    for (int i = 0; i < n; i++) {
        long long next = a + b;
        a = b;
        b = next;
    }
    printf("%lld\n", a);
    return 0;
}

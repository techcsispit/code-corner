#include <stdio.h>

int main() {
    long long n, count = 0;

    scanf("%lld", &n);

    if (n <= 1) {
        printf("not prime\n");
        return 0;
    }

    for (int i = 2; i <= n / 2; i++) {
        if (n % i == 0) {
            count++;
            break;
        }
    }

    if (count == 0) {
        printf("prime\n");
    } else {
        printf("not prime\n");
    }

    return 0;
}

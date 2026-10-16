#include <stdio.h>

int is_prime(long long n) {
    if (n < 2) {
        return 0;
    }
    if (n % 2 == 0) {
        return n == 2;
    }

    for (long long divisor = 3; divisor <= n / divisor; divisor += 2) {
        if (n % divisor == 0) {
            return 0;
        }
    }

    return 1;
}

int main(void) {
    long long n;
    scanf("%lld", &n);

    printf("%s\n", is_prime(n) ? "prime" : "not prime");

    return 0;
}

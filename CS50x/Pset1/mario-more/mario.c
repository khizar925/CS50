#include <stdio.h>
#include <cs50.h>
int main(void) {
    int n;
    n = get_int("Height :");

    while (n <= 0 || n > 8) {
        n = get_int("Height :");
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j < n - i; j++) {
            printf(" ");
        }
        for (int k = 0; k < i; k++) {
            printf("#");
        }
        printf("  ");
        for (int l = 0; l < i; l++) {
            printf("#");
        }
        printf("\n");
    }

    return 0;
}

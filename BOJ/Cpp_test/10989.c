#include <stdio.h>
#include <stdlib.h>

void counting_sort(int arr[], int n) {
    int max_val = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max_val) {
            max_val = arr[i];
        }
    }

    int* counts = (int*)calloc(max_val + 1, sizeof(int));
    if (counts == NULL) {
        return;
    }

    for (int i = 0; i < n; i++) {
        counts[arr[i]]++;
    }

    int idx = 0;
    for (int i = 0; i <= max_val; i++) {
        while (counts[i] > 0) {
            arr[idx++] = i;
            counts[i]--;
        }
    }

    free(counts);
}

int main() {
    int k;
    scanf("%d", &k);

    int* l = (int*)malloc(k * sizeof(int));
    if (l == NULL) {
        return 1;
    }

    for (int i = 0; i < k; i++) {
        scanf("%d", &l[i]);
    }

    counting_sort(l, k);
    for (int i = 0; i < k; i++) {
        printf("%d\n", l[i]);
    }
    printf("\n");

    free(l);

    return 0;
}
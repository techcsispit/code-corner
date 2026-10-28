#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int target;
    if (scanf("%d", &target) != 1) {
        return 0;
    }

    int capacity = 16;
    int size = 0;
    int *nums = malloc(capacity * sizeof(int));
    if (!nums) {
        return 1;
    }

    int num;
    while (scanf("%d", &num) == 1) {
        if (size >= capacity) {
            capacity *= 2;
            int *new_nums = realloc(nums, capacity * sizeof(int));
            if (!new_nums) {
                free(nums);
                return 1;
            }
            nums = new_nums;
        }
        nums[size++] = num;
    }

    int low = 0;
    int high = size - 1;
    int ans = -1;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (nums[mid] == target) {
            ans = mid;
            break;
        } else if (nums[mid] < target) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }

    printf("%d\n", ans);

    free(nums);
    return 0;
}

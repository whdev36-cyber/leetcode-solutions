#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// ===================== twoSum =====================
// Returns the indices of the two numbers that add up to 'target'
// Note: The returned array must be malloced, assume caller calls free().
int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    *returnSize = 2;
    int* result = (int*)malloc(2 * sizeof(int));

    for (int i = 0; i < numsSize; i++) {
        for (int j = i + 1; j < numsSize; j++) {
            if (nums[i] + nums[j] == target) {
                result[0] = i;
                result[1] = j;
                return result;
            }
        }
    }

    *returnSize = 0; // No solution found
    free(result);
    return NULL;
}

int main() {
    // --- twoSum Example ---
    int nums[] = {2, 7, 11, 15};
    int target = 9;
    int returnSize;
    int* result = twoSum(nums, 4, target, &returnSize);
    if (result != NULL) {
        printf("twoSum: [%d, %d]\n", result[0], result[1]);
        free(result);
    } else {
        printf("No two numbers add up to the target.\n");
    }
    return 0;
}

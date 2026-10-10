import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    static int search(int[] nums, int target) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) return mid;
            if (nums[mid] < target) lo = mid + 1;
            else hi = mid - 1;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] values = Arrays.stream(new Scanner(System.in).nextLine().trim().split("\\s+")).mapToInt(Integer::parseInt).toArray();
        System.out.println(search(Arrays.copyOfRange(values, 1, values.length), values[0]));
    }
}

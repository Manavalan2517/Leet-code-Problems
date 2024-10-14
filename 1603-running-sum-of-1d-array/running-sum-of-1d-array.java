import java.util.*;
class Solution {
    public int[] runningSum(int[] nums) {
        int[] res = new int[nums.length];
        int tempSum;
        for (int i = 0; i < nums.length; i++) {
            tempSum = 0;
            for (int j = 0; j <= i; j++) {
                tempSum += nums[j];
            }
            res[i] = tempSum;
        }
        return res;
    }
}
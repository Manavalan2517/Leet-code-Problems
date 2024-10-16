class Solution {
    public int[] shuffle(int[] nums, int n) {
        int len = nums.length;
        int indexNum = 0;
        int[] res = new int[len];
        for(int i=0; i<(len/2); i++){
            int x = nums[i];
            int y = nums[(len/2)+i];
            res[indexNum] = x;
            indexNum++;
            res[indexNum] = y;
            indexNum++;
        }
        return res;
    }
}
class Solution {
    public int maximumWealth(int[][] accounts) {
        int sum;
        int max = 0;
        for (int[] i: accounts){
            sum = 0;
            for(int j: i){
                sum += j;
            }
            if (sum > max){
                max = sum;
            }
        }
        return max;
    }
}
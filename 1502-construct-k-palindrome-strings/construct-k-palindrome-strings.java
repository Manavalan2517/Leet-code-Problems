class Solution {
    public boolean canConstruct(String s, int k) {
        if (k > s.length()) return false;
        int oddCount = 0;
        int[] freq = new int[26];
        for (char c : s.toCharArray()) {
            freq[c - 'a']++;
        }
        for (int count : freq) {
            if (count % 2 != 0) oddCount++;
        }
        return k >= oddCount;
    }
}
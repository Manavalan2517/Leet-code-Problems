class Solution {
    public List<String> wordSubsets(String[] words1, String[] words2) {
        int[] words2Count = new int[26];
        for (String word : words2) {
            int[] tempCount = new int[26];
            for (char c : word.toCharArray()) {
                tempCount[c - 'a']++;
            }
            for (int i = 0; i < 26; i++) {
                words2Count[i] = Math.max(words2Count[i], tempCount[i]);
            }
        }

        List<String> result = new ArrayList<>();
        for (String word : words1) {
            int[] wordCount = new int[26];
            for (char c : word.toCharArray()) {
                wordCount[c - 'a']++;
            }
            boolean isUniversal = true;
            for (int i = 0; i < 26; i++) {
                if (wordCount[i] < words2Count[i]) {
                    isUniversal = false;
                    break;
                }
            }
            if (isUniversal) {
                result.add(word);
            }
        }
        System.out.println(result);
        return result;
    }
}
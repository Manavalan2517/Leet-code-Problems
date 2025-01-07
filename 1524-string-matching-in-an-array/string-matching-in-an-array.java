class Solution {
    public List<String> stringMatching(String[] words) {
        ArrayList<String> result = new ArrayList<String>();
        for (int i = 0; i < words.length ; i++) {
            for (int j = 0; j < words.length ; j++) {
                if (words[j].contains(words[i]) && !words[j].equals(words[i])) {
                    if (!result.contains(words[i])){
                        result.add(words[i]);
                    }
                }
            }
        }
        return result;
    }
}
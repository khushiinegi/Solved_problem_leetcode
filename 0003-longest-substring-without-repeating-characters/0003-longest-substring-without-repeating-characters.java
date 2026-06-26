class Solution {
    public int lengthOfLongestSubstring(String s) 
    {
        int n = s.length();
        int maxLen = 0;
        for (int i = 0; i < n; i++) {
            boolean[] visited = new boolean[256]; 
            int currLen = 0;
            for (int j = i; j < n; j++) {
                char c = s.charAt(j);
                if (visited[c]) {
                    break; 
                }
                visited[c] = true;
                currLen++;
            }
            if (currLen > maxLen) {
                maxLen = currLen;
            }
        }
        return maxLen;
    }
}
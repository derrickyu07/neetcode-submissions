class Solution {
    public String longestPalindrome(String s) {
        int resIdx = 0;
        int resLen = 0;
        for (int i = 0; i < s.length();i++){
            int r = i;
            int l = i;
            while (l >= 0 && r < s.length() && s.charAt(r) == s.charAt(l)){
                if (resLen < r-l +1){
                    resLen = r-l+1;
                    resIdx = l;
                }
                l--;
                r++;
            }
            r = i + 1;
            l = i;
            while (l >= 0 && r < s.length() && s.charAt(r) == s.charAt(l)){
                if (resLen < r-l +1){
                    resLen = r-l+1;
                    resIdx = l;
                }
                l--;
                r++;
            }
        }
        return s.substring(resIdx,resLen+ resIdx);
    }
}

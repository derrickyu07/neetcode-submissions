class Solution {
    public int countSubstrings(String s) {
        int res = 0;
        for (int i = 0; i < s.length();i++){
            int r = i;
            int l = i;
            while (l >= 0 && r < s.length() && s.charAt(r) == s.charAt(l)){
                res++;
                l--;
                r++;
            }
            r = i + 1;
            l = i;
            while (l >= 0 && r < s.length() && s.charAt(r) == s.charAt(l)){
                res++;
                l--;
                r++;
            }
        }
        return res;
    }
}

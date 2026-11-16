class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character> sSet = new HashSet();
        int l = 0;
        int res = 0;
        for (int r = 0; r < s.length(); r++){
            while (sSet.contains(s.charAt(r))){
                sSet.remove(s.charAt(l));
                l++;
            }
            sSet.add(s.charAt(r));
            res = Math.max(res,sSet.size());
        }
        return res;
    }
}

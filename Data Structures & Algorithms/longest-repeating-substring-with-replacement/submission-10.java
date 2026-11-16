class Solution {
    public int characterReplacement(String s, int k) {
        Map<Character,Integer> sMap = new HashMap<>();
        int l = 0;
        int maxFreq = 0;
        int res = 0;

        for (int i = 0; i < s.length(); i++){
            sMap.put(s.charAt(i), sMap.getOrDefault(s.charAt(i),0)+1);
            maxFreq = Math.max(maxFreq, sMap.get(s.charAt(i)));

            while (i - l - maxFreq + 1 > k){
                sMap.put(s.charAt(l),sMap.get(s.charAt(l))-1);
                l++;
            }
            res = Math.max(res,i-l+1);

        }
        return res;


    }
}

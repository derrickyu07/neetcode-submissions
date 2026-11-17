class Solution {
    public String minWindow(String s, String t) {

        if (t.isEmpty()) return "";

        int have = 0;
        Map<Character,Integer> sMap = new HashMap<>();
        Map<Character, Integer> tMap = new HashMap<>();

        for (int i = 0; i < t.length();i++){
            tMap.put(t.charAt(i),tMap.getOrDefault(t.charAt(i),0)+1);
        }
        int need = tMap.size();
        int resLen = Integer.MAX_VALUE;
        int[] res = {-1,-1};
        int l = 0;
        

        for (int r = 0; r < s.length(); r++){
            char c = s.charAt(r);
            sMap.put(c,sMap.getOrDefault(c,0)+1);

            if (tMap.containsKey(c) && tMap.get(c).equals(sMap.get(c))){
                have++;
            }

            while (need == have){
                if (resLen > r-l+1){
                    resLen = r-l+1;
                    res[0] = l;
                    res[1] = r;
                }
                sMap.put(s.charAt(l),sMap.get(s.charAt(l))-1);
                if (tMap.containsKey(s.charAt(l)) && sMap.get(s.charAt(l)) < tMap.get(s.charAt(l))){
                    have--;
                }
                l++;
            }
        }

        return resLen == Integer.MAX_VALUE ? "":s.substring(res[0],res[1]+1);
    }
}

class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        List<Integer>[] freq = new List[nums.length+1];
        Map<Integer, Integer> numDict = new HashMap();

        for (int i=0;i<freq.length;i++){
            freq[i] = new ArrayList();
        }

        for (int num: nums){
            numDict.put(num,numDict.getOrDefault(num,0)+1);
        } 
        for (Map.Entry<Integer,Integer> entry: numDict.entrySet()) {
            freq[entry.getValue()].add(entry.getKey());
        }
        int[] res = new int[k];
        int index = 0;
        for (int i = freq.length-1; i > 0 && index < k; i--){
            for (int j: freq[i]){
                res[index++] = j;
                if (index == k){
                    return res;
                }
            }
        }
        return res;
    }
}

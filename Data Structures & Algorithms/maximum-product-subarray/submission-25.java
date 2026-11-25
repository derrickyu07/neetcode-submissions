class Solution {
    public int maxProduct(int[] nums) {
        int numMax = 1;
        int numMin = 1;
        int res = nums[0];
        for (int num: nums){
            int minTmp = num * numMin;
            int maxTmp = num * numMax;
            numMax = Math.max(Math.max(maxTmp, minTmp), num);
            numMin = Math.min(Math.min(minTmp, maxTmp),num);
            res = Math.max(res, numMax);
        }
        return res;
    }
}

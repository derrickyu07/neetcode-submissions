class Solution {
    public int maxSubArray(int[] nums) {
        int total = 0;
        int res = nums[0];
        for (int num: nums){
            total += num;
            res = Math.max(res, total);
            if (total < 0){
                total = 0;
            }
        }
        return res;
    }
}

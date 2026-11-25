class Solution {
    public int rob(int[] nums) {
        return Math.max( Math.max(helper(Arrays.copyOfRange(nums,1,nums.length)),                helper(Arrays.copyOfRange(nums,0,nums.length-1))),
        nums[0]);
    }
    public int helper(int[] nums) {
        int rob1 = 0;
        int rob2 = 0;

        for (int num: nums){
            int tmp = Math.max(rob1 + num, rob2);
            rob1 = rob2;
            rob2 = tmp;
        }
        return rob2;
    }
}

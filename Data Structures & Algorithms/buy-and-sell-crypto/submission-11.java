class Solution {
    public int maxProfit(int[] prices) {
        int lowest = prices[0];
        int res = 0;
        for (int price : prices){
            lowest = Math.min(lowest,price);
            res = Math.max(res,price- lowest);
        }
        return res;
    }
}

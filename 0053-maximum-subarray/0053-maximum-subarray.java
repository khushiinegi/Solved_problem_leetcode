class Solution {
    public int maxSubArray(int[] nums) 
    {
        int sum =0;
        int MaxSum = nums[0];
        for(int i=0;i<nums.length;i++){
            sum = sum+nums[i] ;
            if(sum > MaxSum){
                MaxSum = sum;
            }
            if(sum<0){
                sum =0;
            }
        }
        return MaxSum;
    }
}
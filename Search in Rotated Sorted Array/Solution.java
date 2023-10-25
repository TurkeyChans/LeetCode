class Solution {
    public int search(int[] nums, int target) {
        for(int i = 0; i < nums.length; ++i) {
            if(target == nums[i])
                return i;
        }
        return -1;
    }
    
    /* 
    public static void main(String[] args) {
        Solution search = new Solution();
        int[] nums = {10,20,30,40,50,60,70,80,90,100};
        System.out.print(search.search(nums,10));
        System.out.println();
        System.out.print(search.search(nums,50));  
        System.out.println();
        System.out.print(search.search(nums,100)); 
        System.out.println();
        System.out.print(search.search(nums,5)); 
    }
    */
}
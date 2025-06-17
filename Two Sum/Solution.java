public class Solution {
   
    public int[] twoSum(int[] nums, int target) {
        int array[] = new int[2];
        boolean stop = false;
        for(int i = 0; i < nums.length; ++i) {
            for(int j = 0; j < nums.length; ++j) {
                if(i != j && nums[i] + nums[j] == target) {
                    array[0] = i;
                    array[1] = j;
                    stop = true;
                    break;  
                }
            }
            if(stop) {
                break;
            }
        }
        return array;
    }
public static void main(String[] args) {
   Solution test = new Solution();
   int[] g = {3,2,-5,-3};
   int[] s = test.twoSum(g,-2);
   for(int i = 0; i < s.length; ++i) {
    System.out.println(s[i]);
   }
}
}

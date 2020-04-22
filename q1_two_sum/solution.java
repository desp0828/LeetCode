#hashmap
class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> remainValues = new HashMap<Integer,Integer>();
        
        for(int i=0; i<nums.length; ++i){
            if(remainValues.containsKey(nums[i])){
                int anotherIndex = remainValues.get(nums[i]);
                return new int[]{anotherIndex,i};
            }
            remainValues.put((target-nums[i]),i);
        }
        return new int[]{-1,-1};
        
    }
}


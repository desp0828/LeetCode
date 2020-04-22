'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

# two pointers

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a,b = 0,len(nums)-1
        array = nums.copy()
        nums.sort()
        if b==0:
            return('Error')
        while(b>a):
            if (nums[a]+nums[b])>target:
                b-=1
            elif (nums[a]+nums[b])<target:
                a+=1
            else:
                break
        res = []
        for i in range(len(nums)):
            if (array[i]==nums[a]) or (array[i]==nums[b]):
                res.append(i)
        return(res)    
# hashmap
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            if nums[i] not in map:
                map[target-nums[i]] = i
            else:
                return(map[nums[i]],i)

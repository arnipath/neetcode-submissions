class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                if dict[target-nums[i]] <= i:
                    return [dict[target-nums[i]], i]
                else:
                    return [i, dict[target-nums[i]]]
            dict[nums[i]] = i

        
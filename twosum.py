class Solution(object):
    def twoSum(self, nums, target):
        h_map = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in h_map:
                return [h_map[diff], i]
            h_map[n] = i
        return []

#so we use hashmap here to bassically store our values 
#we know that our target - i would be in the list somewhere the answer is that where would it appear
#ideally we would like it to apear before where diff = target - index if diff is already in hashmap we can just returen the index
#if not we keep adding 
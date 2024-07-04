class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1

        l = [[nums[k], k] for k in range(len(nums))]
        l.sort()

        while True:
            if i >= j:
                return None

            if l[i][0] + l[j][0] == target:
                return [l[i][1], l[j][1]]
            elif l[i][0] + l[j][0] > target:
                j -= 1
            else:
                i += 1

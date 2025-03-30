nums = input()
i = 0
n = 1

while i<len(nums):
    curr = str(n)
    for c in curr:
        if i < len(nums) and c == nums[i]:
            i += 1
    n += 1

print(n-1)
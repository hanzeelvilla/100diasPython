nums = [20, 10, 1, 4, 3, 15, 8, 25, 12, 7, 18, 2, 9, 14, 6, 22, 11, 16, 5, 13]

max = nums[0]

for n in nums:
    if n > max:
        max = n

print(max)
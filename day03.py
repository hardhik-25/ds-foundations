def oddsum(nums):
    total=0
    for i in range(len(nums)):
        if nums[i]%2 != 0:
            total += nums[i]
    return total

print(oddsum([1, 2, 3, 4, 5]))
            
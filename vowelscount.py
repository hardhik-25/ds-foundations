def vowelcount(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] in 'aeiou':
            count += 1
    return count
print(vowelcount('hello'))

        

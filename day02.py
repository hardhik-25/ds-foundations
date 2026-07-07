
def twosum(nums, target):
    for i in range(len(nums)):
       for j in range(i+1,len(nums)): 
            if nums[i] + nums[j] == target:
                return [i,j]
nums = [3,2,4]
target = 6
print(twosum(nums, target))


# Write a function that takes a list of numbers and a target. Return True if any 
# two numbers in the list add up to the target, and False if they don't.
def truesum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False
nums = [1,4,6,8]
target=10
print(truesum(nums,target))

nums = [1,4,6,8]
target = 3
print(truesum(nums,target))

#revision
def TrueSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return True
    return False

print(TrueSum([1, 4, 6, 8], 10))
print(TrueSum([1, 4, 6, 8], 3))
# Given a list of numbers containing one duplicate and only one duplicated value,
# return the duplicated value.  That value will only be duplicated once.
# Input:
# [1, 2, 3, 2, 4]
# Output:
# 2
# Input:
# [5,8,5,2,3,4]
# Output:
# 5

def solution(nums):
    seen_once = set()
    for num in nums:
        if num in seen_once:
            return num
        else:
            seen_once.add(num)
    return -1



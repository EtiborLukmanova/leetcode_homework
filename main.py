# TASK 1


class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        count1 = sum(1 for num in nums1 if num in set_nums2)
        count2 = sum(1 for num in nums2 if num in set_nums1)

        return [count1, count2]


#TASK 2


class Solution:
    def minimumAddedCoins(self, coins, target):
        coins.sort()
        sum_val = 0
        ans = 0

        for coin in coins:
            while coin > sum_val + 1:
                ans += 1
                sum_val += sum_val + 1
            sum_val += coin

        while sum_val < target:
            sum_val += sum_val + 1
            ans += 1
        return ans


#TASK 3


class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        count1 = sum(1 for num in nums1 if num in set_nums2)
        count2 = sum(1 for num in nums2 if num in set_nums1)

        return [count1, count2]
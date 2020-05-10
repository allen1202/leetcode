import  collections

class Solution():
    def maxSlidingWindow(self, nums, k):
        deque= collections.deque()
        res = []

        for i, num in enumerate(nums):
            while deque and deque[0] <= i -k:
                deque.popleft()

            while deque and num > nums[deque[-1]]:
                deque.pop()

            deque.append(i)
            if i >= k-1:
                res.append(nums[deque[0]])

        return res


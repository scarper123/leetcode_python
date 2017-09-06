class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # max_len = len(nums)
        # inx1 = 0
        # while inx1 < max_len - 1:
        #     inx2 = inx1 + 1
        #     while inx2 < max_len:
        #         if nums[inx1] + nums[inx2] == target:
        #             return [inx1, inx2]
        #         inx2 += 1
        #
        #     inx1 += 1

        # seen = {}
        # for i, v in enumerate(nums):
        #     if v in seen:
        #         return [seen[v], i]
        #     else:
        #         seen[target - v] = i

        buffer_dict = {}
        for inx in range(len(nums)):
            if nums[inx] in buffer_dict:
                return [buffer_dict[nums[inx]], inx]

            else:
                buffer_dict[target - nums[inx]] = inx


if __name__ == '__main__':
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 17) == [0, 3]

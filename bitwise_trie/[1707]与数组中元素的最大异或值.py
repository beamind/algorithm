# 给你一个由非负整数组成的数组 nums 。另有一个查询数组 queries ，其中 queries[i] = [xi, mi] 。
#
#  第 i 个查询的答案是 xi 和任何 nums 数组中不超过 mi 的元素按位异或（XOR）得到的最大值。换句话说，答案是 max(nums[j] XOR
#  xi) ，其中所有 j 均满足 nums[j] <= mi 。如果 nums 中的所有元素都大于 mi，最终答案就是 -1 。
#
#  返回一个整数数组 answer 作为查询的答案，其中 answer.length == queries.length 且 answer[i] 是第 i 个
# 查询的答案。
#
#
#
#  示例 1：
#
#  输入：nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
# 输出：[3,3,7]
# 解释：
# 1) 0 和 1 是仅有的两个不超过 1 的整数。0 XOR 3 = 3 而 1 XOR 3 = 2 。二者中的更大值是 3 。
# 2) 1 XOR 2 = 3.
# 3) 5 XOR 2 = 7.
#
#
#  示例 2：
#
#  输入：nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
# 输出：[15,-1,5]
#
#
#
#
#  提示：
#
#
#  1 <= nums.length, queries.length <= 105
#  queries[i].length == 2
#  0 <= nums[j], xi, mi <= 109
#
#  Related Topics 位运算 字典树
#  👍 23 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:

        # 离线思想 + 字典树：对queries按mi升序排列，这样就可以一边计算答案一边更新字典树

        d = {'0': '1', '1': '0'}

        # 对queries排序
        nq = len(queries)
        for i in range(nq):
            queries[i].append(i)
        queries.sort(key=lambda x: x[1])

        # 对nums排序
        nums = sorted(list(set(nums)))
        n = len(nums)

        trie = {}
        ans = []
        i, j = 0, 0
        while j < nq:
            # 把nums中每个小于等于mi的数加入字典树
            while i < n and nums[i] <= queries[j][1]:
                x = bin(nums[i])[2:]
                x = '0' * (32 - len(x)) + x  # 二进制位数补充至32位
                t = trie
                for c in x:
                    if c not in t:
                        t[c] = {}
                    t = t[c]
                i += 1

            # 如果nums中所有元素都大于mi，则答案是-1
            if not trie:
                ans.append([queries[j][2], -1])
                j += 1
                continue

            # 把xi转化为二进制
            q = bin(queries[j][0])[2:]
            q = '0' * (32 - len(q)) + q  # 二进制位数补充至32位

            # 遍历字典树
            t = trie
            res = 0
            for k, c in enumerate(q):
                if d[c] in t:
                    res = (res << 1) + 1
                    t = t[d[c]]
                else:
                    res = res << 1
                    t = t[c]
            ans.append([queries[j][2], res])
            j += 1
        ans.sort()
        return [res for _, res in ans]


if __name__ == '__main__':
    s = Solution()
    print(s.maximizeXor(nums=[0, 1, 2, 3, 4], queries=[[3, 1], [1, 3], [5, 6]]))
# leetcode submit region end(Prohibit modification and deletion)

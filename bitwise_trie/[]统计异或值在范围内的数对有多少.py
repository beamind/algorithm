# 给你一个整数数组 nums （下标 从 0 开始 计数）以及两个整数：low 和 high ，请返回 漂亮数对 的数目。
#
#  漂亮数对 是一个形如 (i, j) 的数对，其中 0 <= i < j < nums.length 且 low <= (nums[i] XOR nums[
# j]) <= high 。
#
#
#
#  示例 1：
#
#  输入：nums = [1,4,2,7], low = 2, high = 6
# 输出：6
# 解释：所有漂亮数对 (i, j) 列出如下：
#     - (0, 1): nums[0] XOR nums[1] = 5
#     - (0, 2): nums[0] XOR nums[2] = 3
#     - (0, 3): nums[0] XOR nums[3] = 6
#     - (1, 2): nums[1] XOR nums[2] = 6
#     - (1, 3): nums[1] XOR nums[3] = 3
#     - (2, 3): nums[2] XOR nums[3] = 5
#
#
#  示例 2：
#
#  输入：nums = [9,8,4,2,1], low = 5, high = 14
# 输出：8
# 解释：所有漂亮数对 (i, j) 列出如下：
# ​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
#     - (0, 3): nums[0] XOR nums[3] = 11
#     - (0, 4): nums[0] XOR nums[4] = 8
#     - (1, 2): nums[1] XOR nums[2] = 12
#     - (1, 3): nums[1] XOR nums[3] = 10
#     - (1, 4): nums[1] XOR nums[4] = 9
#     - (2, 3): nums[2] XOR nums[3] = 6
#     - (2, 4): nums[2] XOR nums[4] = 5
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 2 * 104
#  1 <= nums[i] <= 2 * 104
#  1 <= low <= high <= 2 * 104
#
#  Related Topics 字典树
#  👍 5 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.cnt = 0
        self.sons = collections.defaultdict(dict)


class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        # 思路：字典树 + 剪枝

        def dfs(i, trie, val, p):
            nonlocal ans
            b = int(bit[i])

            # 走不增值的一枝
            if trie.sons[b]:
                # 如果该节点以下节点全部满足要求，则不需继续遍历判断，可直接利用节点数
                if val >= low and val + (1 << p) - 1 <= high:
                    ans += trie.sons[b].cnt
                # 只有该节点以下节点既有可能满足要求也有可能不满足要求时才需递归判断
                elif val <= high and val + (1 << p) > low:
                    dfs(i + 1, trie.sons[b], val, p - 1)

            # 走增值的一枝
            if trie.sons[1 - b]:
                val2 = val + (1 << p)
                # 如果该节点以下节点全部满足要求，则不需继续遍历判断，可直接利用节点数
                if val2 >= low and val2 + (1 << p) - 1 <= high:
                    ans += trie.sons[1 - b].cnt
                # 只有该节点以下节点既有可能满足要求也有可能不满足要求时才需递归判断
                elif val2 <= high and val2 + (1 << p) > low:
                    dfs(i + 1, trie.sons[1 - b], val2, p - 1)

        # 构造字典树
        trie = TrieNode()
        for n in nums:
            bit = bin(n)[2:]
            bit = '0' * (15 - len(bit)) + bit  # 二进制位数补充至32位
            t = trie
            t.cnt += 1
            for b in bit:
                b = int(b)
                if not t.sons[b]:
                    t.sons[b] = TrieNode()
                t = t.sons[b]
                t.cnt += 1

        ans = 0
        for n in nums:
            bit = bin(n)[2:]
            bit = '0' * (15 - len(bit)) + bit  # 二进制位数补充至32位
            dfs(0, trie, 0, 14)
        return ans // 2


if __name__ == '__main__':
    s = Solution()
    print(s.countPairs(nums=[1, 4, 2, 7], low=2, high=6))

# leetcode submit region end(Prohibit modification and deletion)

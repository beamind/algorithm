# 给你一个整数数组 nums 和一个整数 k 。你需要将这个数组划分到 k 个相同大小的子集中，使得同一个子集里面没有两个相同的元素。 
# 
#  一个子集的 不兼容性 是该子集里面最大值和最小值的差。 
# 
#  请你返回将数组分成 k 个子集后，各子集 不兼容性 的 和 的 最小值 ，如果无法分成分成 k 个子集，返回 -1 。 
# 
#  子集的定义是数组中一些数字的集合，对数字顺序没有要求。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,1,4], k = 2
# 输出：4
# 解释：最优的分配是 [1,2] 和 [1,4] 。
# 不兼容性和为 (2-1) + (4-1) = 4 。
# 注意到 [1,1] 和 [2,4] 可以得到更小的和，但是第一个集合有 2 个相同的元素，所以不可行。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [6,3,8,1,3,1,2,2], k = 4
# 输出：6
# 解释：最优的子集分配为 [1,2]，[2,3]，[6,8] 和 [1,3] 。
# 不兼容性和为 (2-1) + (3-2) + (8-6) + (3-1) = 6 。
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [5,3,3,6,3,3], k = 3
# 输出：-1
# 解释：没办法将这些数字分配到 3 个子集且满足每个子集里没有相同数字。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 16 
#  nums.length 能被 k 整除。 
#  1 <= nums[i] <= nums.length 
#  
#  Related Topics 贪心算法 回溯算法 
#  👍 7 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections
from typing import List


class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:

        count = collections.Counter(nums)
        if max(count.values()) > k:
            return -1

        n = len(nums)
        if k == 1:
            return max(nums) - min(nums)
        elif k == n:
            return 0

        # 筛选满足条件的子集(子集元素个数为m且子集没有重复元素)，并计算其不兼容性。
        m = n // k  # 子集的元素个数
        subs = {}
        for i in range(1 << n):
            if bin(i).count('1') != m:
                continue
            s = set()
            for t in range(n):
                if i & (1 << t) > 0:
                    if nums[t] in s:
                        break
                    else:
                        s.add(nums[t])
            else:
                subs[i] = max(s) - min(s)

        dp = [-1] * (1 << n)
        dp[0] = 0
        for i in range(1 << n):  # 遍历每一个状态
            if bin(i).count('1') % m == 0:  # 选中的元素个数必须是m的整数倍
                for k, v in subs.items():  # 遍历每一个子集，选出当前状态的最小不兼容性
                    if i & k == k:  # 当前状态的选中元素必须包含子集元素
                        x = i ^ k  # 前一个状态，即从当前状态选中的元素中把子集元素排除
                        if dp[x] > -1:  # 前一个状态必须可达
                            if dp[i] == -1:
                                dp[i] = dp[x] + v
                            else:
                                dp[i] = min(dp[i], dp[x] + v)
        return dp[-1]


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    print(s.minimumIncompatibility([1, 2, 1, 4], 2))

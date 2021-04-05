# 给出一个字符串 S，考虑其所有重复子串（S 的连续子串，出现两次或多次，可能会有重叠）。
#
#  返回任何具有最长可能长度的重复子串。（如果 S 不含重复子串，那么答案为 ""。）
#
#
#
#  示例 1：
#
#  输入："banana"
# 输出："ana"
#
#
#  示例 2：
#
#  输入："abcd"
# 输出：""
#
#
#
#
#  提示：
#
#
#  2 <= S.length <= 10^5
#  S 由小写英文字母组成。
#
#  Related Topics 哈希表 二分查找
#  👍 110 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
import collections


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        n = len(s)
        d = collections.defaultdict(list)
        for i, c in enumerate(s):
            d[c].append(i)
        cand = {k: v for k, v in d.items() if len(v) > 1}
        if not cand:
            return ''
        ans = ''
        b, e = 1, n - 1
        while b <= e:
            m = (b + e) // 2
            d = collections.defaultdict(list)
            for k, vs in cand.items():
                ans = k
                for i in vs:
                    d[s[i:i + m]].append(i)
            cand2 = {k: v for k, v in d.items() if len(v) > 1}
            if cand2:
                b = m + 1
                cand = cand2
                ans = list(cand2.keys())[0]
            else:
                e = m - 1
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.longestDupSubstring('banana'))
# leetcode submit region end(Prohibit modification and deletion)

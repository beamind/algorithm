# 给定一个字符串 s，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。
#
#
#
#  示例 1：
#
#
# 输入：s = "aacecaaa"
# 输出："aaacecaaa"
#
#
#  示例 2：
#
#
# 输入：s = "abcd"
# 输出："dcbabcd"
#
#
#
#
#  提示：
#
#
#  0 <= s.length <= 5 * 104
#  s 仅由小写英文字母组成
#
#  Related Topics 字符串
#  👍 316 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        next = [0] * n
        next[0] = -1
        i = -1
        for j in range(1, n):
            while i > -1 and s[i + 1] != s[j]:
                i = next[i]
            if s[i + 1] == s[j]:
                i += 1
            next[j] = i

        rev = s[::-1]
        i = 0
        for j in range(n):
            while i > 0 and rev[j] != s[i]:
                i = next[i - 1] + 1
            if rev[j] == s[i]:
                i += 1
                if j == n - 1:
                    return s[i:][::-1] + s
# leetcode submit region end(Prohibit modification and deletion)

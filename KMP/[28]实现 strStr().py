# 实现 strStr() 函数。
#
#  给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如
# 果不存在，则返回 -1。
#
#  示例 1:
#
#  输入: haystack = "hello", needle = "ll"
# 输出: 2
#
#
#  示例 2:
#
#  输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
#
#
#  说明:
#
#  当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
#  对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
#  Related Topics 双指针 字符串
#  👍 686 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        if n == 0:
            return 0

        # 对模式串进行预处理来支持在文本中的快速查找
        next = [0] * n
        next[0] = -1
        i = -1
        for j in range(1, n):
            while i > -1 and needle[i + 1] != needle[j]:
                i = next[i]
            if needle[i + 1] == needle[j]:
                i += 1
            next[j] = i

        # 匹配过程中文本串的指针i永远不回退
        j = 0
        for i in range(m):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1] + 1
            if haystack[i] == needle[j]:
                j += 1
                if j == n:
                    return i - n + 1
        return -1


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    print(s.strStr(haystack="hello", needle="ll"))

class Solution(object):
    def longestCommonPrefix(self, strs):
        shortest_str_len = len(min(strs, key=len))
        prefix = ""

        if len(strs) == 1:
            return strs[0]

        for i in range(1, shortest_str_len + 1):
            prefix = strs[0][:i]
            for s in strs:
                if prefix != s[:i]:
                    rtn = strs[0][:i-1]

                    return rtn if bool(rtn) else ""

        return prefix


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
print(Solution().longestCommonPrefix(["dog"]))
print(Solution().longestCommonPrefix(["ab", "a"]))

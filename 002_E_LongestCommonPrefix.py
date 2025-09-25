def longestCommonPrefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1] # remove last character
            if not prefix:
                return ""
    return prefix
def longestCommonsuffix(strs):
    if not strs:
        return ""
    suffix = strs[0]
    for s in strs[1:]:
        while not s.endswith(suffix):
            suffix = suffix[1:] # remove first character
            if not suffix:
                return ""
    return suffix
# Example usage:
if __name__ == "__main__":
    arr = ["flower", "flow", "flight"]
    print(arr,"common prefix:",longestCommonPrefix(arr))  # Output: "fl"
    arr2 = ["dog", "racecar", "car"]
    print(arr2,"common prefix:",longestCommonPrefix(arr2))  # Output: ""
    arr3 = ["interspecies", "interstellar", "interstate"]
    print(arr3,"common prefix:",longestCommonPrefix(arr3))  # Output: "inters"
    arr4 = ["goof", "poof", "droof"]
    print(arr4,"common suffix:",longestCommonsuffix(arr4))  # Output: "oof"
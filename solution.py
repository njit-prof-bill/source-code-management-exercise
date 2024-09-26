def longest_substring_k_unique(s: str, k: int) -> int:
    if k == 0 or not s:
        return 0

    left = 0
    max_length = 0
    char_count = {}

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        if len(char_count) == k:
            max_length = max(max_length, right - left + 1)

    return max_length

# Test cases
if __name__ == "__main__":
    print(longest_substring_k_unique("araaci", 2))  # Output: 4
    print(longest_substring_k_unique("cbbebi", 3))  # Output: 5
    print(longest_substring_k_unique("aa", 1))      # Output: 2
    print(longest_substring_k_unique("a", 1))       # Output: 1
    print(longest_substring_k_unique("abc", 2))     # Output: 2
    print(longest_substring_k_unique("abaccc", 2))  # Output: 5

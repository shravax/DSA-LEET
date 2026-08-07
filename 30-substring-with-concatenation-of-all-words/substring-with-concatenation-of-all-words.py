class Solution:
    def findSubstring(self, s, words):
        from collections import Counter

        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        word_freq = Counter(words)
        result = []

        for offset in range(word_len):
            left = offset
            right = offset
            count = 0
            current = Counter()

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_freq:
                    current[word] += 1
                    count += 1

                    while current[word] > word_freq[word]:
                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == word_count:
                        result.append(left)

                        left_word = s[left:left + word_len]
                        current[left_word] -= 1
                        left += word_len
                        count -= 1
                else:
                    current.clear()
                    count = 0
                    left = right

        return result
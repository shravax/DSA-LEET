class Solution:
    def fullJustify(self, words, maxWidth):
        res = []
        i = 0

        while i < len(words):
            j = i
            line_len = 0

            while j < len(words) and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1

            gaps = j - i - 1
            spaces = maxWidth - line_len

            if j == len(words) or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                even = spaces // gaps
                extra = spaces % gaps

                line = ""
                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (even + (1 if k - i < extra else 0))

                line += words[j - 1]

            res.append(line)
            i = j

        return res
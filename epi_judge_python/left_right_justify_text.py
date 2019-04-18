from test_framework import generic_test


def justify_text(words, L):
    cur_line_len, res, cur_line = 0, [], []
    for word in words:
        # We need the len(cur_line), because this tells us the number of spaces
        # so for L = 14 and a set of words "is trickier than", it should
        # be broken down to "is    tricker", "than    "
        if cur_line_len + len(word) + len(cur_line) > L:
            for i in range(L - cur_line_len):
                cur_line[i % max(len(cur_line) - 1, 1)] += " "
            res.append("".join(cur_line))
            cur_line, cur_line_len = [], 0
        cur_line.append(word)
        cur_line_len += len(word)
    return res + [" ".join(cur_line).ljust(L)]


    return []


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("left_right_justify_text.py",
                                       'left_right_justify_text.tsv',
                                       justify_text))

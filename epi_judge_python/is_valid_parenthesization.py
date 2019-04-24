from test_framework import generic_test


def is_well_formed(s):
    stack = []
    LOOKUP = {"(": ")", "{": "}", "[": "]"}
    for char in s:
        if char in LOOKUP:
            stack.append(char)
        elif not stack or LOOKUP[stack.pop()] != char:
            return False
    return not stack


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "is_valid_parenthesization.py",
            "is_valid_parenthesization.tsv",
            is_well_formed,
        )
    )

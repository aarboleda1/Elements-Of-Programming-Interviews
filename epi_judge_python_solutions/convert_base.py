import functools
import string

from test_framework import generic_test

def construct_from_base(num_as_int, base):
    if num_as_int == 0:
        return ''
    else:
        print(num_as_int, "num_as_int plus ", string.hexdigits[num_as_int % base].upper())
        return (
            construct_from_base(num_as_int // base, base) +
            string.hexdigits[num_as_int % base].upper()
        )
def convert_base(num_as_string, b1, b2):
    def construct_from_base(num_as_int, base):
        if num_as_int == 0:
            return ''
        else:

            return (
                construct_from_base(num_as_int // base, base) +
                string.hexdigits[num_as_int % base].upper()
            )

    is_negative = num_as_string[0] == '-'

    def reducer(acc, c):
        return acc * b1 + string.hexdigits.index(c.lower())
    num_as_int = functools.reduce(
        reducer,
        num_as_string[is_negative:],
        0
    )
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))


if __name__ == '__main__':
    # convert_base("314", 2, 93)
    print(construct_from_base(23, 3), "f;aeijf;oiwehj")
    # exit(
        # generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       # convert_base))

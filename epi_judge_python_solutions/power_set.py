import math

from test_framework import generic_test, test_utils

"""
The key to this is understanding the relationship between the time complexity
between and the number of possible subsets.

We can see that there are 2 ^ n possible subsets for a given set. Look at this
example:

For the subset [0,1,2], the possible subsets are

[[], [0], [1], [2], [0,1], [1,2], [0,2], [0,1,2]]

A brute force approach is to compute all subsets that DO NOT contain a
particular element. For example, pick any element to omit, let's 0. First,
pick [1]. Omit 1 and find all subsets of [2], now pick 2 to omit, and see
that there is an empty array, then see that the set ot subsets of [1,2] is [[], [2]]
then to be unioned with the subsets of [[1], [1,2]].

When solving this problem make sure to discuss the time vs space

Complexities

Time: O(n * (2^n))

There are 2^n subsets of any overarching set and we spend O(n) time per call.

Space: O(n * (2^n))

There are 2^n subsets and each subset has an average size of n/2 so O(n/2) =
O(n) times the 2^n subsets yields O(n * (2^n)).

History Log
- 5/7 [HARD]
- 5/12 [SOLVED] make sure to note the time complexity is O(N * 2 ^ N) because
we process O(2 ^ N) for the numbers and at each function call the concatenation
of 2 lists in python is O(N)
"""


def generate_power_set_brute_force(S):
    all_subsets = []

    def helper(subset, idx):
        if idx == len(S):
            all_subsets.append(subset)
            return
        else:
            helper(subset, idx + 1)
            helper(subset + [S[idx]], idx + 1)
    helper([], 0)
    return all_subsets

def generate_power_set(S):
    power_set = []
    for int_for_subset in range(1 << len(S)):
        bit_array = int_for_subset
        subset = []
        while bit_array:
            subset.append(int(math.log2(bit_array & ~(bit_array - 1))))
            bit_array &= bit_array - 1
        power_set.append(subset)
    return power_set
"""
ITERATIVE
"""
def generate_power_set_iterative(nums):
    res = [[]]
    for num in nums:
        res += [
            item + [num] for item in res
        ]
    return res


"""
Solution in PHP with Iterator
/**
 * Recursively returns all (unpermuted) subsets of an input set.
 * Given the set [A, B], returns [[], [A], [B], [A, B]]
 *
 * @param array $set
 * @param array $prefix
 */
function powerset($set, $prefix=array()) {
  if (empty($set)) {
    return array($prefix);
  }
  $without = powerset(array_slice($set, 1), $prefix);
  $with = powerset(array_slice($set, 1), array_merge($prefix, (array)$set[0]));
  return array_merge($without, $with);
}

/**
 * Iteratively returns all (unpermuted) subsets of an input set.
 * Given the set [A, B], returns [[], [A], [B], [A, B]]
 *
 * @param array $set
 */
function powerset_iter($set) {
  $result = array();
  for ($num = 0; $num < pow(2, sizeof($set)); $num++) {
    $partial = array();
    for ($i = $num, $j=0; $i > 0; $i >>= 1, $j++) {
      if ($i & 1) {
        $partial[] = $set[$j];
      }
    }
    $result[] = $partial;
  }
  return $result;
}

/**
 * Iterator over powersets.
 * Uses powerset_num for now, but an even better solution
 * would be to iterate backwards (j--) when current()
 * is called, adding and removing elements from the current
 * set, and break when the condition fails (!$i & 1).
 *
 * @param array $array
 */
class PowerSeterator implements Iterator {
  private $set = array();
  private $num = 0;

  public function __construct($array) {
    if (is_array($array)) {
      $this->set = $array;
      $this->rewind();
    }
  }

  public function rewind() {
    $this->num = 0;
  }

  public function current() {
    // TODO: maintain more state to avoid calling this every time
    $result = powerset_num($this->set, $this->num);
    return $result;
  }

  public function key() {
    return $this->num;
  }

  public function next() {
    if ($this->num >= pow(2, sizeof($this->set))) {
      return null;
    }
    $this->num++;
    return $this->current();
  }

  public function valid() {
    $set = $this->current() !== null;
    echo "valid: {$set}\n";
    return $set;
  }
}
"""
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))

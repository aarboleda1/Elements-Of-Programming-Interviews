

"""
Input: {4,2,3,6,10,1,12}
Output: 5
Explanation: The LBS is {2,3,6,10,1}.

length of Longest Increasing Subseq
max_len =
{4,2,3,6,10,1,12}
"""

"""
{11,2,1,0,12}
{11,2,13, 1,0,11,-1,12}
{11,2,13}
max_len = 1
prev = 11
cur = 2

{
  11: 0,
  2: 1,
}
[
  [],
  [],
]
--
{11,2,13, 1,0,11,-1,12}
 11
 subset = []
--
i = 1
el = 2
subset = [11]
--
i = 2
el = 13
subset = [11, 13]

def longstIncSubsequence(nums):
  max_len = 0
  def backtrack(i, nums, subset):
    if i == len(nums):
      return len(subset)

    if not subset or nums[i] > subset[-1]:
      subset.append(nums[i])
      dp[cur + 1][] = dp[cur][]

    return backtrack(i + 1, nums, subset)
  for i in range(len(nums)):
    max_len = max(backtrack(i, nums, []), max_len)
  return max_len
"""

def longest_increasing_subsequence(nums):
  dp = [[0]*len(nums) for _ in range(0,len(nums)+1)]
  def helper(nums,pre,cur,dp):
      if cur >= len(nums) or pre >= len(nums):
        return 0

      if dp[cur][pre + 1]:
        return dp[cur][pre + 1]
      res1 = 0
      if pre == -1 or nums[pre] < nums[cur]:
        res1 = 1 + helper(nums, cur, cur + 1, dp)
      res2 = helper(nums, pre, cur + 1, dp)

      current_longest_sub = max(res1, res2)
      dp[cur][pre + 1] = current_longest_sub
      return current_longest_sub
  return helper(nums, -1, 0, dp)



"""
  public int findLISLength(int[] nums) {
    int[] dp = new int[nums.length];
    dp[0] = 1;

    int maxLength = 1;
    for (int i=1; i<nums.length; i++) {
      dp[i] = 1;
      for (int j=0; j<i; j++)
        if (nums[i] > nums[j] && dp[i] <= dp[j] ) {
          dp[i] = dp[j]+1;
          maxLength = Math.max(maxLength, dp[i]);
        }
    }
    return maxLength;
  }
  public int findLCSLength(String s1, String s2) {
    Integer[][] dp = new Integer[s1.length()][s2.length()];
    return findLCSLengthRecursive(dp, s1, s2, 0, 0);
  }

  private int findLCSLengthRecursive(Integer[][] dp, String s1, String s2, int i1, int i2) {
    if (i1 == s1.length() || i2 == s2.length())
      return 0;

    if (dp[i1][i2] == null) {
      if (s1.charAt(i1) == s2.charAt(i2))
        dp[i1][i2] = 1 + findLCSLengthRecursive(dp, s1, s2, i1 + 1, i2 + 1);
      else {
        int c1 = findLCSLengthRecursive(dp, s1, s2, i1, i2 + 1);
        int c2 = findLCSLengthRecursive(dp, s1, s2, i1 + 1, i2);
        dp[i1][i2] = Math.max(c1, c2);
      }
    }

    return dp[i1][i2];
  }
"""

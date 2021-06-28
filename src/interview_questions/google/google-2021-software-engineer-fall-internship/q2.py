# You are given a string S consisting of N lowercase English letters. A split of string S is a partition
# into two non-empty strings S1 and S2 such that S1 + S2 = S (where the "+" operator means string, concatenation). 
# You would like to find the number of splits of S into S1 and S2 such that the number of distinct letters in S1 
# equals the number of distinct letters in S2.
#
# For example, given S="abaca" we can split S into S1 = "ab" and $2 = "aca". The number of distinct letters 
# in S1 and S2 is equal to 2, so the split is valid.
#
# On the other hand, splitting S into $1 = "a" and S2 = "baca" is invalid. In this split S1 has one distinct letter
# "baca" is invalid. In this split S1 has one distinct letter and S2 has three distinct letters.
#
# Write a function:
#
# class Solution (public int solution(String S); }
# that, given a non-empty string S consisting of N letters, returns the number of possible splits 
# into two parts such that the number of distinct letters in each part is equal.
#
# Examples:
# 1. Given S="abaca", the function should return 2. S has the following possible splits: ("a", "baca"),
#
# S has the following possible splits: ("a", "baca"), ("ab", "aca"), ("aba", "ca"), ("abac", "a") with the numbers of distinct letters respectively: (1,3), (2, 2), (2, 2), (3, 1), so the only valid splits are ("ab", "aca") and ("aba", "ca"), and therefore the result is 2.
#
# 2. Given S = "aaaa', the function should return 3. The following splits contain equal numbers of distinct letters: ("a", "aaa"), ("aa", "aa"), ("aaa",
#
# 3. Given S = 'ab', the function should return 1. The only valid split is ("a", "b").
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [2..200,000);
#
# N is an integer within the range [2..200,000); • string S consists only of lowercase letters (a-z).
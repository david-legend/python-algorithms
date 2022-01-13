# Words Concatenation (hard) ✩

Given a string and a list of words, find all the starting indices of substrings 
in the given string that are a concatenation of all the given words exactly once 
without any overlapping of words. It is given that all words are of the same length.

#### Example 1
Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

#### Example 2
Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".


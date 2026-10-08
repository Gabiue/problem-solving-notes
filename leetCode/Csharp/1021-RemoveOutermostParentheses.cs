// 1021. Remove Outermost Parentheses (Easy)
// https://leetcode.com/problems/remove-outermost-parentheses/
// Given a valid parentheses string, split it into primitive parts
// and remove the outermost pair of parentheses from each one.

using System.Text;

public class Solution {
    public string RemoveOuterParentheses(string s) {
        var result = new StringBuilder();
        int depth = 0;


        foreach (char ch in s)
        {
            if(ch == '(')
            {
                if(depth > 0)
                {
                    result.Append(ch);
                }
                depth++;
            }
            else
            {
                depth--;
                if (depth > 0)
                {
                    result.Append(ch);
                }
            }
           
        }
         return result.ToString();
    }
}
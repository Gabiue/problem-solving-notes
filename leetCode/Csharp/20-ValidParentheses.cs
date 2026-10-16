// 20. Valid Parentheses (Easy)
// https://leetcode.com/problems/valid-parentheses/
// Given a string of '()[]{}', check that every opening bracket is closed
// by the same type, in the correct order.

public class Solution {
    public bool IsValid(string s) {
        var stack = new Stack<char>();
        var pairs = new Dictionary<char, char> {
            {')', '('}, {']', '['}, {'}', '{'}
        };

        foreach (char c in s) {
            if (c == '(' || c == '[' || c == '{') {
                stack.Push(c);
            } else {
                if (stack.Count == 0 || stack.Peek() != pairs[c]) {
                    return false;
                } else {
                    stack.Pop();
                }
            }
        }

        return stack.Count == 0;
    }
}

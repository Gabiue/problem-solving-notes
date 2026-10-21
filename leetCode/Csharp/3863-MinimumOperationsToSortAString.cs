// 3863. Minimum Operations to Sort a String (Medium)
// https://leetcode.com/problems/minimum-operations-to-sort-a-string/
// In one operation, sort any substring that is not the whole string.
// Return the minimum number of operations to sort s, or -1 if impossible.

public class Solution {
    public int MinOperations(string s) {
        int n = s.Length;

        // Already sorted -> 0
        bool sorted = true;
        for (int i = 1; i < n; i++) {
            if (s[i - 1] > s[i]) {
                sorted = false;
                break;
            }
        }
        if (sorted) return 0;

        // Only allowed substrings have length 1 -> nothing changes
        if (n == 2) return -1;

        char mn = 'z', mx = 'a';
        foreach (char c in s) {
            if (c < mn) mn = c;
            if (c > mx) mx = c;
        }

        // Smallest already at the front or largest already at the end:
        // sort the rest in one move
        if (s[0] == mn || s[n - 1] == mx) return 1;

        // mn somewhere before the last position: sort s[0..n-2] to bring it to the front,
        // then sort s[1..n-1]. Same idea mirrored for mx.
        if (s.IndexOf(mn) < n - 1 || s.LastIndexOf(mx) > 0) return 2;

        // mx only at the start and mn only at the end (e.g. "edc")
        return 3;
    }
}

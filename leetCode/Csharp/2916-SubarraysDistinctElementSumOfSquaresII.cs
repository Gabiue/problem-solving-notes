// 2916. Subarrays Distinct Element Sum of Squares II (Hard)
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/
// Same as 2913: sum the squares of the distinct counts of all subarrays,
// but with n up to 1e5, so the answer must be returned modulo 1e9 + 7.

// Idea: fix the END of the subarray (endIndex). For every start j, keep
// distinctCount[j] = distinct values in nums[j..endIndex].
// When nums[endIndex] arrives, only starts after its previous occurrence gain +1.
// Since (x + 1)^2 - x^2 = 2x + 1, the sum of squares grows by
// 2 * (sum of distinctCount in that range) + (range length).
// A segment tree gives "range sum" and "range +1" in O(log n).

public class Solution {
    private const long Modulo = 1_000_000_007;
    private const int MaxValue = 100_000;

    // Segment tree over the start indices j.
    // distinctCountSum[node]  = sum of distinctCount[j] for every j this node covers.
    // pendingIncrement[node]  = +1s already counted in this node but not yet passed to its children.
    private long[] distinctCountSum;
    private long[] pendingIncrement;

    public int SumCounts(int[] nums) {
        int length = nums.Length;
        distinctCountSum = new long[4 * length];
        pendingIncrement = new long[4 * length];

        int[] lastSeenIndex = new int[MaxValue + 1];
        Array.Fill(lastSeenIndex, -1);

        long sumOfSquaresEndingHere = 0; // sum of distinctCount[j]^2 for subarrays ending at endIndex
        long totalAnswer = 0;

        for (int endIndex = 0; endIndex < length; endIndex++) {
            int currentValue = nums[endIndex];
            int previousIndexOfValue = lastSeenIndex[currentValue];

            // Starts that do NOT contain currentValue yet: they all gain +1.
            int rangeStart = previousIndexOfValue + 1;
            int rangeEnd = endIndex;
            int rangeLength = rangeEnd - rangeStart + 1;

            // Must be read BEFORE the +1, because the formula uses the old values.
            long distinctCountSumInRange = QueryRangeSum(1, 0, length - 1, rangeStart, rangeEnd);

            sumOfSquaresEndingHere = (sumOfSquaresEndingHere + 2 * distinctCountSumInRange + rangeLength) % Modulo;

            IncrementRange(1, 0, length - 1, rangeStart, rangeEnd);

            totalAnswer = (totalAnswer + sumOfSquaresEndingHere) % Modulo;
            lastSeenIndex[currentValue] = endIndex;
        }

        return (int)totalAnswer;
    }

    // Adds +1 to distinctCount[j] for every j in [updateStart, updateEnd].
    private void IncrementRange(int node, int nodeStart, int nodeEnd, int updateStart, int updateEnd) {
        bool noOverlap = updateEnd < nodeStart || nodeEnd < updateStart;
        if (noOverlap) return;

        bool fullyInside = updateStart <= nodeStart && nodeEnd <= updateEnd;
        if (fullyInside) {
            ApplyIncrement(node, nodeStart, nodeEnd, 1);
            return;
        }

        PushPendingToChildren(node, nodeStart, nodeEnd);

        int middle = (nodeStart + nodeEnd) / 2;
        int leftChild = 2 * node;
        int rightChild = 2 * node + 1;

        IncrementRange(leftChild, nodeStart, middle, updateStart, updateEnd);
        IncrementRange(rightChild, middle + 1, nodeEnd, updateStart, updateEnd);

        distinctCountSum[node] = distinctCountSum[leftChild] + distinctCountSum[rightChild];
    }

    // Returns the sum of distinctCount[j] for every j in [queryStart, queryEnd].
    private long QueryRangeSum(int node, int nodeStart, int nodeEnd, int queryStart, int queryEnd) {
        bool noOverlap = queryEnd < nodeStart || nodeEnd < queryStart;
        if (noOverlap) return 0;

        bool fullyInside = queryStart <= nodeStart && nodeEnd <= queryEnd;
        if (fullyInside) return distinctCountSum[node];

        PushPendingToChildren(node, nodeStart, nodeEnd);

        int middle = (nodeStart + nodeEnd) / 2;
        long leftSum = QueryRangeSum(2 * node, nodeStart, middle, queryStart, queryEnd);
        long rightSum = QueryRangeSum(2 * node + 1, middle + 1, nodeEnd, queryStart, queryEnd);

        return leftSum + rightSum;
    }

    // Adds "amount" to every position the node covers, without visiting them one by one.
    private void ApplyIncrement(int node, int nodeStart, int nodeEnd, long amount) {
        int positionsCovered = nodeEnd - nodeStart + 1;
        distinctCountSum[node] += amount * positionsCovered;
        pendingIncrement[node] += amount;
    }

    // Before visiting the children, hand them the increments this node was holding.
    private void PushPendingToChildren(int node, int nodeStart, int nodeEnd) {
        long pending = pendingIncrement[node];
        if (pending == 0) return;

        int middle = (nodeStart + nodeEnd) / 2;
        ApplyIncrement(2 * node, nodeStart, middle, pending);
        ApplyIncrement(2 * node + 1, middle + 1, nodeEnd, pending);

        pendingIncrement[node] = 0;
    }
}

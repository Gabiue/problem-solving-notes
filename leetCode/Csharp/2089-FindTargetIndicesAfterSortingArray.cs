// 2089. Find Target Indices After Sorting Array (Easy)
// https://leetcode.com/problems/find-target-indices-after-sorting-array/
// Sort nums in non-decreasing order and return every index i
// where nums[i] == target, in increasing order.

public class Solution {
    public IList<int> TargetIndices(int[] nums, int target) {
        List<int> resultado = new List<int>();
        Array.Sort(nums);
        for(int i = 0; i < nums.Length ; i ++){
            if(target == nums[i]){
                resultado.Add(i);
            }

        }
        return resultado;
    }
}

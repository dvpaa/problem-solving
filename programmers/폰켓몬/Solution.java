import java.util.HashSet;

class Solution {
    public int solution(int[] nums) {
        HashSet<Integer> hashSet = new HashSet<>();
        for (int num: nums) {
            hashSet.add(num);
        }
        
        int defaultValue = nums.length / 2;
        int contrastValue = hashSet.size();
        return Math.min(defaultValue, contrastValue);
    }
}

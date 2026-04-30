class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] answer = {0, 0};
        for (int i = 0; i < nums.length; i++) {
            int index = target - nums[i];
                for (int j = i; j < nums.length; j++) {
                    if (nums[j] == index && i != j) {
                        answer[0] = i; 
                        answer[1] = j; 
                    }
                }
            }
            return answer;
        }
    }

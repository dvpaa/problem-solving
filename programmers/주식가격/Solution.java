import java.util.Stack;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        Stack<List<Integer>> stack = new Stack<>();
        stack.push(new ArrayList<Integer>(Arrays.asList(0, prices[0])));
        
        for (int i=1; i<prices.length; i++) {
            while (!stack.empty()) {
                if (stack.peek().get(1) > prices[i]) {
                    List<Integer> list = stack.pop();
                    answer[list.get(0)] = i - list.get(0);
                }
                else { break; }
            }
            stack.push(new ArrayList<Integer>(Arrays.asList(i, prices[i])));
        }
        
        int topTime = stack.pop().get(0);
        while (!stack.empty()) {
            int time = stack.pop().get(0);
            answer[time] = topTime - time;
        }
        
        return answer;
    }
}

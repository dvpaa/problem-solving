import java.util.Queue;
import java.util.LinkedList;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {

    public int solution(int[] priorities, int location) {
        Queue<List<Integer>> queue = new LinkedList<>();
        
        for (int i=0; i<priorities.length; i++) {
            queue.add(new ArrayList<Integer>(Arrays.asList(i, priorities[i])));
        }
        
        int cnt = 0;
        while (!queue.isEmpty()) {
            List<Integer> list = queue.poll();
            int idx = list.get(0);
            int priority = list.get(1);
            
            if (isVaild(queue, priority)) {
                cnt++;
                if (idx == location) { break; }
            }
            else { queue.add(list); }
        }
        return cnt;
    }
    
    private boolean isVaild(Queue<List<Integer>> q, int target) {
        for (List<Integer> list: q) {
            if (list.get(1) > target) {
                return false;
            }
        }
        return true;
    }
}

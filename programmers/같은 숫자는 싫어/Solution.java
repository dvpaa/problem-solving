import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        ArrayList<Integer> list = new ArrayList<>();
        int prevNum = 10;
        
        for (int num: arr) {
            if (prevNum != num) {
                list.add(num);
                prevNum = num;
            }
        }
        
        int size = list.size();
        int[] answer = new int[size];
        
        for (int i=0; i<size; i++) {
            answer[i] = list.get(i);
        }
        return answer;
    }
}

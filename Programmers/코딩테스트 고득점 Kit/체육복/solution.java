import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int[] students = new int[n+2];
        students[0] = -2;
        students[n+1] = -2;
        
        for (int lostIdx: lost) {
            students[lostIdx] -= 1;
        }
        for (int reserveIdx: reserve) {
            students[reserveIdx] += 1;
        }
        
        for (int i=1; i<n+1; i++) {
            if (students[i] == -1) {
                int prevIdx = i - 1;
                int nextIdx = i + 1;
                
                if (students[prevIdx] == 1) {
                    students[i] += 1;
                    students[prevIdx] -= 1;
                }
                else if (students[nextIdx] == 1) {
                    students[i] += 1;
                    students[nextIdx] -= 1;
                }
            }
        }
        
        return countAnswer(students);
        
    }
    
    
    private int countAnswer(int[] students) {
        int cnt = 0;
        for (int val: students) {
            if (val >= 0) {cnt+=1;}
        }
        return cnt;
    }
}

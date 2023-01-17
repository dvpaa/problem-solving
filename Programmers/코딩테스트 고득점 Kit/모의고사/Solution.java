import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        int[][] solutions = {
            {1, 2, 3, 4, 5},
            {2, 1, 2, 3, 2, 4, 2, 5},
            {3, 3, 1, 1, 2, 2, 4, 4, 5, 5}
        };
        int size = solutions.length;
        int[] scores = new int[size];
        
        for (int i=0; i<size; i++) {
            scores[i] = getScore(answers, solutions[i]);
        }
        return getMaxIdxArr(scores);
        
        
    }
    
    private int getScore(int[] answers, int[] solution) {
        int idx = 0;
        int score = 0;
        int size = solution.length;
        
        for (int answer: answers) {
            if (answer == solution[idx]) { score++; }
            idx = (idx+1) % size;
        }
        return score;
    }
    
    private int[] getMaxIdxArr(int[] array) {
        int maxVal = getMaxValue(array);
        int size = array.length;
        ArrayList<Integer> list = new ArrayList<>();
        
        for (int i=0; i<size; i++) {
            if (array[i] == maxVal) { list.add(i+1); }
        }
        return list.stream().mapToInt(i->i.intValue()).toArray();
        
    }
    
    private int getMaxValue(int[] array) {
        int maxVal = -1;
        for (int num: array) {
            maxVal = Math.max(maxVal, num);
        }
        return maxVal;
    }
}

import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        for (int i=0; i<commands.length; i++) {
            int start = commands[i][0];
            int end = commands[i][1];
            int k = commands[i][2];

            int[] slicingArray = getSliceOfArray(array, start, end);
            Arrays.sort(slicingArray);

            answer[i] = slicingArray[k-1];
        }
        return answer;


    }

    private int[] getSliceOfArray(int[] array, int start, int end) {
        final int size = end-start+1;
        int[] slicingArray = new int[size];
        for (int i=start-1; i<end; i++) {
            slicingArray[i-(start-1)] = array[i];
        }
        return slicingArray;
    }
}
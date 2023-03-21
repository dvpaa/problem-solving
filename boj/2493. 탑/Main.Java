import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;


public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] datas = br.readLine().split(" ");
        int[] answer = new int[n];
        
        Stack<List<Integer>> leftStack = new Stack<>();
        Stack<List<Integer>> rightStack = new Stack<>();
        
        for (int i=0; i<n; i++) {
            leftStack.push(new ArrayList(Arrays.asList(i, Integer.parseInt(datas[i]))));
        }
        
        
        while (!leftStack.empty()) {
            List<Integer> stand = leftStack.pop();
            
            while (!rightStack.empty()) {
                if (stand.get(1) > rightStack.peek().get(1)) {
                    List<Integer> idx = rightStack.pop();
                    answer[idx.get(0)] = stand.get(0) + 1;
                }
                else {
                    break;
                }
            }
            rightStack.push(stand);
        }
        
        for (int i : answer) {
            System.out.print(i + " ");
        }
        
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Stack;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String initStr = br.readLine();
        int n = Integer.parseInt(br.readLine());
        
        Stack<Character> leftStack = new Stack<>();
        Stack<Character> rightStack = new Stack<>();
        
        for (int i=0; i<initStr.length(); i++) {
            leftStack.push(initStr.charAt(i));
        }
        
        for (int i=0; i<n; i++) {
            String[] oper = br.readLine().split(" ");
            
            if ((oper[0].equals("L")) && !leftStack.empty()) {
                rightStack.push(leftStack.pop());
            }
            else if ((oper[0].equals("D")) && !rightStack.empty()) {
                leftStack.push(rightStack.pop());
            }
            else if ((oper[0].equals("B")) && !leftStack.empty()) {
                leftStack.pop();
            }
            else if (oper[0].equals("P")) {
                leftStack.push(oper[1].charAt(0));
            } 
        }
        
        StringBuilder sb = new StringBuilder();
        while (!leftStack.empty()) {
            rightStack.push(leftStack.pop());
        }
        while (!rightStack.empty()) {
            sb.append(rightStack.pop());
        }
        System.out.println(sb);
    }
}

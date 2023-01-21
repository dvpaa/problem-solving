import java.util.Stack;

class Solution {
    boolean solution(String s) {
        int length = s.length();
        Stack<String> stack = new Stack<>();
        
        for (int i=0; i<length; i++) {
            if (s.charAt(i) == ')') {
                if (stack.empty()) { return false; }
                stack.pop();
            }
            else {
                stack.push("(");
            }
        }
        if (stack.empty()) { return true; }
        else { return false; }
    }
}

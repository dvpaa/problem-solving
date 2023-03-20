import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.LinkedList;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        
        for (int i=0; i<t; i++) {
            String input = br.readLine();
            LinkedList<Character> list = new LinkedList<>();
            int index = 0;
            
            for (int j=0; j<input.length(); j++) {
                char ch = input.charAt(j);
                
                if (ch == '<') {
                    if (index > 0) {index -= 1;}
                }
                else if (ch == '>') {
                    if (index < list.size()) {index += 1;}
                }
                else if (ch == '-') {
                    if (index > 0) {list.remove(--index);}
                }
                else {
                    list.add(index, ch);
                    index += 1;
                }
            }
            
            StringBuilder sb = new StringBuilder();
            for (Character ch : list) {
                sb.append(ch);
            }
            System.out.println(sb);
        }
        
    }
}

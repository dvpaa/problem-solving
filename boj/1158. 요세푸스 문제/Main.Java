import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.ArrayList;
import static java.util.stream.Collectors.joining;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int k = Integer.parseInt(input[1]);
        
        Deque<Integer> q = new ArrayDeque<>();
        
        for (int i=1; i<=n; i++) { q.addLast(i); }
        
        ArrayList<Integer> list = new ArrayList<>();
        int cnt = 1;
        
        while (!q.isEmpty()) {
            if (cnt % k == 0) {
                list.add(q.removeFirst());
            }
            else {
                q.addLast(q.removeFirst());
            }
            cnt += 1;
        }
        
        String result = list.stream()
                            .map(String::valueOf)
                            .collect(joining(", "));
        
        System.out.println("<" + result + ">");
    }
}

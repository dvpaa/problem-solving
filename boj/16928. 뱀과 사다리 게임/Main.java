import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      StringTokenizer st = new StringTokenizer(br.readLine());
      int n = Integer.parseInt(st.nextToken());
      int m = Integer.parseInt(st.nextToken());
      
      int[] ladders = new int[101];
      int[] snakes = new int[101];
      int[] result = new int[101];
      Arrays.fill(result, Integer.MAX_VALUE);
      
      for (int i=0; i<n; i++) {
          st = new StringTokenizer(br.readLine());
          int ladderStart = Integer.parseInt(st.nextToken());
          int ladderEnd = Integer.parseInt(st.nextToken());
          ladders[ladderStart] = ladderEnd;
      }
      for (int i=0; i<m; i++) {
          st = new StringTokenizer(br.readLine());
          int snakeStart = Integer.parseInt(st.nextToken());
          int snakeEnd = Integer.parseInt(st.nextToken());
          snakes[snakeStart] = snakeEnd;
      }
      
      ArrayDeque<ArrayList<Integer>> deque = new ArrayDeque<>();
      deque.add(new ArrayList(Arrays.asList(1, 0)));
      
      while (!deque.isEmpty()) {
          
          ArrayList<Integer> list = deque.removeFirst();
          int node = list.get(0);
          int cost = list.get(1);

          if (cost >= result[node]) {continue;}
          result[node] = cost;
          
          if (snakes[node] != 0) {
              deque.add(new ArrayList(Arrays.asList(snakes[node], result[node])));
              continue;
          }
          
          if (ladders[node] != 0) {
              deque.add(new ArrayList(Arrays.asList(ladders[node], result[node])));
          }
          
          for (int i=1; i<Math.min(100-node, 6)+1; i++) {
              deque.add(new ArrayList(Arrays.asList(node+i, result[node]+1)));
          }
      }
      System.out.println(result[100]);
    }
}
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
      BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
      int n = Integer.parseInt(br.readLine());
      int[] dp = new int[n+1];
      Arrays.fill(dp, 4);
      dp[0] = 0;
      
      for (int i=1; i<n+1; i++) {
          for (int j=(int)Math.sqrt(i); j>0; j--) {
              dp[i] = Math.min(dp[i-(int)Math.pow(j, 2)] + 1, dp[i]);
          }
      }
      System.out.println(dp[n]);
    }
}
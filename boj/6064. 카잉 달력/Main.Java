import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for (int i=0; i<t; i++) {
            String[] input = br.readLine().split(" ");
            int m = Integer.parseInt(input[0]);
            int n = Integer.parseInt(input[1]);
            int x = Integer.parseInt(input[2]);
            int y = Integer.parseInt(input[3]);
            System.out.println(findDate(m, n, x, y));
        }
    }
    
    public static int findGCD(int a, int b) {
        if (b == 0) {
            return a;
        }
        return findGCD(b, a%b);
    }
    
    public static int findDate(int m, int n, int x, int y) {
        int limit = m * (n / findGCD(m, n));
        int i = 0;
        while (true) {
            int result = i * m + x;
            
            if (result > limit) {
                return -1;
            }
            if (((result - y) % n == 0) && (result >= y)) {
                return result;
            }
            i++;
        }
    }
}
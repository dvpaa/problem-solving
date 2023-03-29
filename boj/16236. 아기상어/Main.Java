import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        int sharkSize = 2;
        int time = 0;
        int x = -1;
        int y = -1;
        
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] graph = new int[n][n];
        for (int i=0; i<n; i++) {
            String[] input = br.readLine().split(" ");
            for (int j=0; j<n; j++) {
                graph[i][j] = Integer.parseInt(input[j]);
                if (graph[i][j] == 9) {
                    x = i;
                    y = j;
                }
            }
        }
        graph[x][y] = 0;
        
        int cnt = 0;
        while (true) {
            int[] start = {x, y};
            int[] nextPosAndDist = findNextPosAndDist(start, graph, sharkSize);
            if (nextPosAndDist[0] == -1 && nextPosAndDist[1] == -1) {
                break;
            }
            x = nextPosAndDist[0];
            y = nextPosAndDist[1];
            graph[x][y] = 0;
            time += nextPosAndDist[2];
            cnt++;
            if (cnt == sharkSize) {
                cnt = 0;
                sharkSize++;
            }
        }
        
        System.out.println(time);
    }
    
    public static int[] findNextPosAndDist(int[] start, int[][] graph, int sharkSize) {
        int length = graph.length;
        int[] nextPos = {-1, -1};
        int dist = Integer.MAX_VALUE;
        for (int i=0; i<length; i++) {
            for (int j=0; j<length; j++) {
                if (graph[i][j] > 0 && graph[i][j] < sharkSize) {
                    int[] end = {i, j};
                    int tempDist = findDistance(start, end, graph, sharkSize);
                    if (compare(dist, tempDist, nextPos, end)) {
                        nextPos[0] = i;
                        nextPos[1] = j;
                        dist = tempDist;
                    }
                }
            }
        }
        int[] result = {nextPos[0], nextPos[1], dist};
        return result;
    }
    
    public static int findDistance(int[] start, int[] end, int[][] graph, int sharkSize) {
        int length = graph.length;
        int[] dx = {-1, 1, 0, 0};
        int[] dy = {0, 0, -1, 1};
        
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[length][length];
        queue.add(new int[] {start[0], start[1], 0});
        visited[start[0]][start[1]] = true;
        
        while (!queue.isEmpty()) {
            int[] arr = queue.removeFirst();
            int x = arr[0];
            int y = arr[1];
            int dist = arr[2];
            
            if (x == end[0] && y == end[1]) {
                return dist;
            }
            
            for (int i=0; i<4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx < 0 || nx >= length || ny < 0 || ny >= length) {
                    continue;
                }
                if (!visited[nx][ny] && graph[nx][ny] <= sharkSize) {
                    queue.add(new int[] {nx, ny, dist+1});
                    visited[nx][ny] = true;
                }
            }
        }
        return Integer.MAX_VALUE;
    }
    
    public static boolean compare(int dist, int comparedDist, int[] nextPos, int[] end) {
        if (comparedDist == Integer.MAX_VALUE) {
            return false;
        }
        
        if (comparedDist < dist) {
            return true;
        }
        else if (comparedDist == dist) {
            if (end[0] < nextPos[0]) {
                return true;
            }
            else if (end[0] == nextPos[0]) {
                if (end[1] < nextPos[1]) {
                    return true;
                }
                return false;
            }
            return false;
        }
        return false;
    }
}

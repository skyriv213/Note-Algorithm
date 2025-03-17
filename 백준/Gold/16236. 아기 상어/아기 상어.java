import java.util.*;

public class Main {
    static int n;
    static int[][] acua;
    static int[] dx = {0, 0, 1, -1};
    static int[] dy = {1, -1, 0, 0};
    static int INF = Integer.MAX_VALUE;
    static int size = 2;
    static int x, y;
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        acua = new int[n][n];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                acua[i][j] = sc.nextInt();
                if (acua[i][j] == 9) {
                    x = i;
                    y = j;
                    acua[i][j] = 0; // 아기 상어 위치를 빈칸으로 설정
                }
            }
        }
        
        int answer = 0;
        int foodCount = 0;

        while (true) {
            int[][] visited = bfs(x, y);
            int[] result = solve(visited);
            
            if (result == null) {
                System.out.println(answer);
                break;
            } else {
                x = result[0];
                y = result[1];
                answer += result[2];
                acua[x][y] = 0;
                foodCount++;
                
                if (foodCount >= size) {
                    size++;
                    foodCount = 0;
                }
            }
        }
        
        sc.close();
    }

    static int[][] bfs(int startX, int startY) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{startX, startY});
        
        int[][] visited = new int[n][n];
        for (int[] row : visited) Arrays.fill(row, -1);
        
        visited[startX][startY] = 0;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int cx = current[0];
            int cy = current[1];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                    if (size >= acua[nx][ny] && visited[nx][ny] == -1) {
                        visited[nx][ny] = visited[cx][cy] + 1;
                        queue.add(new int[]{nx, ny});
                    }
                }
            }
        }

        return visited;
    }

    static int[] solve(int[][] visited) {
        int targetX = -1;
        int targetY = -1;
        int minDist = INF;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (visited[i][j] != -1 && acua[i][j] >= 1 && acua[i][j] < size) {
                    if (visited[i][j] < minDist) {
                        minDist = visited[i][j];
                        targetX = i;
                        targetY = j;
                    } else if (visited[i][j] == minDist) { 
                        // 위쪽 -> 왼쪽 우선순위 처리
                        if (i < targetX || (i == targetX && j < targetY)) {
                            targetX = i;
                            targetY = j;
                        }
                    }
                }
            }
        }

        if (minDist == INF) return null;
        
        return new int[]{targetX, targetY, minDist};
    }
}

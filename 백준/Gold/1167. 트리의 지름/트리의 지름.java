import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import java.util.*;


public class Main {

    static class Node {
        int e;
        int cost;

        public Node(int e, int cost) {
            this.e = e;
            this.cost = cost;
        }
    }

    static ArrayList<Node>[] list;
    static boolean[] visited;
    static int max = 0;
    static int node;

    public static void main(String[] args) throws Exception {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Scanner sc = new Scanner(System.in);
        int n = Integer.parseInt(sc.nextLine());

        list = new ArrayList[n + 1];
        visited = new boolean[n + 1];
        for (int i = 1; i < n+1; i++) {
            list[i] = new ArrayList<>();
        }
        for (int i = 0; i < n; i++) {
            int s = sc.nextInt();
            while (true) {
                int e = sc.nextInt();
                if (e == -1) {
                    break;
                }
                int cost = sc.nextInt();
                list[s].add(new Node(e, cost));
            }
        }
        // 트리이므로 모든 노드들은 연결이 되어있음
        dfs(1, 0);
        visited = new boolean[n + 1];
        dfs(node, 0); // node를 기준으로 다시 한 번 dfs 실행하여 최종 길이 탐색
        System.out.println(max);
    }
    public static void dfs(int x, int depth) {
        // 해당 depth가 max 값보다 크다면 max는 depth로 대체, node는 현재 노드로 대체
        if (depth > max) {
            max = depth;
            node = x;
        }
        visited[x] = true;
        for (int i = 0; i < list[x].size(); i++) {
            Node n =   list[x].get(i); // x번째 정점에서 i번째 Node를 get
            if(!visited[n.e]){ // 방문한 적이 없다면
                dfs(n.e, n.cost + depth);
                visited[n.e] = true; // 방문 체크
            }
        }
    }
}
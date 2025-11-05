
import java.io.*;
import java.util.Arrays;
import java.util.*;

/***
 * 3 1
 * 4 4 2
 * N개의 자연수 중에서 M개를 고른 수열
 */
public class Main {
    static int[] arr;
    static int n, m;
    static int[] res;
    static boolean[] used;
    static LinkedHashSet<String> set = new LinkedHashSet();

    private static void dfs(int depth) {
        if (depth == m) {
            StringBuilder sb = new StringBuilder();
            for (int k : res) {
                sb.append(k).append(" ");
            }
            set.add(sb.toString());
            return;
        }
        for (int i = 0; i < n; i++) {
            if(used[i]) {
                continue;}
            res[depth] = arr[i];
            used[i] = true;
            dfs(depth + 1);
            used[i] = false;
        }

    }
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        arr=new int[n];
        res=new int[m];
        used=new boolean[n];
        st = new StringTokenizer(br.readLine());

        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(arr);
        dfs(0);

        StringBuilder sb = new StringBuilder();
        for(String str : set){
            sb.append(str).append("\n");
        }
        System.out.println(sb.toString());

    }
}
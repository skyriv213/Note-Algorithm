import java.util.*;
import java.io.*;
public class Main {


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        int [] arr = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        StringBuilder sb = new StringBuilder();
        Deque<Integer> dq = new ArrayDeque<>();
        for (int i = 0; i < N; i++) {
            while (!dq.isEmpty() && arr[i] <= arr[dq.peekLast()]) {
                dq.removeLast();
            }
            dq.addLast(i);
            if(dq.peekFirst()<=i-L){
                dq.removeFirst();
            }
            sb.append(arr[dq.peekFirst()]).append(" ");
        }
        System.out.println(sb.toString());
    }


}

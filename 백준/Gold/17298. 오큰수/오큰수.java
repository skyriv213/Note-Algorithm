
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import java.util.*;


public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] arr = Arrays.stream(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();
//        for(int i = 0; i < n; i++){
//            arr[i] = Integer.parseInt(br.readLine());
//        }
        StringBuilder sb = new StringBuilder();
        Stack<Integer> s = new Stack<>();
        for(int i = 0; i < n; i++){
            while(!s.isEmpty() && arr[i] > arr[s.peek()]){
                arr[s.pop()] = arr[i];
            }
            s.push(i);
        }
        while(!s.isEmpty()){
            arr[s.pop()] = -1;
        }
        for(int i = 0; i < n; i++){
            sb.append(String.valueOf(arr[i])+" ");
        }
        System.out.println(sb.toString());
    }
}

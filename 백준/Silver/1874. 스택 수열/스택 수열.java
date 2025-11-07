
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import java.util.*;


public class Main {
    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        StringBuilder sb = new StringBuilder();
        Stack<Integer> stack = new Stack<>();
        int lastValue = 1;
        /***
         * 1. 배열 내의 숫자가 스택의 최상단보다 작을때
         *  1.1 스택 안에 숫자를 넣어야함
         * 2. 배열 내의 숫자가 스택의 최상단보다 클때
         *  2.1 스택에서 숫자를 빼야함
         */
        for (int i = 0; i < n; i++) {
            while(stack.isEmpty() || stack.peek() < arr[i]) {
                sb.append("+").append("\n");
                stack.push(lastValue++);
            }
            if(stack.peek() == arr[i]) {
                stack.pop();
                sb.append("-").append("\n");
            }else{
                System.out.println("NO");
                return;
            }
        }
        System.out.println(sb.toString());
    }
}

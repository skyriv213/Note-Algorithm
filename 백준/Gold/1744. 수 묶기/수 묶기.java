
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import java.util.*;




public class Main {
    public static void main(String[] args) throws Exception{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> plus = new PriorityQueue<>((a,b)-> b-a);
        PriorityQueue<Integer> minus = new PriorityQueue<>();
        int one, zero;
        one = 0;
        zero = 0;
        for (int i = 0; i < n; i++) {
            int x = Integer.parseInt(br.readLine());
            if (x == 1) {
                one++;
            } else if (x == 0) {
                zero++;
            } else if (x >1) {
                plus.add(x);
            }else{
                minus.add(x);
            }
        }
        int sum =0;
        while (plus.size()>1){
            sum += plus.poll() * plus.poll();
        }
        if(plus.size()>0){
            sum+= plus.poll();
        }
        while (minus.size()>1){
            sum += minus.poll()*minus.poll();
        }
        if (minus.size() > 0 && zero == 0) {
            sum+= minus.poll();
        }
        System.out.println(sum+one);

    }
}

import java.io.*;
import java.util.*;


public class Main {
    private static class Hands implements Comparable<Hands> {

        int pi;
        int hand;

        public Hands(int p,int i) {
            this.pi = p;
            this.hand = i;
        }

        @Override
        public int compareTo(Hands o) {
            return Integer.compare(this.hand, o.hand);
        }
    }


    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n, m;
        String[] temp = br.readLine().split(" ");
        n = Integer.parseInt(temp[0]);
        m = Integer.parseInt(temp[1]);

        List<Hands> h = new ArrayList<>();
        int max = m*2;
        h.add(new Hands(0,0));
        for (int i = 1; i <= m; i++) {
            temp = br.readLine().split(" ");
            h.add(new Hands(i, Integer.parseInt(temp[0])));
            h.add(new Hands(i, Integer.parseInt(temp[1])));
        }
        Collections.sort(h);
        int floor = n % max == 0 ? max : n % max;
        System.out.println(h.get(floor).pi);
        
        
        }

    }






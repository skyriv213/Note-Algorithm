//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or

import java.io.*;
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();

        String a = "0".repeat(32 - Integer.toBinaryString(Integer.parseInt(s)).length()) + Integer.toBinaryString(Integer.parseInt(s));

        String b = Integer.toBinaryString(~Integer.parseInt(s)+1);
        
        int res = 0;
        for (int i = 0; i < a.length(); i++) {
            if (a.charAt(i) != b.charAt(i)) {
                res++;
            }
        }
        System.out.println(res);

    }
}
import java.util.*;

class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        String [] dart = dartResult.split("");
        StringBuilder sb = new StringBuilder();
        int temp=0;
        int temp2 = 0;
        for(String s : dart){
            if(s.equals("S")){
                temp=Integer.valueOf(sb.toString());
                System.out.println(temp+ " "+answer);
                sb.setLength(0);
            }
            else if(s.equals("D")){
                temp=Integer.valueOf(sb.toString())*Integer.valueOf(sb.toString());
                System.out.println(temp+ " "+answer);
                sb.setLength(0);
            }
            else if(s.equals("T")){
                temp=Integer.valueOf(sb.toString())*Integer.valueOf(sb.toString())*Integer.valueOf(sb.toString());
                System.out.println(temp+ " "+answer);
                sb.setLength(0);
            }else if(s.equals("*")){
                temp*=2;
                answer+=temp2;
                sb.setLength(0);
            }else if(s.equals("#")){
                temp*=-1;
                sb.setLength(0);
            }
            else{
                answer +=temp;
                temp2 = temp;
                temp =0;
                sb.append(s);
            }
        
        }
        answer +=temp;
        System.out.println(temp+ " "+answer);

        // System.out.println(sb.toString());
        return answer;
    }
}
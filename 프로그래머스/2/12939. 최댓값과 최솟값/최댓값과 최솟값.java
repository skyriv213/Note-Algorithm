import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        ArrayList<Integer> list = new ArrayList<>();
        String [] s1 = s.split(" ");
        for(int i = 0 ; i < s1.length ;i++){
            list.add(Integer.valueOf(s1[i]));
        }
        
        answer += String.valueOf(list.stream().min(Integer::compareTo).get());
        answer += " ";
        answer += String.valueOf(list.stream().max(Integer::compareTo).get());

        
        return answer;
    }
}
import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> py = new HashMap<>();
        
        for(String s : participant){
            py.merge(s, 1, Integer::sum);
        }
        for(String s :completion ){
            py.merge(s,-1,Integer::sum);
            if(py.get(s) == 0){
                py.remove(s);
            }
        }
        for(String s: py.keySet()){
            answer =s;
        }
        return answer;
    }
}
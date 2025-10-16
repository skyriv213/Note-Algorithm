import java.util.*;

class Solution {
    public String solution(String[] survey, int[] choices) {
        StringBuilder answer = new StringBuilder();
        int [] arr = new int[4];
        for(int i = 0; i < choices.length;i++){
            String s = survey[i];
            if(s.equals("RT")){
                arr[0]+=(-1*(4-choices[i]));
            }else if(s.equals("TR")){
                arr[0]+=(4-choices[i]);
            }
            else if(s.equals("CF")){
                arr[1]+=(-1*(4-choices[i]));
            }
            else if(s.equals("FC")){
                arr[1]+=(4-choices[i]);
            }
            else if(s.equals("JM")){
                arr[2]+=(-1*(4-choices[i]));
            }
            else if(s.equals("MJ")){
                arr[2]+=(4-choices[i]);
            }
            else if(s.equals("AN")){
                arr[3]+=(-1*(4-choices[i]));
            }
            else if(s.equals("NA")){
                arr[3]+=(4-choices[i]);
            }
                    
        }
        answer.append(arr[0] > 0 ? "T" : "R");
        answer.append(arr[1] > 0 ? "F" : "C");
        answer.append(arr[2] > 0 ? "M" : "J");
        answer.append(arr[3] > 0 ? "N" : "A");

        return answer.toString();
    }
}
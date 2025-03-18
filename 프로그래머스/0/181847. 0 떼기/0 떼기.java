

class Solution {
    public String solution(String n_str) {
        String answer = n_str;
        int check=0;
        for(int i = 0; i<n_str.length();i++){
            if(n_str.charAt(i)=='0'){
                check++;
            }else{
                break;
            }
        }
        
        return answer.substring(check,answer.length());
    }
}
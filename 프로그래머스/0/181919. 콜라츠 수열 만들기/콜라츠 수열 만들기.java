import java.util.*;
class Solution {
    public ArrayList<Integer> solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        answer.add(n);
        while(true){
            if(n==1){
                break;
            }
            if(n%2==0){
                n=n/2;
                answer.add(n);
            }else{
                n=n*3+1;
                answer.add(n);
            }
        }
        return answer;
    }
}
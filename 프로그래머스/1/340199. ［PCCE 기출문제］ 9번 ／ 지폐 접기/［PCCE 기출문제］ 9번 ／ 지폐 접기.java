import java.util.*;

class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        
        int walletMin = Math.min(wallet[0],wallet[1]);
        int walletMax =  Math.max(wallet[0],wallet[1]);
        while(walletMin< Math.min(bill[0],bill[1]) || walletMax < Math.max(bill[0],bill[1])){
            if(bill[0]>bill[1]){
                bill[0] /=2;
            }else{
                bill[1]/=2;
            }
            answer++;
        }
        return answer;
    }
}
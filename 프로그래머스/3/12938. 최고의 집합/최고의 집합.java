/*
각 원소의 합이 s가 되는 수의 집합
각 원소의 곱이 최대가 되는 집합
n은 숫자의 갯수
각 원소의 편차를 최대한 줄이는것
*/

import java.util.*;

class Solution {
    public int[] solution(int n, int s) {
        int[] answer;
        if(n>s){
            return new int[] {-1};
        }else{
            answer = new int[n];
            for(int i = 0;i<n;i++){
                answer[i] = s/n;
            }
            int temp = s%n;
            if(temp!=0){
                for(int i = 0 ; i< answer.length;i++){
                    if(temp == 0 ){
                        break;
                    }
                    answer[i]+=1;
                    temp--;
                };
            }
            Arrays.sort(answer);
        }
        return answer;
    }
}
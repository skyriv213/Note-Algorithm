class Solution {
    public int[] solution(String myString) {
        int[] answer;
      
        String [] sa = myString.split("x",-1);
        
        answer = new int[sa.length];
        for(int i = 0; i<sa.length;i++){
            answer[i]=sa[i].length();
        }
     
        return answer;
    }
}
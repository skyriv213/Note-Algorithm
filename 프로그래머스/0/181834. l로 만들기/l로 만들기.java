class Solution {
    public String solution(String myString) {
         StringBuilder answer = new StringBuilder();
        char target = 'l'; // 비교할 문자
        
        for (int i = 0; i < myString.length(); i++) {
            if ((int) myString.charAt(i) < (int) target) {
                answer.append("l");
            } else {
                answer.append(myString.charAt(i));
            }
        }
        
        return answer.toString();
    
    }
}
import java.util.*;


class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        List<String> s = Arrays.asList(seoul);
        return "김서방은 " + s.indexOf("Kim") + "에 있다";
    }
}
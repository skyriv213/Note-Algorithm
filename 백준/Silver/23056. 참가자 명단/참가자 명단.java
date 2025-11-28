import java.util.*;
import java.io.*;

public class Main {

    static class Student implements Comparable<Student> {
        int room;
        String name;

        @Override
        public int compareTo(Student o) {
            // 1. 학급 번호 오름차순
            if (this.room != o.room) {
                return this.room - o.room;
            }
            // 2. 이름 길이 오름차순
            if (this.name.length() != o.name.length()) {
                return this.name.length() - o.name.length();
            }
            // 3. 이름 사전순 오름차순
            return this.name.compareTo(o.name);
        }

        public Student(int room, String name) {
            this.room = room;
            this.name = name;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        // 홀수반, 짝수반을 나누어 저장할 우선순위 큐
        PriorityQueue<Student> studentsEven = new PriorityQueue<>();
        PriorityQueue<Student> studentsOdd = new PriorityQueue<>();
        
        String[] line = br.readLine().split(" ");
        int n = Integer.parseInt(line[0]);
        int m = Integer.parseInt(line[1]);
        
        // 각 반별 현재 인원수를 체크할 배열
        int[] cnt = new int[n + 1];

        while (true) {
            String inputLine = br.readLine();
            if (inputLine == null) break; // EOF 처리

            line = inputLine.split(" ");
            if (line[0].equals("0") && line[1].equals("0")) {
                break;
            }

            int room = Integer.parseInt(line[0]);
            String name = line[1];

            // [핵심 수정] 입력받는 즉시 정원 체크 (선착순)
            if (cnt[room] < m) {
                cnt[room]++; // 인원 증가
                
                if (room % 2 == 0) {
                    studentsEven.add(new Student(room, name));
                } else {
                    studentsOdd.add(new Student(room, name));
                }
            }
            // 정원이 찼으면(else) 큐에 넣지 않고 그냥 무시함
        }

        // 출력: 홀수반 먼저
        while (!studentsOdd.isEmpty()) {
            Student s = studentsOdd.poll();
            System.out.println(s.room + " " + s.name);
        }
        
        // 출력: 짝수반 나중
        while (!studentsEven.isEmpty()) {
            Student s = studentsEven.poll();
            System.out.println(s.room + " " + s.name);
        }
    }
}
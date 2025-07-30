
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashSet;

public class Main{

	public static void main(String[] args) throws NumberFormatException, IOException {
		// TODO Auto-generated method stub
		
		BufferedReader br = new BufferedReader
				(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter
				(new OutputStreamWriter(System.out));
		
		int test =  Integer.parseInt(br.readLine());
		
		HashSet<String> set1 = new HashSet<String>();
		
		for(int i =0 ; i < test; i++) {
			set1.add(br.readLine());
		}
		
		ArrayList <String> arr = new ArrayList<String>(set1);
		
		// 문자형 ArrayList 선언, <데이터의 형식>(값을 받아오는 구간)
		
		Collections.sort(arr, new Comparator<String>() {
				public int compare(String w1, String w2) {
					if(w1.length() > w2.length())
						return 1;
					else if(w1.length() < w2.length())
						return -1;
					else
						return w1.compareTo(w2);
				}
			
		});
		for(String s : arr)
			System.out.println(s);
		
		/*for(int i = 0 ; i < test; i++) {
			sarr.add(br.readLine());
		}
		
		HashSet<String> arr2 = new HashSet<String>(sarr);
		// HashSet에 sarr의 데이터를 삽입
		ArrayList<String> arr3 =  new ArrayList<String>();
		
		String temp = "";
	
		for(int i = 0 ; i < arr3.size(); i++) {
			for(int j = i+1 ; j < arr3.size() ; j++) {
				if(arr3.get(i).length() > arr3.get(j).length()) {
					temp = arr3.get(i);
					arr3.remove(i);
					arr3.add(i, arr3.get(i));
					arr3.remove(j);
					arr3.add(j, temp);
				}
				
				
				}
			}
		for(int i = 0 ; i < arr3.size(); i++) {
			System.out.print(arr3.get(i)+ "\n");
		}*/
		
		
		

	}

}

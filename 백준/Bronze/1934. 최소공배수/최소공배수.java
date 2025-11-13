import java.util.Scanner; 

public class Main {
	static int GCD(int a, int b) {
		int r = a%b;
		if(r==0) {
			return b;
		}
		else {
			return GCD(b,r);
		}
	}
	public static void main(String [] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		for(int i = 0 ; i < n;i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			int x = GCD(a,b);
			
			System.out.println(a*b/x);
			
		}
	}
}


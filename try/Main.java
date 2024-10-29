import java.util.*;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		ArrayList<Integer> l= new ArrayList<>();
		
		Scanner sc = new Scanner(System.in);
		int A = sc.nextInt();
		int B = sc.nextInt();

		int c = 1;
		int num = 1;
		int n = B-A+1;
		while (true) {
			if (l.size() > B)
			break;
			l.add(num);
			
			if (c==num) {
				c = 1;
				num += 1;
			}
			else {
				c += 1;
			}
		}

		int sum = 0;
		for (int i = A ; i<=B ; i++) {
			sum += l.get(i-1);
		}
		System.out.println(sum);
	}
}

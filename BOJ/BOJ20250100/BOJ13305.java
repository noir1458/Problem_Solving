import java.util.*;
import java.io.IOException;

public class BOJ13305 {

	public static void main(String[] args) throws IOException {
		
		Scanner sc = new Scanner(System.in);
		long N = sc.nextInt();
		ArrayList<Long> L1 = new ArrayList<>(); 
		ArrayList<Long> L2 = new ArrayList<>();

		for(int i=0;i<N-1;i++){
			long append = sc.nextInt();
			L1.add(append);
		}
		for(int i=0;i<N;i++){
			long append = sc.nextInt();
			L2.add(append);
		}
		
		long c = 0;
		long price = L2.get(0);

		for(int i=0;i<N-1;i++){
			if (price > L2.get(i)){
				price = L2.get(i);
			}
			c += (price * L1.get(i));
		}
		System.out.println(c);
	}
}

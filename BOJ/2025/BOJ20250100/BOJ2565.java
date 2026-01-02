import java.util.*;
import java.io.IOException;

public class BOJ2565 {
	public static void main(String[] args) throws IOException {
		
		Scanner sc = new Scanner(System.in);
		ArrayList<ArrayList<Integer>> AL = new ArrayList<>();

		int N = sc.nextInt();
		for (int i=0;i<N;i++) {
			int addA = sc.nextInt();
			int addB = sc.nextInt();
			ArrayList<Integer> append = new ArrayList<>();
			append.add(addA);
			append.add(addB);

			AL.add(append);
		}

		// AL기준으로 정렬하고
		AL.sort((a,b) -> Integer.compare(a.get(0), b.get(0)));

		// BL기준으로 증가하는 부분수열을 구한다.
		ArrayList<Integer> BL = new ArrayList();
		for (ArrayList<Integer> tmp : AL) {
			int tmp1 = tmp.get(1);
			BL.add(tmp1);
		}

		// dp배열 1로 초기화
		int[] dp = new int[BL.size()];
		for(int i=0;i<BL.size();i++){
			dp[i] = 1;
		}

		for(int i=0;i<BL.size();i++){
			for(int j=0;j<i;j++){
				if (BL.get(j) <= BL.get(i)){
					dp[i] = (dp[i]>(dp[j]+1)) ? dp[i] : (dp[j]+1);
				}
			}
		}

		// 답은 N - 부분수열 최대길이
		int maxlen = Arrays.stream(dp).max().getAsInt();
		System.out.println(N-maxlen);

	}
}

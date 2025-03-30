import java.util.*;
import java.io.*;
import java.lang.reflect.Array;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

	public static void main(String[] args) throws IOException{
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		String[] tmp = br.readLine().split(" ");

		Integer[] arr = new Integer[N];
		for (int i=0;i<N;i++){
			arr[i] = Integer.parseInt(tmp[i]);
		}

		Arrays.sort(arr,(a,b)-> b-a);

		int res = -1;
		int now = 0;
		for(int i=0;i<N;i++){
			now = arr[i];
			int cnt = 0;
			for(int j=0;j<N;j++){
				if (now == arr[j]){
					cnt += 1;
				}
			}
			if (now == cnt){
				res = now;
				break;
			}
			if ((i==N-1)&&(now!=0)){
				res = 0;
			}
		}
		System.out.println(res);
		return;
	}
}
	

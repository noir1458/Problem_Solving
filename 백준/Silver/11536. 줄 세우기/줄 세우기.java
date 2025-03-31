import java.util.*;
import java.lang.*;
import java.io.*;

public class Main {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	
	public static void main (String[] args) throws IOException {
		StringBuilder sb = new StringBuilder();
		int N = Integer.parseInt(br.readLine());
		
		String[] arr = new String[N];
		for(int i=0;i<N;i++){
			arr[i] = br.readLine();
		}
		
		String[] cmp = arr.clone();
		String[] asc = arr.clone();
		String[] desc = arr.clone();
		Arrays.sort(asc,Comparator.naturalOrder());
		Arrays.sort(desc,Comparator.reverseOrder());
		
		String c = String.join(" ", cmp);
		String a = String.join(" ", asc);
		String d = String.join(" ", desc);
		
		if (c.equals(a)){
			System.out.println("INCREASING");
		} else if (c.equals(d)) {
			System.out.println("DECREASING");
		} else {
			System.out.println("NEITHER");
		}
		
		
	}
}
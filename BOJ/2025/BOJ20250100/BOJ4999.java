import java.util.*;
import java.io.IOException;

public class BOJ4999 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
		String a,need;
		a = sc.nextLine();
		need = sc.nextLine();
		
		String res = "no";
		for(int i=0;i<a.length();i++){
			if (i + need.length() > a.length()) {
				break;
			}

			String suba = a.substring(i, i+need.length());

			if (suba.equals(need)) {
				res = "go";
				break;
			}
		}
		System.out.println(res);
    }
}

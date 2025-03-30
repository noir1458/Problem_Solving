import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class tmp {
    public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    try {
        System.out.print("숫자를 입력하세요: ");
        int n = Integer.parseInt(br.readLine());
        System.out.println("입력받은 숫자: " + n);

        long res = 1;
        for (int i = 2; i <= n; i++) {
            res *= i;
            while (res % 10 == 0) {
                res /= 10;
            }
            res = res % 100000;
        }
        res %= 10;

        bw.write("결과: " + res + "\n");
        bw.flush();
    } catch (Exception e) {
        System.out.println("오류 발생: " + e.getMessage());
        e.printStackTrace();
    } finally {
        br.close();
        bw.close();
    }
}

}
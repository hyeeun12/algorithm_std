import java.io.*;

public class boj1000_1 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader (new InputStreamReader(System.in));
        // br.readLine() : 한 줄을 문자열로 입력받음
        char[] arr = br.readLine().toCharArray();  // 1 2 -> '1', ' ', '2'
        // 자바에서 char은 문자지만 내부적으로는 숫자(아스키코드)
        System.out.println(arr[0] - '0' + arr[2] - '0');
    }
}

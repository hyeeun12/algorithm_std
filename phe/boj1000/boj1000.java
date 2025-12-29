import java.io.*;

public class boj1000 {
    public static void main(String[] args) throws IOException {
        // read는 1바이트 단위씩 읽기를 한다!
        // 0의 아스키코드 값은 48 
        int a = System.in.read() - 48;
        System.in.read();
        int b = System.in.read() - 48;
        System.out.print(a + b);
    }
}
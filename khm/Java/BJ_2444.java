import java.io.*;

public class BJ_2444 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    // 위쪽 삼각형
    for(int i = 1;  i <= N; i++ ) {
      for(int j = N - i; j > 0; j--) {
        System.out.print(" ");
      }
      System.out.println("*".repeat(2 * i - 1));
    }
    // 아래쪽 삼각형
    for(int i = N - 1; i >= 1; i--){
      for(int j = N - i; j > 0; j--) {
        System.out.print(" ");
      }
      System.out.println("*".repeat(2 * i - 1));

    }
  }
}

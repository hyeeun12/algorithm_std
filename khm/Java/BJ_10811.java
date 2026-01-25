import java.io.*;

public class BJ_10811 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] firstLine = br.readLine().split(" ");
    int N = Integer.parseInt(firstLine[0]);
    int M = Integer.parseInt(firstLine[1]);

    // 바구니 초기화
    // index 0 ~ N - 1 까지 바구니 번호 1 ~ N 으로 설정
    int [] baskets = new int[N];
    for (int i = 0; i < N; i++) {
      baskets[i] = i + 1;
    }

    // 역순 작업
    for (int i = 0; i < M; i++) {
      String[] operation = br.readLine().split(" ");
      int a = Integer.parseInt(operation[0]) - 1;
      int b = Integer.parseInt(operation[1]) - 1;

      // a부터 b까지 역순
      // a와 b 교체, a + 1과 b - 1 교체... 반복
      while (a < b) {
        int temp = baskets[a];
        baskets[a] = baskets[b];
        baskets[b] = temp;
        a++;
        b--;
      }
    }
    for (int i = 0; i < N; i++) {
      System.out.print(baskets[i] + " ");
    }
  }   
}

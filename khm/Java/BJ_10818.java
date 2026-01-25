import java.io.*;

public class BJ_10818{
  public static void main(String[] args)throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int N = Integer.parseInt(br.readLine());
    String[] numbers = br.readLine().split(" ");

    int max_number = Integer.MIN_VALUE; // 최대값 설정(가장 작은 정수로)
    int min_number = Integer.MAX_VALUE; // 최소값 설정(가장 큰 정수로)

    for (int i = 0; i < N; i++){
      int num = Integer.parseInt(numbers[i]);
      if (num > max_number){
        max_number = num; // 최대값 갱신
      }
      if (num < min_number){
        min_number = num; // 최소값 갱신
      }
    }
    System.out.println(min_number + " " + max_number);
  }
}
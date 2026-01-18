import java.util.Scanner; // 자바 입력받기용 클래스 호출
import java.math.BigInteger; // 문제 속 입력받는 숫자의 최대가 10의 1000이라 int로는 역부족

public class BJ_1271 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in); // 스캐너 객체 생성
    BigInteger n = sc.nextBigInteger(); // 첫 번째 입력값 n(큰 수)
    BigInteger m = sc.nextBigInteger();

    System.out.println(n.divide(m) + " " + n.remainder(m));

  }
}

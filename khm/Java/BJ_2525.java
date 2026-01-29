import java.io.*;

public class BJ_2525 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String [] time = br.readLine().split(" ");
    
    // 현재 시간
    int hour = Integer.parseInt(time[0]);
    int minute = Integer.parseInt(time[1]);

    // 요리 시간(분)
    int C = Integer.parseInt(br.readLine());

    // 총 시간 계산
    minute = minute + C;
    hour = hour + (minute / 60);
    minute = minute % 60;
    hour = hour % 24;

    System.out.println(hour + " " + minute);
  } 
}

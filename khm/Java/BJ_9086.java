import java.io.*;

public class BJ_9086 {
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(br.readLine());
    for(int i = 0; i < T; i++) {
      String words = br.readLine();
      Character first = words.charAt(0);
      Character last = words.charAt(words.length() - 1);
      System.out.println(first + "" +  last);
    }
  }
}

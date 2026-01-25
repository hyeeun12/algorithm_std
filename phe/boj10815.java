import java.util.*;
import java.io.*;

class Main {
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        Set<String> cards = new HashSet<>();

        while (st.hasMoreTokens()) {
            cards.add(st.nextToken());
        }

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        while (st.hasMoreTokens()) {
           if (cards.contains(st.nextToken())) {
               sb.append("1 ");
           } else {
               sb.append("0 ");
           }
        }
        System.out.println(sb);
    }
}
//회사에 있는 사람
import java.util.*;
import java.io.*;

class boj7785 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        HashSet<String> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            String[] arr = br.readLine().split(" ");
            // 자바에서 ==는 문자열 내용 비교가 아니라참조(주소) 비교이므로 사용XX
            if (arr[1].equals("enter")) {
                set.add(arr[0]);
            } else {
                set.remove(arr[0]);
            }
        }

        List<String> tempSet = new ArrayList<>(set);
        Collections.sort(tempSet, Collections.reverseOrder());

        for (String name : tempSet) {
            System.out.println(name);
        }
    }
}
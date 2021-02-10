
public class MissingInteger {
  public static void main(String[] args) {
    int[] A = { -1, -3 };
    System.out.println(solution(A));
  }

  public static int solution(int[] A) {
    int len = A.length;
    int N = 1000001;
    boolean[] memorize = new boolean[N];
    for (int i = 0; i < len; i++) {
      if (A[i] <= 0) {
        continue;
      }

      int currentVal = A[i];
      if (!memorize[currentVal]) {
        memorize[currentVal] = true;
      }
    }

    for (int i = 1; i < N; i++) {
      if (!memorize[i])
        return i;
    }

    return 1;
  }
}
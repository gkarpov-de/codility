import javax.lang.model.util.ElementScanner6;

public class FrogRiverOne {

  public static void main(String[] args) {
    int[] A = { 1, 3, 1, 3, 2, 1, 3 };

    System.out.println(solution(3, A));
  }

  public static int solution(int X, int[] A) {
    int N = A.length;
    boolean[] memorize = new boolean[X + 1];

    for (int i = 1; i <= X; i++)
      memorize[i] = false;

    for (int i = 0; i < N; i++) {
      if(!memorize[A[i]]) {
        if(--X == 0) return i;
        memorize[A[i]] = true;
      }
    }
      return -1;
  }
}









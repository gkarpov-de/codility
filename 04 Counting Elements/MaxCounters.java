import java.util.Arrays;

public class MaxCounters {
  public static void main(String[] args) {
    int[] A = { 3, 4, 4, 6, 1, 4, 4 };
    int N = 5;
    solution(N, A);
  }

  private static int[] solution(int N, int[] A) {
    int len = A.length;
    int[] counters = new int[N];
    int condition = N + 1;
    int lastUpdate = 0;
    int maxCounter = 0;

    Arrays.fill(counters, 0);

    for (int i = 0; i < len; i++) {
      int X = A[i];
      if (X == condition) {
        lastUpdate = maxCounter;
      } else {
        int position = X - 1;
        if (counters[position] < lastUpdate)
          counters[position] = lastUpdate + 1;
        else
          counters[position]++;

        int cntr = counters[position];
        if (cntr > maxCounter) {
          maxCounter = cntr;
        }
        printCounters(counters, N);
      }
    }

    for (int i = 0; i < N; i++) {
      if (counters[i] < lastUpdate)
        counters[i] = lastUpdate;
    }

    printCounters(counters, N);
    return counters;
  }

  private static void printCounters(int[] counters, int N) {
    System.out.print("(");
    for (int j = 0; j < N; j++) {
      System.out.print(counters[j]);
      if (j < N - 1)
        System.out.print(", ");
    }
    System.out.println(")");
  }
}
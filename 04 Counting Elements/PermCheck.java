public class PermCheck {
    public static void main(String[] args) {
        PermCheck permCheck = new PermCheck();
//        System.out.println(permCheck.solution(new int[]{4, 1, 3, 2}));
//        System.out.println(permCheck.solution(new int[]{4, 1, 3}));
//        System.out.println(permCheck.solution(new int[]{1, 1}));
        System.out.println(permCheck.solution(new int[]{1000000000}));
    }

    public int solution(int[] A) {
        int n = A.length;
        int max = 0;
        for (int i : A) {
            if (max < i) max = i;
        }

        if (n != max) return 0;

        int[] numPresence = new int[max + 1];

        for (int i = 0; i < max + 1; i++) {
            numPresence[i] = i;
        }

        for (int i : A) {
            if (i > max + 1) return 0;
            numPresence[i] = 0;
        }

        for (int i = 0; i < max + 1; i++) {
            if (numPresence[i] != 0) return 0;
        }

        return 1;
    }
}

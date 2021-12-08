import java.util.*;

class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {

        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        int result[] = new int[k];
        int count = 0;

        for (int row = 0; row < mat.length; row++) {
            int one_count = 0;

            // count the num of once
            while (one_count < mat[row].length && mat[row][one_count] == 1) {
                one_count++;
            }

            map.put(row, one_count);

        }

        for (int i = 0; i < k; i++) {

            int smallest_row_value = 100;
            int smallest_row_key = 0;

            for (Map.Entry me : map.entrySet()) {
                int x = (Integer) me.getValue();
                if (x < smallest_row_value) {
                    smallest_row_value = x;
                    smallest_row_key = (Integer) me.getKey();
                }

            }

            result[count] = smallest_row_key;
            count++;
            map.remove(smallest_row_key);
        }

        return result;
    }

}
import java.util.*;
class Solution {
    public int[] solution(int start_num, int end_num) {
        ArrayList<Integer> arr = new ArrayList<>();
        for(int i=start_num;i<=end_num;i++){
            arr.add(i);
        }
        
        int[] res = new int[arr.size()];
        for(int i=0;i<arr.size();i++){
            res[i] = arr.get(i);
        }
        return res;
    }
}
import java.util.*;
class Solution {
    public int[] solution(int l, int r) {
        ArrayList<Integer> arr = new ArrayList();
        for(int i=l;i<=r;i++){
            String tmp = "" + i;
            boolean check = true;
            for(int j=0;j<tmp.length();j++){
                if(tmp.charAt(j) != '0' && tmp.charAt(j) != '5') {
                    check = false;
                    break;
                }
            }
            if (check) {
                arr.add(Integer.parseInt(tmp));
            }
        }
        
        
        if(arr.size()==0){
            int[] tmp = {-1};
            return tmp;
        } else {
            int[] res = new int[arr.size()];
            for(int i=0;i<arr.size();i++){
                res[i] = arr.get(i);
            }
            return res;
        }
    }
}
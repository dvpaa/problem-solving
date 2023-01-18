import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        HashMap<String, Integer> hashMap = new HashMap<String, Integer>();
        String answer = "";
        
        for (String person: participant) {
            int val = hashMap.getOrDefault(person, 0);
            hashMap.put(person, val+1);
        }
        
        for (String person: completion) {
            hashMap.put(person, hashMap.get(person) - 1);
        }
        
        for (Map.Entry<String, Integer> entry: hashMap.entrySet()) {
            if (entry.getValue() != 0) {
                answer = entry.getKey();
                break;
            }
        }
        return answer;
    }
}

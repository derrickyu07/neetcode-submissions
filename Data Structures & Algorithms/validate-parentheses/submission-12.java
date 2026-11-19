class Solution {
    public boolean isValid(String s) {
        Map<Character,Character> sMap = new HashMap<>();
        Stack<Character> stack= new Stack<>();
        sMap.put('}','{');
        sMap.put(')','(');
        sMap.put(']','[');
        for (Character c: s.toCharArray()){
            if (sMap.containsKey(c)){
                if (!stack.isEmpty() && stack.peek()== sMap.get(c)){
                    stack.pop();
                } else{
                    return false;
                } 
            }else{
                    stack.push(c);
                }
        }
        return stack.isEmpty();
        
    }
}

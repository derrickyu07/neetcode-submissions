class TrieNode{
    HashMap<Character,TrieNode> children = new HashMap<>();
    boolean endOfWord = false; 
}

class WordDictionary {
    private TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode cur = root;
        for (char c: word.toCharArray()){
            if (!cur.children.containsKey(c)){
                cur.children.put(c,new TrieNode());
            }
            cur = cur.children.get(c);
        }
        cur.endOfWord = true;
    }

    public boolean search(String word) {

        return dfs(word,0,root);
        
    }

    public boolean dfs(String word, int x, TrieNode node){
        TrieNode cur = node;
        for (int i = x; i < word.length(); i++){
            if (word.charAt(i) == '.'){
                for(TrieNode temp:cur.children.values()){
                    if (dfs(word,i+1,temp)){
                        return true;
                    }
                }
                return false; 
            } else{
                if (!cur.children.containsKey(word.charAt(i))){
                    return false;
                }
                cur = cur.children.get(word.charAt(i));
            }

        }
        return cur.endOfWord;
    }
}

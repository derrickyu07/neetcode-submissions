/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        ListNode[] resLists = lists;

        if (resLists == null || resLists.length == 0) {
            return null;
        }
        while (resLists.length > 1){
            List<ListNode> mergedLists = new ArrayList<>();
            for (int i = 0; i < resLists.length;i+=2){
                ListNode list1 = resLists[i];
                ListNode list2 = (i + 1) < resLists.length? resLists[i+1] :null;
                mergedLists.add(merge(list1,list2));
            } 
            resLists = mergedLists.toArray(new ListNode[0]); 

        }
        return resLists[0];

    }
    
    public ListNode merge(ListNode list1, ListNode list2){
        ListNode cur = new ListNode();
        ListNode dummy = cur;
        while (list1 != null && list2 != null){
            if (list1.val < list2.val){
                cur.next = list1;
                list1 = list1.next;
            }else{
                cur.next = list2;
                list2 = list2.next;
            }
            cur = cur.next;
        }
        cur.next = list1 != null?list1 : list2;
        return dummy.next;
    }
}

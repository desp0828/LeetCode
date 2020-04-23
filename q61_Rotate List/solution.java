class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null){return head;}
        int length = 1;
        ListNode end = head;
        while(end.next != null){
            end = end.next;
            length = length +1;
        }
        k = k%length;
        end.next = head;
        for(int i=0;i<(length-1-k);i++){
            head = head.next;
        }
        ListNode cur = head.next;
        head.next = null;
        return cur;
        
    }
}

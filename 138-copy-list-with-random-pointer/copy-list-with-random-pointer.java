/*
// Definition for a Node.
class Node {
    int val;
    Node next;
    Node random;

    public Node(int val) {
        this.val = val;
        this.next = null;
        this.random = null;
    }
}
*/

class Solution {
    public Node copyRandomList(Node head) {
        if(head == null) return head;
        HashMap<Node, Node> map = new HashMap<>();
        Node tmp = head;
        while(tmp != null){
            map.put(tmp, new Node(tmp.val));
            tmp = tmp.next;
        }
        Node newNode = head;
        while(newNode != null){
            Node copy = map.get(newNode);
            copy.next = map.get(newNode.next);
            copy.random = map.get(newNode.random);
            newNode = newNode.next;
        }
        return map.get(head);
    }
}
class Solution {
    public int[] kWeakestRows(int[][] mat, int k) {

        BinaryTree tree = null;

        for (int row = 0; row < mat.length; row++) {
            int one_count = 0;

            // count the num of once
            while (one_count < mat[row].length && mat[row][one_count] == 1) {
                one_count++;
            }

            if (tree == null) {
                tree = new BinaryTree(one_count, row, k);
            } else {
                tree.addNode(tree.rootNode, one_count, row);
            }

        }

        tree.asendingNumbers(tree.rootNode);

        return tree.asending;
    }

}

class Node {
    int count;
    int index;
    Node left, right;

    public Node(int count, int index) {
        this.count = count;
        this.index = index;
    }
}

class BinaryTree {

    Node rootNode;
    int[] asending;
    int count = 0;
    int k;

    public BinaryTree(int count, int index, int k) {
        this.rootNode = new Node(count, index);
        this.k = k;
        asending = new int[k];
    }

    public void addNode(Node node, int count, int index) {
        if (node == null) {
            return;
        }

        if (node.index == index) {
            return;
        }

        if (node.count > count) {
            if (node.left == null) {
                node.left = new Node(count, index);
            } else {
                addNode(node.left, count, index);
            }
        }

        if (node.count < count) {
            if (node.right == null) {
                node.right = new Node(count, index);
            } else {
                addNode(node.right, count, index);
            }
        }
    }

    public void asendingNumbers(Node node) {

        if (node == null) {
            return;
        }

        asendingNumbers(node.left);

        asending[count] = node.index;
        count++;

        if (count == k) {
            return;
        }

        asendingNumbers(node.right);

    }

}
# recursive - check if each branch has path sum value of sum - root.val

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public boolean hasPathSum(TreeNode root, int sum) {
        if(root == null) return false;
        if(root.left==null && root.right==null && root.val == sum) return true;
        return (hasPathSum(root.left, sum - root.val) || hasPathSum(root.right, sum - root.val));
    }
}
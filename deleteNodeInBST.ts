/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function deleteNode(root: TreeNode | null, key: number): TreeNode | null {
    if(!root) return null;
    if (root.val === key){
        if(!root.left && !root.right)return null;
        if(!root.left && root.right) return root.right;
        if(!root.right && root.left)return root.left
        if(root.right && root.left){
            let pointer = root.right;
            while(pointer.left){
                pointer = pointer.left;
            }
            root.val = pointer.val;
            root.right = deleteNode(root.right, root.val);
        }
    }else if(root.val > key){
        root.left = deleteNode(root.left,key);
    }else{
        root.right = deleteNode(root.right, key)
    }
return root;
}

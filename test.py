class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.data, end=" ")
            self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if root:
            self.postorder_traversal(root.left)
            self.postorder_traversal(root.right)
            print(root.data, end=" ")

    def delete(self, data):
        
        if self is None:
            return self
        if data < self.data:
            if self.left is not None:  # เพิ่มการตรวจสอบก่อนเรียกใช้เมธอด delete
                self.left = self.left.delete(data)
        elif data > self.data:
            if self.right is not None:  # เพิ่มการตรวจสอบก่อนเรียกใช้เมธอด delete
                self.right = self.right.delete(data)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left

            temp_node = self.find_min()
            self.data = temp_node.data
            self.right = self.right.delete(temp_node.data)

        return self            

# Use the insert method to add nodes
root = Node(None)
root.insert(10)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(20)
root.insert(47)
root.insert(5)

print("Inorder traversal result:", end=" ")
root.inorder_traversal(root)
print("\n")
print("Preorder traversal result:", end=" ")
root.preorder_traversal(root)
print("\n")
print("Postorder traversal result:", end=" ")
root.postorder_traversal(root)
print("\n")

select = int(input("What node do u want to delete?\n:"))
root = root.delete(select)

print("After deletion:")
print("Inorder traversal result:", end=" ")
root.inorder_traversal(root)
print("\n")
print("Preorder traversal result:", end=" ")
root.preorder_traversal(root)
print("\n")
print("Postorder traversal result:", end=" ")
root.postorder_traversal(root)
print("\n")
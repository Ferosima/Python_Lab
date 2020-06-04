#17. Дано посилання A1 на одну з вершин дерева зі зворотним зв'язком. Вивести посилання A2 на корінь вихідного дерева.
class TreeNode:
    def __init__(self):
        self.prev=None
        self.data = ""
        self.left = None
        self.right = None

    # ініціалізуються зв’язки вузла,
    # так як дерево бінарне, то
    # можливі тільки 2 дочірні вузла
    def initNode(self, left, right):
        self.left = left
        self.right = right

    # встановлюються деякі дані вузла
    def set_data(self, data):
        self.data = data
    def set_node_right(self,Node):
      self.right=Node
      Node.prev=self

      def set_node_left(self, Node):
          self.left = Node
          Node.prev = self

def root(Node:TreeNode):
    while Node.prev!=None :
        Node=Node.prev
    return Node

a=TreeNode()
b=TreeNode()
c=TreeNode()
a.data="1"
b.data="2"
c.data="3"
a.set_node_right(b)
b.set_node_right(c)
root=root(c)
print(root.data)
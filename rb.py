class Node:
    def __init__(self,data,right=None,left=None,parent=None,color=0):
        self.data = data
        self.right = right
        self.left = left
        self.parent = parent
        self.color = color # 0 is RED 1 is BLACK
    def __repr__(self):
        return "<Node data = {0}, color = {1}>" .format(self.data, self.color)
    def __getitem__(self,key):
        return self.left if key == 0 else self.right
    def __setitem__(self,key,value):
        if key == 0:
            self.left = value
        else:
            self.right = value

class Tree:
    def __init__(self):
        self.sentinel = Node(None)
        self.sentinel.left = self.sentinel.right = self.sentinel
        self.sentinel.color = 1
        self.root = self.sentinel
    def search(self,data):
        return self._search(self.root,[],data)
    def _search(self,node,queue,data):
        queue.append(node)
        if node == self.sentinel:
            return queue
        elif data < node.data:
            return self._search(node.left,queue,data)
        elif data > node.data:
            return self._search(node.right,queue,data)
        else:
            return queue
    def insert(self,data):
            n = Node(data)
            n.left = n.right = self.sentinel
            current = self.root
            if self.root == self.sentinel:
                self.root = n
                n.parent = None
                n.color = 1
            else:
                while current:
                    if data < current.data:
                        if current.left == self.sentinel:
                            current.left = n
                            break
                        else:
                            current = current.left
                    else:
                        if current.right == self.sentinel:
                            current.right = n
                            break
                        else:
                            current = current.right
                n.parent = current
                while n != self.root and n.parent.color == 0:
                    if n.parent == n.parent.parent.left:
                        u = n.parent.parent.right
                        if u.color == 0:
                            n.parent.color = 1
                            u.color = 1
                            n.parent.parent.color = 0
                            n = n.parent.parent
                        else:
                            if n == n.parent.right:
                                n = n.parent
                                self.rotation(1,n)
                            n.parent.color = 1
                            n.parent.parent.color = 0
                            self.rotation(0,n.parent.parent)
                    else:
                        u = n.parent.parent.left
                        if u.color == 0:
                            n.parent.color = 1
                            u.color = 1
                            n.parent.parent.color = 0
                            n = n.parent.parent
                        else:
                            if n == n.parent.left:
                                n = n.parent
                                self.rotation(0,n)
                            n.parent.color = 1
                            n.parent.parent.color = 0
                            n.rotation(1,n.parent.parent)
                self.root.color = 1
    def rotation(self,key,n):
            r = 1 - key
            a = n[key]
            n[key] = a[r]
            if a[r] != self.sentinel: 
                a[r].parent = n
            if a != self.sentinel:
                a.parent = n.parent
            if n.parent:
                if n == n.parent[r]:
                    n.parent[r] = a
                else:
                    n.parent[a] = a
            else:
                self.root = a
            a[r] = n
            if n != self.sentinel:
                n.parent = a

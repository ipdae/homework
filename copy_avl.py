class Node:
    def __init__(self,data,right=None,left=None,parent=None):
        self.data = data
        self.right = right
        self.left = left
        self.height = 0
        self.parent = parent
    def __repr__(self):
        return "<Node data={0}, height={1}>".format(self.data, self.height)
    def __getitem__(self, key):
        return self.left if key == 0 else self.right
    def __setitem__(self, key, value):
        if key == 0:
            self.left = value
        else:
            self.right = value
        
class Tree:
    def __init__(self):
        self.root = None
    def __repr__(self):
        print "select 1. bfs or 2. dfs"
        num = int(raw_input('choose number: '))
        if num == 1:
            n = []
            queue = []
            current = self.root
            n.append(current)
            while len(n) != 0:
                if n[0].left:
                    n.append(n[0].left)
                if n[0].right:
                    n.append(n[0].right)
                queue.append(n[0])
                n.pop(0)
            return str(queue)
        elif num == 2:
            pass
        else:
            pass
    def _search(self,node,queue,data):
        queue.append(node) 
        if node == None:
            return queue
        elif data < node.data:
            return self._search(node.left,queue,data)
        elif data > node.data:
            return self._search(node.right,queue,data)
        else:
            return queue
    def search(self,data):
        return self._search(self.root,[],data)
    def insert(self,data):
        n = Node(data)
        if self.root == None:
            self.root = n
        else:
            s = self.search(data)
            if s[-1] == None:
                if data < s[-2].data:
                    s[-2].left = n
                else:
                    s[-2].right = n
                n.parent = s[-2]
                while len(s) != 1:
                    lh = s[-2].left.height if s[-2].left else -1
                    rh = s[-2].right.height if s[-2].right else -1
                    h = max(lh, rh)
                    s[-2].height = h + 1
                    lh = s[-2].left.height if s[-2].left else -1
                    rh = s[-2].right.height if s[-2].right else - 1
                    if lh - rh == 2 or lh - rh == -2:
                        a = s[-2]
                        if data < a.data:
                            b = a.left
                        else:
                            b = a.right
                        if data < b.data:
                            c = b.left
                        else:
                            c = b.right
                        if b is a.left and c is b.left: # LEft-Left
                            self.rotation(0,a,b)
                        elif b is a.left and c is b.right: # Left-Right
                            self.rotation(1,b,c) 
                            self.rotation(0,a,c) 
                        elif b is a.right and c is b.left: # Right-Left
                            self.rotation(0,b,c)
                            self.rotation(1,a,c)
                        else: # Right-Right
                            self.rotation(1,a,b)                    
                        lh = self.root.left.height if self.root.left else -1
                        rh = self.root.right.height if self.root.right else -1
                        self.root.height = max(lh,rh) + 1  
                    s.pop(-2)
    def delete(self,data):
        s = self.search(data)
        if s[-1] == None:
            pass
        else:
            if s[-1].left == None and s[-1].right == None:
                if s[-2]:
                    if s[-2].left == s[-1]:
                        s[-2].left = None
                    else:
                        s[-2].right = None
            elif s[-1].left == None or s[-1].right == None:
                if s[-1].left:
                    n = s[-1].left
                else:
                    n = s[-1].right
                if s[-2]:
                    if s[-2].left == s[-1]:
                        s[-2].left = n
                    else:
                        s[-2].right = n
            else:
                parent = s[-1]
                successor = s[-1].right
                while successor.left:
                    parent = successor
                    successor = successor.left
                s[-1].data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right
            while len(s) != 0:
                s[-1].height -= 1
                lh = s[-1].left.height if s[-1].left else -1
                rh = s[-1].right.height if s[-1].right else -1
                if lh - rh == 2 or lh - rh == -2:
                    a =  s[-1]
                    if lh > rh:
                        b = a.left
                    else:
                        b = a.right
                    if b is a.left:
                        if b.right:
                            c = b.right
                        else:
                            c = b.left
                    else:
                        if b.left:
                            c = b.left
                        else:
                            c = b.right
                    if b is a.left and c is b.left: # LEft-Left
                        self.rotation(0,a,b)
                    elif b is a.left and c is b.right: # Left-Right
                        self.rotation(1,b,c) 
                        self.rotation(0,a,c) 
                    elif b is a.right and c is b.left: # Right-Left
                        self.rotation(0,b,c)
                        self.rotation(1,a,c)
                    else: # Right-Right
                        self.rotation(1,a,b)                    
                    lh = self.root.left.height if self.root.left else -1
                    rh = self.root.right.height if self.root.right else -1
                    self.root.height = max(lh,rh) + 1
                s.pop(-1)
    def rotation(self,key,a,b):
        a_k = 1 - key
        c = b[key]
        d = a.parent
        a[key] = b[a_k]
        if a[key]:
            a[key].parent = a
        b[a_k] = a
        a.parent = b
        if d is None:
            self.root = b
            self.root.parent = b
        else:
            if d[key] == a:
                d[key] = b
            else:
                d[a_k] = b
            b.parent = d
        t1 = self.height(a[a_k])
        t2 = self.height(b[key])
        t3 = self.height(a[key])
        a.height = max(t1, t3) + 1
        b.height = max(a.height, t2) + 1
    def height(self,node):
        return -1 if node is None else node.height
    def dfs(self):
        queue = []
        current = self.root
        while current.left:
            current = current.left
            parent = current
        queue.append[current]
        queue.append[parent]
        while len(queue) != 0:
            if queue[0].data < self.root.data:
                if queue[1].right:
                    queue.append[queue[1].right]
                if queue[1].parent:
                    queue.append[queue[1].parent]
                print "<Node data={0}, height={1}>".format(queue[0].data, queue[0].height)
                queue.pop(0)
            elif queue[0].data >= self.root.data:
                if queue[0].right:
                    if queue[0].right.left:
                        pass    
    def bfs(self):
        queue = []
        current = self.root
        queue.append(current)
        while len(queue) != 0:
            if queue[0].left:
                queue.append(queue[0].left)
            if queue[0].right:
                queue.append(queue[0].right)
            print "<Node data={0}, height={1}>".format(queue[0].data, queue[0].height)
            queue.pop(0)

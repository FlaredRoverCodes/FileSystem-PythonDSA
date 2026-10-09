from file_system_node  import FileSystemNode

class FileSystemTree:
    def __init__(self):
        self.root = None

    def insert(self, name):
        new_node = FileSystemNode(name)

        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if name < current.name:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            elif name > current.name:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right
            else:
                return

    def search(self, name):
        return self._search(self.root, name)

    def _search(self, node, name):
        if node is None or node.name == name:
            return node
        if name < node.name:
            return self._search(node.left, name)
        return self._search(node.right, name)

    def delete(self, name):
        self.root = self._delete(self.root, name)

    def _delete(self, node, name):
        if node is None:
            return None
        if name < node.name:
            node.left = self._delete(node.left, name)
        elif name > node.name:
            node.right = self._delete(node.right, name)
        else:
            if node.left is None:        # no child / only right child
                return node.right
            if node.right is None:       # only left child
                return node.left
            successor = node.right       # two children
            while successor.left is not None:
                successor = successor.left
            node.name = successor.name
            node.right = self._delete(node.right, successor.name)
        return node

    def list_all(self):
        result = []
        self._in_order(self.root, result)
        return result

    def _in_order(self, node, result):
        if node:
            self._in_order(node.left, result)
            result.append(node.name)
            self._in_order(node.right, result)

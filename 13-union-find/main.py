class UnionFind:
    def __init__(self, size):
        if size <= 0:
            raise ValueError("Size <= 0 is not allowed")

        self.size = size
        self.num_components = size
        self.sz = [1] * size  # Size of each component
        self.id = list(range(size))  # Parent array

    def find(self, p):
        # Find the root of the component/set
        root = p
        while root != self.id[root]:
            root = self.id[root]

        # Path compression
        while p != root:
            next_p = self.id[p]
            self.id[p] = root
            p = next_p

        return root

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def component_size(self, p):
        return self.sz[self.find(p)]

    def size(self):
        return self.size

    def components(self):
        return self.num_components

    def unify(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)

        # Elements are already in the same component
        if root1 == root2:
            return

        # Union by size
        if self.sz[root1] < self.sz[root2]:
            self.sz[root2] += self.sz[root1]
            self.id[root1] = root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = root1

        # Number of components has decreased by one
        self.num_components -= 1


# Example usage
if __name__ == "__main__":
    uf = UnionFind(10)

    uf.unify(1, 2)
    uf.unify(2, 3)
    print(uf.connected(1, 3))  # True
    print(uf.component_size(1))  # 3
    print(uf.components())  # 8 (10 - 2 components merged)

    uf.unify(4, 5)
    print(uf.connected(4, 5))  # True
    print(uf.component_size(4))  # 2

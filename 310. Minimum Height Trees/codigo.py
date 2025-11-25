class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        adj = defaultdict(list)

        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        edgecount = {}
        leaves = deque()
        for s, nei in adj.items():
            if len(nei)==1:
                leaves.append(s)
            edgecount[s]=len(nei)
        while leaves:
            if n<=2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n-=1
                for m in adj[node]:
                    edgecount[m]-=1
                    if edgecount[m]==1:
                        leaves.append(m)
        
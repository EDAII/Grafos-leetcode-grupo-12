from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        start = node
        V_p_N = {}
        stk=[start]
        visitado = set()
        visitado.add(start)

        while stk:
            node = stk.pop()
            V_p_N[node] = Node(val = node.val)

            for nei in node.neighbors:
                if nei not in visitado:
                    visitado.add(nei)
                    stk.append(nei)

        for old_node, new_node in V_p_N.items():
            for nei in old_node.neighbors:
                new_nei = V_p_N[nei]
                new_node.neighbors.append(new_nei)
        
        return V_p_N[start]
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        last_node = []
        for node in edges:
            if node[0] in last_node:
                return node[0]
            else:
                last_node.append(node[0])
            if node[1] in last_node:
                return node[1]
            else:
                last_node.append(node[1])
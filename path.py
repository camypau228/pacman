class Path():
    
    def __init__(self, map):
        inf = 1e9
        self.dist = []
        self.next = []
        for i in range(len(map)):
            self.dist.append([])
            self.next.append([])
            for j in range(len(map)):
                if i != j:
                    self.dist[i].append(inf)
                else:
                    self.dist[i].append(0)
                self.next[i].append((i, 0))
        for i in range(1, len(map)):
            for where in map[i].neighbor:
                if not (where in (-1, 1, -2, 2)):
                    continue
                if map[i].neighbor[where] != -1:
                    self.dist[i][map[i].neighbor[where].num] = 1
                    self.next[i][map[i].neighbor[where].num] = (map[i].neighbor[where].num, where)
        for u in range(1, len(map)):
            for i in range(1, len(map)):
                for j in range(1, len(map)):
                    if self.dist[i][j] > self.dist[i][u] + self.dist[u][j]:
                        self.dist[i][j] = self.dist[i][u] + self.dist[u][j]
                        self.next[i][j] = self.next[i][u]
        
    def get_path(self, v_from, v_to):
        ans = []
        cur_v, where = self.next[v_from][v_to]
        while where != 0:
            ans.append(where)
            cur_v, where = self.next[cur_v][v_to]
        return ans
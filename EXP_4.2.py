class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1

    # Greedy coloring algorithm
    def greedy_coloring(self):
        result = [-1] * self.vertices
        result[0] = 0  # Assign the first color to the first vertex

        # A function to check if a given color can be assigned to the vertex
        def is_safe(v, c):
            for i in range(self.vertices):
                if self.graph[v][i] == 1 and result[i] == c:
                    return False
            return True

        # Assign colors to remaining vertices
        for v in range(1, self.vertices):
            for c in range(self.vertices):
                if is_safe(v, c):
                    result[v] = c
                    break

        return result

# Example usage:
if __name__ == "__main__":
    # Create a graph with 5 vertices
    g = Graph(5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)

    colors = g.greedy_coloring()
    print("Vertex \t Color")
    for i in range(len(colors)):
        print(f"{i} \t {colors[i]}")

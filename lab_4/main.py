class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node in self.graph:
            self.graph[node].append(neighbor)
        else:
            self.graph[node] = [neighbor]


def blow_up(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):

            if matrix[y][x] == 0:
                if x != 0:

                    if matrix[y][x - 1] != 0:
                        matrix[y][x - 1] = -1

                    if y != 0:
                        if matrix[y - 1][x - 1] != 0:
                            matrix[y - 1][x - 1] = -1

                    if y != len(matrix) - 1:
                        if matrix[y + 1][x - 1] != 0:
                            matrix[y + 1][x - 1] = -1

                if x != len(matrix[y]) - 1:
                    if matrix[y][x + 1] != 0:
                        matrix[y][x + 1] = -1

                    if y != 0:
                        if matrix[y - 1][x + 1] != 0:
                            matrix[y - 1][x + 1] = -1

                    if y != len(matrix) - 1:
                        if matrix[y + 1][x + 1] != 0:
                            matrix[y + 1][x + 1] = -1

                if y != 0:
                    if matrix[y - 1][x] != 0:
                        matrix[y - 1][x] = -1

                if y != len(matrix) - 1:
                    if matrix[y + 1][x] != 0:
                        matrix[y + 1][x] = -1

    return matrix


def bfs(graph, start, all_goals):
    visited = set()
    queue = [start]
    result = []
    while queue:
        node = queue.pop()

        if all_goals.__contains__(node):
            return result

        if node not in visited:
            result.append(node)
            visited.add(node)

            if node in graph.graph:
                queue.extend(neighbor for neighbor in graph.graph[node] if neighbor not in visited)

    return -1


# Create a graph from the matrix
def create_graph_from_matrix(matrix):
    graph = Graph()

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if matrix[i][j] == 1:
                node = (i, j)

                if i + 1 < len(matrix):
                    if matrix[i + 1][j] == 1:
                        graph.add_edge(node, (i + 1, j))

                if i - 1 >= 0:
                    if matrix[i - 1][j] == 1:
                        graph.add_edge(node, (i - 1, j))

                if j + 1 < len(matrix[0]):
                    if matrix[i][j + 1] == 1:
                        graph.add_edge(node, (i, j + 1))

                if j - 1 >= 0:
                    if matrix[i][j - 1] == 1:
                        graph.add_edge(node, (i, j - 1))

    return graph


def find_all_start_and_all_goals(matrix):
    all_starts = []
    all_goals = []

    for x in range(len(matrix)):

        if (matrix[x][0] == 1):
            all_starts.append((x, 0))

    for x in range(len(matrix[0])):

        if (matrix[x][len(matrix[0]) - 1] == 1):
            all_goals.append((x, len(matrix[0]) - 1))

    return all_starts, all_goals


def find_shortest_way(all_starts, all_goals, graph,matrix_length):
    shortest_way = float("inf")
    iteration = 0
    for start in all_starts:
        iteration+=1
        dfs_result = bfs(graph, start, all_goals)
        if (
                shortest_way != float("inf") and dfs_result == -1
                or shortest_way != float(-1) and dfs_result == -1
        ):
            shortest_way = -1

        elif len(dfs_result) < shortest_way:
            shortest_way = len(dfs_result)

        if shortest_way==matrix_length:
            return shortest_way

    return shortest_way


if __name__ == '__main__':
    with open("input.txt", "r") as file:
        lines = file.readlines()
        matrix = blow_up([list(map(int, line.strip().split())) for line in lines])

    graph = create_graph_from_matrix(matrix)
    all_starts, all_goals = find_all_start_and_all_goals(matrix)
    shortest_way = find_shortest_way(all_starts, all_goals, graph,len(matrix))

    with open("output.txt", "w") as file:
        file.write(str(shortest_way))

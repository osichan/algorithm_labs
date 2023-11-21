import heapq

class Node:
    def __init__(self, node_id):
        self.node_id = node_id
        self.neighbors = {}

    def add_neighbor(self, neighbor, latency):
        self.neighbors[neighbor] = latency


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_id):
        self.nodes[node_id] = Node(node_id)

    def add_edge(self, start_node, end_node, latency):
        self.nodes[start_node].add_neighbor(end_node, latency)
        self.nodes[end_node].add_neighbor(start_node, latency)


def dijkstra(graph, start_node):
    min_delay = {node: float('inf') for node in graph.nodes}
    min_delay[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_delay, current_node = heapq.heappop(priority_queue)

        for neighbor, latency in graph.nodes[current_node].neighbors.items():
            delay = current_delay + latency
            if delay < min_delay[neighbor]:
                min_delay[neighbor] = delay
                heapq.heappush(priority_queue, (delay, neighbor))

    return min_delay


def find_optimal_server_location(graph,clients):
    min_max_delay = float('inf')
    keys = []

    for key in graph.nodes.keys():
        if not clients.__contains__(key):
            keys.append(key)

    for potential_server in keys:
        delays = dijkstra(graph, potential_server)
        max_delay = max(delays[client] for client in clients)
        min_max_delay = min(min_max_delay, max_delay)

    return min_max_delay


def write_output(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))


def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        N, M = map(int, lines[0].split())
        clients = list(map(int, lines[1].split()))
        graph = Graph()

        for i in range(2, M + 2):
            start, end, latency = map(int, lines[i].split())
            if start not in graph.nodes:
                graph.add_node(start)
            if end not in graph.nodes:
                graph.add_node(end)
            graph.add_edge(start, end, latency)

        return graph, clients

def main(read_input_file,write_output_file):
    graph, clients = read_input(read_input_file)
    result = find_optimal_server_location(graph, clients)
    write_output(write_output_file, result)


if __name__ == "__main__":
    main("./gamsrv.in","./gamsrv.out")

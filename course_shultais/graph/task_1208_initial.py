class Graph:

    def __init__(self, nodes):
        # Создаем матрицу смежности.
        self.matrix = []

        # Заполняем матрицу нулями.
        for n in range(nodes):
            self.matrix.append([0] * nodes)

        # Список для хранения узлов.
        self.nodes = []
        self.visited = []

    def get_node_index_by_name(self, name):
        return self.nodes.index(name)

    def add_node(self, name):
        # Добавляем новый узел.
        self.nodes.append(name)

        # Возвращаем индекс нового узла в массиве self.nodes.
        return len(self.nodes) - 1

    def add_edge(self, node_from, node_to, weight=1, directed=True):
        self.matrix[node_from][node_to] = weight
        if not directed:
            self.matrix[node_to][node_from] = weight

    def dfs(self, node_name):
        node_index = self.get_node_index_by_name(node_name)
        idx=0
        self.visited[node_index] = True
        for weightt in self.matrix[node_index]:
            if weightt>0 and not self.visited[idx]:
                self.dfs(self.nodes[idx])
            idx+=1

        return []

    def __str__(self):
        text = ""
        # Вычисляем максимальную длину имени.
        max_len_name = max([len(name) for name in self.nodes])
        max_len_name = 2 if max_len_name <= 2 else max_len_name + 1

        header = ["" * max_len_name] + self.nodes
        header = " ".join([f"{name:>{max_len_name}}" for name in header])
        text += f"{header}\n"

        for i, edges in enumerate(self.matrix):
            text += f"{self.nodes[i]:>{max_len_name}} " + " ".join([f"{edge:>{max_len_name}}" for edge in edges]) + "\n"

        return text


with open("matrix.txt") as matrix_file:
    data = matrix_file.read().split("\n")

    # Создаем граф
    nodes_count, start_node = data[0].split()
    nodes_count = int(nodes_count)
    graph = Graph(nodes_count)

    # Добавляем ноды
    nodes = data[1].split(" ")
    for node in nodes:
        graph.add_node(node)

    # Добавляем связи
    for edge in data[2:]:
        node1, node2 = edge.split(" ")
        node1 = graph.get_node_index_by_name(node1)
        node2 = graph.get_node_index_by_name(node2)

        graph.add_edge(node1, node2)

    # Получаем путь обхода
    path = graph.dfs(start_node)
    print(" -> ".join(path))




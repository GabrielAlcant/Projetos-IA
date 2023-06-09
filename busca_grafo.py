from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, heuristic_value):
        self.vertices[name] = heuristic_value

    def add_edge(self, start_vertex, end_vertex, weight):
        if start_vertex not in self.vertices:
            raise ValueError("O vértice inicial não existe no grafo.")
        if end_vertex not in self.vertices:
            raise ValueError("O vértice final não existe no grafo.")
        if not isinstance(weight, (int, float)):
            raise ValueError("O peso da aresta deve ser um número.")

        if start_vertex not in self.vertices:
            self.vertices[start_vertex] = float('inf')
        if end_vertex not in self.vertices:
            self.vertices[end_vertex] = float('inf')

        self.vertices[start_vertex] = min(self.vertices[start_vertex], weight)

    def greedy_best_first_search(self, start_vertex, end_vertex):
        if start_vertex not in self.vertices:
            raise ValueError("O vértice inicial não existe no grafo.")
        if end_vertex not in self.vertices:
            raise ValueError("O vértice final não existe no grafo.")

        visited = set()
        queue = PriorityQueue()
        queue.put((self.vertices[start_vertex], [start_vertex]))

        while not queue.empty():
            _, path = queue.get()
            current_vertex = path[-1]

            if current_vertex == end_vertex:
                return path

            visited.add(current_vertex)

            for neighbor, _ in self.get_neighbors(current_vertex):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    queue.put((self.vertices[neighbor], new_path))
                    visited.add(neighbor)

    def a_star_search(self, start_vertex, end_vertex):
        if start_vertex not in self.vertices:
            raise ValueError("O vértice inicial não existe no grafo.")
        if end_vertex not in self.vertices:
            raise ValueError("O vértice final não existe no grafo.")

        visited = set()
        queue = PriorityQueue()
        queue.put((self.vertices[start_vertex], [start_vertex], 0))

        while not queue.empty():
            _, path, cost = queue.get()
            current_vertex = path[-1]

            if current_vertex == end_vertex:
                return path

            visited.add(current_vertex)

            for neighbor, weight in self.get_neighbors(current_vertex):
                if neighbor not in visited:
                    new_path = list(path)
                    new_path.append(neighbor)
                    new_cost = cost + weight
                    queue.put((self.vertices[neighbor] + new_cost, new_path, new_cost))
                    visited.add(neighbor)

    def get_neighbors(self, vertex):
        neighbors = []
        for v, weight in self.vertices.items():
            if weight != float('inf'):
                neighbors.append((v, weight))
        return neighbors

def create_graph():
    graph = Graph()

    while True:
        print("\n1 - Adicionar vértice")
        print("2 - Adicionar aresta")
        print("3 - Realizar busca gulosa pela melhor escolha")
        print("4 - Realizar busca A*")
        print("0 - Sair")

        choice = input("\nEscolha uma opção: ")

        if choice == "1":
            name = input("Nome do vértice: ")
            heuristic = float(input("Valor heurístico: "))
            graph.add_vertex(name, heuristic)
            print("Vértice adicionado.")

        elif choice == "2":
            start = input("Vértice de origem: ")
            end = input("Vértice de destino: ")
            weight = float(input("Peso da aresta: "))
            graph.add_edge(start, end, weight)
            print("Aresta adicionada.")

        elif choice == "3":
            start = input("Vértice de origem: ")
            end = input("Vértice de destino: ")
            try:
                path = graph.greedy_best_first_search(start, end)
                if path:
                    print("Caminho encontrado:", " -> ".join(path))
                else:
                    print("Caminho não encontrado.")
            except ValueError as e:
                print(e)

        elif choice == "4":
            start = input("Vértice de origem: ")
            end = input("Vértice de destino: ")
            try:
                path = graph.a_star_search(start, end)
                if path:
                    print("Caminho encontrado:", " -> ".join(path))
                else:
                    print("Caminho não encontrado.")
            except ValueError as e:
                print(e)

        elif choice == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    create_graph()
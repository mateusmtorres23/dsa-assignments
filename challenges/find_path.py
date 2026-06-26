from data_structures.city_map import CityMap
import heapq
import math


def find_path(city_map: CityMap, start: int, goal: int) -> list[int]:
    if start == goal:
        return [start]

    intersections = city_map.intersections
    roads = city_map.roads

    # Função para calcular a distância euclidiana (linha reta)
    def calculate_distance(node1: int, node2: int) -> float:
        x1, y1 = intersections[node1]
        x2, y2 = intersections[node2]
        return math.hypot(x1 - x2, y1 - y2)

    # Estruturas de dados auxiliares
    # O heap armazenará tuplas no formato: (f_score, g_score, node_id)
    open_set = []

    # O custo g do start é 0.
    # O f_score inicial é apenas a heurística do start até o goal.
    heapq.heappush(open_set, (calculate_distance(start, goal), 0, start))

    # Dicionário de "pais" para reconstruir o caminho no final
    came_from = {}

    # Dicionário do custo real acumulado (g_score) para chegar em cada nó.
    # Nós não descobertos têm custo implicito de infinito.
    g_score = {start: 0}

    # Conjunto de nós já totalmente processados
    visited = set()

    # 4. Loop Principal do A*
    while open_set:
        # Pega o nó com o menor f_score da fila (graças ao heapq)
        current_f, current_g, current = heapq.heappop(open_set)

        # Ignora nós obsoletos que podem ter sobrado na fila de prioridade
        if current in visited:
            continue

        visited.add(current)

        # 5. Condição de Parada e Reconstrução do Caminho
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            # Inverte a lista para ficar na ordem correta: start -> ... -> goal
            path.reverse()
            return path

        # 6. Avaliação dos Vizinhos
        for neighbor in roads.get(current, []):
            if neighbor in visited:
                continue

            # Custo do caminho desde o 'start'
            # passando pelo nó 'current' até o 'neighbor'
            dist_to_neighbor = calculate_distance(current, neighbor)
            tentative_g_score = current_g + dist_to_neighbor

            # Se encontramos um caminho mais curto para o vizinho
            if tentative_g_score < g_score.get(neighbor, float('inf')):
                # Registramos de onde viemos
                came_from[neighbor] = current
                # Atualizamos o melhor custo real
                g_score[neighbor] = tentative_g_score

                # A "mágica" do A*: calculamos o f_score somando o custo real
                # com a estimativa até o destino
                f_score = tentative_g_score + calculate_distance(
                                                        neighbor, goal
                                                        )

                # Inserimos no heap
                heapq.heappush(
                    open_set, (f_score, tentative_g_score, neighbor)
                    )

    # Se a fila esvaziar e não acharmos o goal, é porque o grafo é desconexo
    return []

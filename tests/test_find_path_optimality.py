import math
import heapq

from challenges.find_path import (
    find_path,
)

from tests.generators import (
    generate_small_map,
    generate_reference_map,
    generate_city_map,
    generate_single_node_map,
)


def calculate_distance(city_map, node1, node2):
    x1, y1 = city_map.intersections[node1]
    x2, y2 = city_map.intersections[node2]
    return math.hypot(x1 - x2, y1 - y2)


def shortest_distance(
    city_map,
    start,
    goal,
):

    # Novo gabarito com Dijkstra
    # Calcula a menor distância geométrica real possível.

    queue = [(0.0, start)]
    distances = {start: 0.0}

    while queue:
        current_dist, current = heapq.heappop(queue)

        if current == goal:
            return current_dist

        if current_dist > distances.get(current, float('inf')):
            continue

        for neighbor in city_map.roads[current]:
            weight = calculate_distance(city_map, current, neighbor)
            distance = current_dist + weight

            if distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return None


def path_cost(city_map, path):
    if not path:
        return None

    cost = 0.0
    for current, next in zip(path, path[1:]):
        cost += calculate_distance(city_map, current, next)

    return cost


def test_single_node_map():

    (
        city_map,
        start,
        goal,
    ) = generate_single_node_map()

    path = find_path(
        city_map,
        start,
        goal,
    )

    cost = path_cost(city_map, path)
    assert cost == 0.0


def test_optimal_path_small_map():

    (
        city_map,
        start,
        goal,
    ) = generate_small_map()

    path = find_path(
        city_map,
        start,
        goal,
    )

    expected = shortest_distance(
        city_map,
        start,
        goal,
    )
    cost = path_cost(city_map, path)

    assert expected is not None
    assert cost is not None
    assert math.isclose(cost, expected, rel_tol=1e-9)


def test_optimal_path_reference_map():

    (
        city_map,
        start,
        goal,
    ) = generate_reference_map()

    path = find_path(
        city_map,
        start,
        goal,
    )

    expected = shortest_distance(
        city_map,
        start,
        goal,
    )
    cost = path_cost(city_map, path)

    assert expected is not None
    assert cost is not None
    assert math.isclose(cost, expected, rel_tol=1e-9)


def test_optimal_path_medium_map():

    (
        city_map,
        start,
        goal,
    ) = generate_city_map(
        250
    )

    path = find_path(
        city_map,
        start,
        goal,
    )

    expected = shortest_distance(
        city_map,
        start,
        goal,
    )
    cost = path_cost(city_map, path)

    assert expected is not None
    assert cost is not None
    assert math.isclose(cost, expected, rel_tol=1e-9)


def test_optimal_path_large_map():

    (
        city_map,
        start,
        goal,
    ) = generate_city_map(
        1000
    )

    path = find_path(
        city_map,
        start,
        goal,
    )

    expected = shortest_distance(
        city_map,
        start,
        goal,
    )
    cost = path_cost(city_map, path)

    assert expected is not None
    assert cost is not None
    assert math.isclose(cost, expected, rel_tol=1e-9)

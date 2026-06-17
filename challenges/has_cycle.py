def has_cycle(graph: dict[str, list[str]]) -> bool:
    not_visited = set(graph.keys())

    while not_visited:
        current_trail = set()
        node = not_visited.pop()

        while node:
            if node in current_trail:
                return True

            current_trail.add(node)
            not_visited.discard(node)
            
            neighbor = graph.get(node, [])

            if neighbor:
                node = neighbor[0]
            else:
                node = None
                
    return False
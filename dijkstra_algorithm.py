def find_lowes_cost_node(costs: dict[str:int|float], processed:list[str]) -> str:
    lowes_cost = float('inf')
    lowes_cost_node = None

    for node, cost in costs.items():
        if cost < lowes_cost and node not in processed:
            lowes_cost = cost
            lowes_cost_node = node

    return lowes_cost_node


if __name__ == '__main__':
    r"""
    Graph
            A-- 1 --C-- 1 --E
           /|      / \       \   
          6 |     /   1       3
         /  |    /     \       \
    Start   3   1       F-- 4 --Finish
         \  |  /       /       /
          2 | /       5       2
           \|/       /       /  
            B-- 2 --D-- 2 --G            
    """




    graph = {
        'start': {'a': 6, 'b': 2},
        'a': {'c': 1,},
        'b': {'a': 3, 'c': 1, 'd': 2},
        'c': {'e': 1, 'f': 1},
        'd': {'f': 5, 'g': 2},
        'e': {'finish': 3},
        'f': {'g': 1, 'finish': 4},
        'g': {'finish': 1},
        'finish': {},
    }

    costs = {
        'a': 6,
        'b': 2,
        'c': float('inf'),
        'd': float('inf'),
        'e': float('inf'),
        'f': float('inf'),
        'g': float('inf'),
        'finish': float('inf'),
    }

    parents = {
        'a': 'start',
        'b': 'start',
        'finish': None,
    }

    processed = []

    node = find_lowes_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for neighbor in neighbors.keys():
            new_cost = cost + neighbors[neighbor]

            if costs[neighbor] > new_cost:
                costs[neighbor] = new_cost
                parents[neighbor] = node

        processed.append(node)
        node = find_lowes_cost_node(costs, processed)



    child_node = 'finish'
    result_nodes = [child_node]
    for i in range(len(parents)):
        parent_node = parents.get(child_node)

        if parent_node:
            result_nodes.append(parent_node)
            child_node = parent_node

    result_nodes.reverse()

    print(' -> '.join(result_nodes))

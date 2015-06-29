graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 4],
    3: [0],
    4: [2, 5],
    5: [4]
}

coffee_store = [0, 0, 1, 0, 0, 1]
store_list = {x: coffee_store[x] for x in list(graph.keys())}


def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in graph:
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest


def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


def closest_coffee_store(graph, starting_point):
    if starting_point not in graph:
        print("No such point.")
    temp = []
    for element in store_list:
        if store_list[element] == 1:
            # temp.append(find_shortest_path(graph, starting_point, element))
            temp.append(bfs(graph, starting_point, element))
    return min(temp, key=len)


for number in range(0, 6):
    print(closest_coffee_store(graph, number))

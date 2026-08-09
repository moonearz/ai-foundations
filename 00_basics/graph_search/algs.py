import networkx as nx
from collections import deque

def depth_first_search(graph: nx.Graph, start: str, goal: str) -> list[str] | None:
    if start not in graph or goal not in graph:
        return None
    stack = []
    visited_set = set()

    stack.append([start])
    visited_set.add(start)
    while stack:
        current_path = stack.pop()
        current_node = current_path[-1]
        if current_node == goal:
            return current_path
            
        for node in graph.neighbors(current_node):
            if node not in visited_set:
                visited_set.add(node)
                new_path = current_path + [node]
                stack.append(new_path)


    return None




def breadth_first_search(graph: nx.Graph, start: str, goal: str) -> list[str] | None:
    if start not in graph or goal not in graph:
        return None
    
    queue = deque()
    visited_set = set()

    queue.append([start])
    visited_set.add(start)
    while queue:
        current_path = queue.popleft()
        current_node = current_path[-1]

        if current_node == goal:
            return current_path

        for node in graph.neighbors(current_node):
            if node not in visited_set:
                new_path = current_path + [node]
                queue.append(new_path)
                visited_set.add(node)
    
    return None

def branch_and_bound(graph: nx.Graph, start: str, goal: str) -> list[str] | None:
    if start not in graph or goal not in graph:
        return None
    
    queue = deque()
    best_path = None
    best_path_length = float("inf")

    queue.append([start])
    while queue:
        current_path = queue.popleft()
        current_node = current_path[-1]

        if len(current_path) - 1 >= best_path_length:
            continue

        if current_node == goal:
            best_path = current_path
            best_path_length = len(current_path) - 1
        else:
            for node in graph.neighbors(current_node):
                if node not in current_path:
                    new_path = current_path + [node]
                    queue.append(new_path)

    
    return best_path


import random
import heapq
from collections import deque

# ------------------------------
# Graph Definition (Weighted)
# ------------------------------
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2, 'E': 5},
    'C': {'A': 4, 'F': 3},
    'D': {'B': 2},
    'E': {'B': 5, 'F': 1},
    'F': {'C': 3, 'E': 1}
}

# ------------------------------
# 1. Random Search
# ------------------------------
def random_search(graph, start, goal):
    visited = set()
    path = [start]

    while path:
        current = path[-1]
        if current == goal:
            return path
        visited.add(current)

        neighbors = [n for n in graph[current] if n not in visited]
        if neighbors:
            next_node = random.choice(neighbors)
            path.append(next_node)
        else:
            path.pop()
    return None

# ------------------------------
# 2. Breadth-First Search (BFS)
# ------------------------------
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()

    while queue:
        path = queue.popleft()
        current = path[-1]

        if current == goal:
            return path

        if current not in visited:
            visited.add(current)
            for neighbor in graph[current]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

# ------------------------------
# 3. Dijkstra’s Algorithm
# ------------------------------
def dijkstra(graph, start, goal):
    open_list = [(0, start, [])]  # (cost, node, path)
    closed_list = set()

    while open_list:
        cost, current, path = heapq.heappop(open_list)

        if current in closed_list:
            continue
        path = path + [current]

        if current == goal:
            return (cost, path)

        closed_list.add(current)

        for neighbor, weight in graph[current].items():
            if neighbor not in closed_list:
                heapq.heappush(open_list, (cost + weight, neighbor, path))
    return (float('inf'), None)

# ------------------------------
# Main Program with Loop
# ------------------------------
def main():
    while True:
        print("\n--- Search Algorithms ---")
        print("1. Random Search")
        print("2. Breadth-First Search (BFS)")
        print("3. Dijkstra's Algorithm")
        print("0. Exit")
        choice = input("Choose (1/2/3 or 0 to exit): ").strip()

        if choice == '0':
            print("Exiting program.")
            break

        start = input("Enter start node: ").strip().upper()
        goal = input("Enter goal node: ").strip().upper()

        if start not in graph or goal not in graph:
            print("Invalid nodes. Available nodes:", list(graph.keys()))
            continue

        if choice == '1':
            path = random_search(graph, start, goal)
            print("Random Search Path:", path)
        elif choice == '2':
            path = bfs(graph, start, goal)
            print("BFS Path:", path)
        elif choice == '3':
            cost, path = dijkstra(graph, start, goal)
            print(f"Dijkstra Path: {path} with cost {cost}")
        else:
            print("Invalid choice.")

        # Prompt to return or exit
        back = input("\nPress 0 to exit or any other key to try again: ").strip()
        if back == '0':
            print("Exiting program.")
            break

if __name__ == "__main__":
    main()


import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        
    def add_node(self, value):
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []
    
    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append((to_node, distance))
        self.edges[to_node].append((from_node, distance))  # assuming bidirectional edges
        
def dijkstra(graph, start):
    visited = {start: 0}
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_node not in graph.nodes:
            continue
        
        for neighbor, distance in graph.edges[current_node]:
            new_distance = current_distance + distance
            
            if neighbor not in visited or new_distance < visited[neighbor]:
                visited[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))
    
    return visited

def shortest_path(graph, start, end):
    distances = dijkstra(graph, start)
    path = [end]
    current_node = end
    
    while current_node != start:
        for neighbor, _ in graph.edges[current_node]:
            if distances[current_node] == distances[neighbor] + graph.edges[neighbor][0][1]:
                path.append(neighbor)
                current_node = neighbor
                break
    
    return path[::-1]

# Create the graph
g = Graph()

# Add nodes
nodes = ["Grand Palace", "Villa Vichalai Hotel", "Faculty of Management", "Roundabout", 
         "Male Dormitory", "Female Dormitory 1", "Female Dormitory 2", "Sport Complex Building",
         "Faculty of Agricultural Industry", "Administration Building", 
         "Faculty of Industrial Technology and Management", "Faculty of Engineering"]
for node in nodes:
    g.add_node(node)

# Add edges
edges = [("Grand Palace", "Villa Vichalai Hotel", 300), 
         ("Villa Vichalai Hotel", "Faculty of Management", 54), 
         ("Faculty of Management", "Roundabout", 1500),
         ("Faculty of Management", "Male Dormitory", 2200), 
         ("Male Dormitory", "Female Dormitory 1", 130), 
         ("Male Dormitory", "Female Dormitory 2", 180), 
         ("Female Dormitory 1", "Female Dormitory 2", 110), 
         ("Male Dormitory", "Sport Complex Building", 40), 
         ("Female Dormitory 1", "Sport Complex Building", 100), 
         ("Roundabout", "Sport Complex Building", 750), 
         ("Roundabout", "Faculty of Agricultural Industry", 600), 
         ("Faculty of Agricultural Industry", "Administration Building", 160), 
         ("Roundabout", "Faculty of Industrial Technology and Management", 900), 
         ("Faculty of Industrial Technology and Management", "Faculty of Engineering", 900),
         ("Faculty of Industrial Technology and Management", "Sport Complex Building", 2000)]
for edge in edges:
    g.add_edge(*edge)

# Search for the shortest path
start_location = "Grand Palace"
end_location = "Faculty of Engineering"
shortest_path = shortest_path(g, start_location, end_location)
print("Shortest path from", start_location, "to", end_location, ":", shortest_path)

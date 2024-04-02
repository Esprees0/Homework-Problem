import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()

# Add nodes
nodes = [
    "Guardhouse",
    "Grand Palace",
    "Villa Vichalai Hotel",
    "Faculty of Management",
    "Roundabout",
    "Faculty of Agricultural Industry",
    "Male Dormitory",
    "Female Dormitory1",
    "Female Dormitory2",
    "Sport Complex Building",
    "Faculty of Industrial Technology and Management",
    "Faculty of Engineering",
    "Administration Building"
]

color_node = [
    "gray",
    "orange",
    "cyan",
    "olive",
    "brown",
    "red",
    "cyan",
    "pink",
    "pink",
    "brown",
    "blue",
    "red",
    "green"
]
G.add_nodes_from(nodes)

# Add edges with weights
edges = [
    ("Guardhouse", "Grand Palace",{"weight" : 175}),
    ("Grand Palace", "Villa Vichalai Hotel", {"weight": 300}),
    ("Villa Vichalai Hotel", "Faculty of Management", {"weight": 54}),
    ("Faculty of Management", "Roundabout", {"weight": 1500}),
    ("Roundabout", "Faculty of Agricultural Industry", {"weight": 600}),
    ("Roundabout", "Faculty of Industrial Technology and Management", {"weight": 550}),
    ("Faculty of Agricultural Industry", "Administration Building", {"weight": 160}),
    ("Faculty of Management", "Male Dormitory", {"weight": 2200}),
    ("Male Dormitory", "Female Dormitory1", {"weight": 130}),
    ("Male Dormitory", "Female Dormitory2", {"weight": 180}),
    ("Male Dormitory", "Sport Complex Building", {"weight": 40}),
    ("Female Dormitory1", "Female Dormitory2", {"weight": 110}),
    ("Sport Complex Building", "Faculty of Industrial Technology and Management", {"weight": 2000}),
    ("Faculty of Industrial Technology and Management", "Faculty of Engineering", {"weight": 900}),
    ("Sport Complex Building", "Female Dormitory1", {"weight": 100}),
    ("Roundabout", "Sport Complex Building", {"weight": 750})
]

G.add_edges_from(edges)

# Draw the graph
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=1000, node_color=color_node, font_size=8, font_weight='bold', edge_color='gray')
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Show the graph
plt.title('Campus Map')
plt.show()

'''import networkx as nx
import matplotlib.pyplot as plt

# Create a new graph
G = nx.Graph()

# Add nodes to the graph
G.add_nodes_from(range(1, 8))

# Add edges to the graph
edges = [(4, 6), (6, 7), (7, 5), (5, 3), (3, 1), (1, 4),(2,6)]
G.add_edges_from(edges)

# Set node positions
pos = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 2),
    5: (1, 1),
    6: (2, 2),
    7: (2, 1),
    8: (4, 1)  # จุดใหม่ที่เพิ่มเข้าไป
}


# Draw the graph
nx.draw_networkx(G, pos=pos, node_color='lightblue', edge_color='black', with_labels=True)

# Show the graph
plt.show()'''

# import networkx as nx
# import matplotlib.pyplot as plt

# # สร้างกราฟเปล่า
# G = nx.Graph()

# # เพิ่มโหนด A, B, และ C และเชื่อมโหนด A กับ B, C
# G.add_node([
#     "main entrance",
#     "Grand Palace",
#     "Villa Vichalai Hotel",
#     "Faculty of Management",
#     "Technology Park",
#     "Faculty of Industrial Technology and Management",
#     "Faculty of Engineering",
#     "Faculty of Agricultural Industry",
#     "Central Library",
#     "Administration Building",
#     "Male Dormitory",
#     "Female Dormitory",
#     "New Female Dormitory",
#     "Sport Complex Building",

# ])
# G.add_edge('A', 'B', weight=175)
# G.add_edge('A', 'C', weight=480)

# # สร้าง layout สำหรับการวาดกราฟ
# pos = nx.spring_layout(G)

# # วาดโหนดและเส้นเชื่อมระหว่างโหนด
# nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=20, font_weight="bold")
# labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# # แสดงกราฟ
# plt.show()

import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes representing various locations
locations = [
    ("Grand Palace", 0),
    ("Villa Vichalai Hotel", 480),
    ("Faculty of Management", 550),
    ("Technology Park", 640),
    ("Faculty of Industrial Technology and Management", 2550),
    ("Faculty of Engineering", 3300),
    ("Faculty of Agricultural Industry", 2650),
    ("Central Library", 2600),
    ("Administration Building", 2800),
    ("Male Dormitory", 2700),
    ("Female Dormitory", 2800),
    ("New Female Dormitory", 2850),
    ("Sport Complex Building", 2800)
]

# Add nodes and connect the main entrance with the locations


# Create a layout for graph visualization
pos = nx.spring_layout(G)

# Draw nodes and edges
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=10, font_weight="bold")
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Display the graph
plt.show()

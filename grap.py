import networkx as nx
import matplotlib.pyplot as plt
network = nx.Graph()

network.add_nodes_from([1,2,3])
print(f"This network has now {network.number_of_nodes()} nodes.")

network.add_edge(1,2)
network.add_edge(1,3)
network.add_edge(2,3)

color_list = ["gold", "red", "violet"]
plt.figure(figsize=(8, 6))
plt.title('Example of Graph Representation', size=10)

nx.draw_networkx(network,node_color=color_list, with_labels=True)

plt.show()
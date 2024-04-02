import networkx as nx
import matplotlib.pyplot as plt
network = nx.Graph()

network.add_nodes_from({1:"a",2:"g",3:"h",4:"j",5:"u",6:"b",7:"i"})
print(f"This network has now {network.number_of_nodes()} nodes.")

network.add_edge(1,2)
network.add_edge(1,3)
network.add_edge(1,4)
network.add_edge(1,5)
network.add_edge(2,4)
network.add_edge(3,5)
network.add_edge(3,7)
network.add_edge(5,6)
network.add_edge(6,7)

color_list = ["red", "orange", "yellow","green","blue","purple","pink"]
plt.figure(figsize=(16, 10))
plt.title('Example of Graph Representation', size=10)

nx.draw_networkx(network,node_color=color_list, with_labels=True)

plt.show()

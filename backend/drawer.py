import json

import matplotlib.pyplot as plt
import networkx as nx


graph = nx.Graph()

with open('../data/sample3.js', 'r') as fd:
	data = json.loads(fd.read()[11:])

	for e in data:
		graph.add_edge(e[0], e[1], weight=e[2]*10);

plt.figure(1, figsize=(14, 14))
plt.axis('off') 

pos = nx.spring_layout(graph)
nx.draw_networkx_nodes(graph, pos, node_size=60)
nx.draw_networkx_edges(graph, pos, edge_color='#bbbbbb')
nx.draw_networkx_labels(graph, pos, font_size=8)

plt.savefig("simple_path.png", dpi=200)
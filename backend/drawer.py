import sys, json
from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx

from arg_parser import drawer_argparse as get_args


args = vars(get_args())

sample_file = args['sample']
img_file = args['image']
drawing_mode = args['mode']


graph = nx.Graph()

with open(sample_file, 'r') as fd:
	data = json.loads(fd.read()[11:])
	tdata = defaultdict(list)

	for e in data['data']:
		w = e[2]*10
		graph.add_edge(e[0], e[1], weight=w)
		tdata[w].append((e[0], e[1]))

plt.figure(1, figsize=(14, 14))
plt.axis('off')
plt.title('%s (%i ingredients)' % (data['props']['ftype'], data['props']['inum']))

if drawing_mode == 'opacity':
	pos = nx.graphviz_layout(graph)
	nx.draw_networkx_nodes(
		graph, pos, 
		node_size=60,
		linewidths=0.6
	)
	for weight in tdata:
		nx.draw_networkx_edges(
			graph, pos,
			edgelist=tdata[weight],
			alpha=weight
		)
	nx.draw_networkx_labels(
		graph, pos,
		font_size=8,
		font_color='blue'
	)
elif drawing_mode == 'solid':
	nx.draw_graphviz(
		graph,
		node_size=60,
		linewidths=0.6,
		edge_color='#bbbbbb',
		font_size=8,
		with_labels=True
	)

plt.savefig(
	img_file,
	dpi=200
)
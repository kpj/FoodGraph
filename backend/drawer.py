import sys, json
from collections import defaultdict

import matplotlib.pyplot as plt
import networkx as nx

from arg_parser import drawer_argparse as get_args
from draw_config import config


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
		node_size=config['node_size'],
		linewidths=config['node_border_width']
	)
	for weight in tdata:
		nx.draw_networkx_edges(
			graph, pos,
			edgelist=tdata[weight],
			alpha=weight
		)
	nx.draw_networkx_labels(
		graph, pos,
		font_size=config['label_size'],
		font_color=config['label_color']
	)
elif drawing_mode == 'solid':
	nx.draw_graphviz(
		graph,
		node_size=config['node_size'],
		linewidths=config['node_border_width'],
		edge_color=config['solid_edge_color'],
		font_size=config['label_size'],
		with_labels=True
	)

plt.savefig(
	img_file,
	dpi=200
)
function setupGraph() {
	var graph = jsnx.Graph();

	// add nodes and edges
	for(var p in data) {
		var e = data[p];
		graph.add_edge(e[0], e[1], {weight: e[2]});
	}

	jsnx.draw(graph, {
		element: '#graph',
		with_labels: true,
		weighted: true,
		with_edge_labels: true,
		weights: 'weight',
		weighted_stroke: true,
		layout_attr: {
			charge: -1500,
			linkDistance: 1,
			gravity: 1,
			friction: 0.4,
			alpha: -100
		},
		pan_zoom: {
			enabled: false
		}
	});

	force = d3.layout.force();

	return graph;
}
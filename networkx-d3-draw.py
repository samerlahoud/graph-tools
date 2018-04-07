import networkx as nx
import json
import matplotlib.pyplot as plt
from networkx.readwrite import json_graph

G = nx.erdos_renyi_graph(30,4.0/30)
while not nx.is_connected(G):
    G = nx.erdos_renyi_graph(30,4.0/30)
plt.figure(figsize=(6,4));
nx.draw(G)

for ix,deg in G.degree():
    G.node[ix]['playcount'] = deg
    G.node[ix]['parity'] = (1-deg%2)

for ix,katz in nx.katz_centrality(G).items():
    G.node[ix]['katz'] = katz

G.nodes(data=True)

data = json_graph.node_link_data(G)
with open('graph.json', 'w') as f:
    json.dump(data, f, indent=4)

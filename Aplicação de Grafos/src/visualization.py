import matplotlib.pyplot as plt
import networkx as nx
from networkx.algorithms.community import greedy_modularity_communities

def visualize_graph(G):
    pos = nx.spring_layout(G, seed=42) 
    plt.figure(figsize=(12, 12))
    nx.draw(
        G, pos, with_labels=True, node_size=500, font_size=10,
        edge_color="gray", node_color="skyblue"
    )
    plt.title("Grafo dos Planetas Semelhantes à Terra")
    plt.show()

def detect_clusters(G):
    communities = list(greedy_modularity_communities(G))
    if not communities:
        print("Nenhum cluster foi detectado no grafo.")
    for i, community in enumerate(communities):
        print(f"Cluster {i + 1}: {sorted(community)}")
    return communities

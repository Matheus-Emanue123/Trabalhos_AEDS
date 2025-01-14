# def construct_graph(data, comparison_columns, tolerance=1.5):  # Aumentei a tolerância
#     import networkx as nx
#     import numpy as np
#     G = nx.Graph()
#     for i, row in data.iterrows():
#         G.add_node(i, **row.to_dict())
#     for i in data.index:
#         for j in data.index:
#             if i < j:
#                 distance = np.linalg.norm(
#                     data.loc[i, comparison_columns].values -
#                     data.loc[j, comparison_columns].values
#                 )
#                 if distance <= tolerance:  # Critério de proximidade
#                     G.add_edge(i, j, weight=distance)
#     print(f"Grafo construído com {G.number_of_nodes()} nós e {G.number_of_edges()} arestas.")
#     return G

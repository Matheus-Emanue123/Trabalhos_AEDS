import networkx as nx
import numpy as np
from pyvis.network import Network
import webbrowser
import os

def construct_graph_interactive(data, comparison_columns, tolerance=1.5, output_html="graph.html"):
    """
    Constrói um grafo (usando NetworkX) e gera um HTML interativo com PyVis.
    Cada nó recebe os atributos do DataFrame, e a aresta recebe o peso (distância).
    """
    G = nx.Graph()

    # Cria nós
    for i, row in data.iterrows():
        G.add_node(
            i,
            label=f"Planeta {i}",
            **row.to_dict()
        )

    # Cria arestas
    for i in data.index:
        for j in data.index:
            if i < j:
                distance = np.linalg.norm(
                    data.loc[i, comparison_columns].values -
                    data.loc[j, comparison_columns].values
                )
                if distance <= tolerance:
                    G.add_edge(i, j, weight=distance, title=f"dist={distance:.2f}")

    print(f"Grafo construído com {G.number_of_nodes()} nós e {G.number_of_edges()} arestas.")

    # Construindo a visualização PyVis
    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")

    # Layout (você pode escolher 'force_atlas_2based', 'barnes_hut', etc.)
    net.force_atlas_2based()

    # Adicionar nós no PyVis
    for node, node_data in G.nodes(data=True):
        net.add_node(
            node,
            label=node_data.get("label", str(node)),
            title=str(node_data)  # tooltip com atributos
        )

    # Adicionar arestas no PyVis
    for source, target, edge_data in G.edges(data=True):
        net.add_edge(
            source,
            target,
            title=edge_data.get("title", ""),  # tooltip ao hover
            value=edge_data.get("weight", 1)
        )

    # Mostra botões de configuração (opcional)
    net.show_buttons(filter_=['physics'])

    # 1) Gera o HTML usando `write_html`
    net.write_html(output_html)

    # 2) (Opcional) Abre o arquivo HTML no navegador, se quiser
    full_path = os.path.abspath(output_html)
    webbrowser.open(f"file://{full_path}")

    return G

import networkx as nx
import numpy as np
from pyvis.network import Network
import webbrowser
import os

def construct_graph_interactive_full_connect(data, comparison_columns, output_html="graph.html"):
    """
    Constrói um grafo interativo conectando TODOS os nós do DataFrame,
    atribuindo pesos baseados na distância Euclidiana entre eles.
    """
    import networkx as nx
    import numpy as np
    from pyvis.network import Network
    import webbrowser
    import os

    G = nx.Graph()

    # Cria nós
    for i, row in data.iterrows():
        G.add_node(i, label=f"Planeta {i}", **row.to_dict())

    # Cria arestas para TODOS os pares de planetas, com peso = distância Euclidiana
    for i in data.index:
        for j in data.index:
            if i < j:
                distance = np.linalg.norm(
                    data.loc[i, comparison_columns].values -
                    data.loc[j, comparison_columns].values
                )
                # Adiciona a aresta independentemente da distância
                G.add_edge(i, j, weight=distance, title=f"dist={distance:.2f}")

    print(f"Grafo construído com {G.number_of_nodes()} nós e {G.number_of_edges()} arestas.")

    # Visualização interativa com PyVis (sem alterações)
    net = Network(height="750px", width="100%", bgcolor="#222222", font_color="white")
    net.force_atlas_2based()

    for node, node_data in G.nodes(data=True):
        net.add_node(
            node,
            label=node_data.get("label", str(node)),
            title=str(node_data)
        )

    for source, target, edge_data in G.edges(data=True):
        net.add_edge(
            source,
            target,
            title=edge_data.get("title", ""),
            value=edge_data.get("weight", 1)
        )

    net.show_buttons(filter_=['physics'])
    net.write_html(output_html)
    full_path = os.path.abspath(output_html)
    webbrowser.open(f"file://{full_path}")

    return G


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

    # Cria arestas com base na distância Euclidiana
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
    net.force_atlas_2based()

    # Adicionar nós e arestas ao PyVis
    for node, node_data in G.nodes(data=True):
        net.add_node(
            node,
            label=node_data.get("label", str(node)),
            title=str(node_data)  # tooltip com atributos
        )

    for source, target, edge_data in G.edges(data=True):
        net.add_edge(
            source,
            target,
            title=edge_data.get("title", ""),
            value=edge_data.get("weight", 1)
        )

    net.show_buttons(filter_=['physics'])
    net.write_html(output_html)

    # Abre o arquivo HTML no navegador
    full_path = os.path.abspath(output_html)
    webbrowser.open(f"file://{full_path}")

    return G

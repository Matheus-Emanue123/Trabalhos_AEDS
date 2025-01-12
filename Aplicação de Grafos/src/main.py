from sklearn.preprocessing import MinMaxScaler
import numpy as np
import pandas as pd
from graph_construction_interactive import construct_graph_interactive


def generate_lsh_hashes(data, num_hashes=10, seed=42):
    """
    Gera hashes LSH para um conjunto de dados.
    """
    np.random.seed(seed)
    dimensions = data.shape[1]
    random_vectors = np.random.randn(num_hashes, dimensions)  # Vetores aleatórios
    hashes = np.dot(data, random_vectors.T)  # Produto escalar para gerar assinaturas
    return (hashes > 0).astype(int)  # Convertendo em assinatura binária


# def main_with_lsh_and_earth():
#     # Configurações
#     data_file = r"C:\Users\hecla\OneDrive\Área de Trabalho\CEFET\4 periodo\AEDS II\TRABALHOS\trabalho 01 indiviudal\databases\PS_2025.01.12_10.15.56.csv"
#     comparison_columns = ["st_teff", "st_rad", "st_mass", "pl_insol", "pl_eqt", "pl_orbper", "pl_orbsmax", "pl_orbeccen"]
#     num_hashes = 20  # Número de hashes para LSH
#     tolerance = 1.5

#     # Dados da Terra
#     earth_reference = {
#         "st_teff": 5778,      # Temperatura da estrela (Sol)
#         "st_rad": 1.0,        # Raio da estrela (em relação ao Sol)
#         "st_mass": 1.0,       # Massa da estrela (em relação ao Sol)
#         "pl_insol": 1.0,      # Fluxo de insolação (em relação à Terra)
#         "pl_eqt": 288.0,      # Temperatura de equilíbrio (K)
#         "pl_orbper": 365.25,  # Período orbital (dias)
#         "pl_orbsmax": 1.0,    # Semieixo maior (UA)
#         "pl_orbeccen": 0.0167 # Excentricidade orbital
#     }

#     # Dados artificiais semelhantes à Terra
#     similar_earth_reference = {
#         "st_teff": 5778,      # Mantemos os valores solares
#         "st_rad": 1.0,        
#         "st_mass": 1.0,       
#         "pl_insol": 1.02,     # Levemente maior
#         "pl_eqt": 290.0,      # Levemente maior
#         "pl_orbper": 365.0,   # Levemente menor
#         "pl_orbsmax": 1.01,   # Levemente maior
#         "pl_orbeccen": 0.02   # Levemente maior
#     }

#     # Carregar e preparar os dados
#     data = pd.read_csv(data_file, comment='#')  # Ignorar linhas de comentário
#     data = data = data.iloc[:]
#     data = data[comparison_columns].fillna(data[comparison_columns].median())  # Preencher valores ausentes com a mediana

#     # Adicionar Terra e planeta artificial
#     earth_data = pd.DataFrame([earth_reference, similar_earth_reference], columns=comparison_columns)
#     data = pd.concat([data, earth_data], ignore_index=True)

#     # Índices fixos para a Terra e o planeta artificial
#     earth_index = len(data) - 2
#     artificial_index = len(data) - 1

#     # Normalizar os dados
#     normalized_data = MinMaxScaler().fit_transform(data)

#     # Gerar hashes LSH
#     print("\n--- Gerando Hashes LSH ---")
#     hashes = generate_lsh_hashes(normalized_data, num_hashes=num_hashes)
#     hashes_df = pd.DataFrame(hashes, columns=[f"hash_{i}" for i in range(num_hashes)])

#     # Agrupar planetas semelhantes
#     similarity_buckets = hashes_df.groupby(list(hashes_df.columns)).indices
#     grouped_planets = {bucket: list(planets) for bucket, planets in similarity_buckets.items()}

#     # Identificar grupos com a Terra e o planeta artificial
#     groups_with_earth = [
#         (bucket, planets) for bucket, planets in grouped_planets.items()
#         if earth_index in planets or artificial_index in planets
#     ]

#     # Exibir grupos com a Terra
#     print("\n--- Grupos que Contêm a Terra ou o Planeta Artificial ---")
#     for bucket, planets in groups_with_earth:
#         print(f"Grupo {bucket}: Planetas {planets}")

#     # Criar grafos baseados nos grupos LSH
#     for bucket, planets in grouped_planets.items():
#         if len(planets) > 1:  # Apenas grupos com mais de 1 planeta
#             group_data = data.iloc[planets]
#             output_file = f"graph_group_{bucket}.html"
#             construct_graph_interactive(group_data, comparison_columns, tolerance=tolerance, output_html=output_file)

#     print("Grafos gerados para grupos com planetas semelhantes!")


# if __name__ == "__main__":
#     main_with_lsh_and_earth()

def main_with_earth_specific_graphs():
    # Configurações
    data_file = r"C:\Users\hecla\OneDrive\Área de Trabalho\CEFET\4 periodo\AEDS II\TRABALHOS\trabalho 01 indiviudal\databases\PS_2025.01.12_10.15.56.csv"
    comparison_columns = ["st_teff", "st_rad", "st_mass", "pl_insol", "pl_eqt", "pl_orbper", "pl_orbsmax", "pl_orbeccen"]
    num_hashes = 20  # Número de hashes para LSH
    tolerance = 1.8

    # Dados da Terra
    earth_reference = {
        "st_teff": 5778,      # Temperatura da estrela (Sol)
        "st_rad": 1.0,        # Raio da estrela (em relação ao Sol)
        "st_mass": 1.0,       # Massa da estrela (em relação ao Sol)
        "pl_insol": 1.0,      # Fluxo de insolação (em relação à Terra)
        "pl_eqt": 288.0,      # Temperatura de equilíbrio (K)
        "pl_orbper": 365.25,  # Período orbital (dias)
        "pl_orbsmax": 1.0,    # Semieixo maior (UA)
        "pl_orbeccen": 0.0167 # Excentricidade orbital
    }

    # Dados artificiais semelhantes à Terra
    similar_earth_reference = {
        "st_teff": 5778,      # Mantemos os valores solares
        "st_rad": 1.0,        
        "st_mass": 1.0,       
        "pl_insol": 1.02,     # Levemente maior
        "pl_eqt": 290.0,      # Levemente maior
        "pl_orbper": 365.0,   # Levemente menor
        "pl_orbsmax": 1.01,   # Levemente maior
        "pl_orbeccen": 0.02   # Levemente maior
    }

    # Carregar e preparar os dados
    data = pd.read_csv(data_file, comment='#')  # Ignorar linhas de comentário
    data = data[comparison_columns].fillna(data[comparison_columns].median())  # Preencher valores ausentes com a mediana

    # Adicionar Terra e planeta artificial
    earth_data = pd.DataFrame([earth_reference, similar_earth_reference], columns=comparison_columns)
    data = pd.concat([data, earth_data], ignore_index=True)

    # Índices fixos para a Terra e o planeta artificial
    earth_index = len(data) - 2
    artificial_index = len(data) - 1

    # Normalizar os dados
    normalized_data = MinMaxScaler().fit_transform(data)

    # Gerar hashes LSH
    print("\n--- Gerando Hashes LSH ---")
    hashes = generate_lsh_hashes(normalized_data, num_hashes=num_hashes)
    hashes_df = pd.DataFrame(hashes, columns=[f"hash_{i}" for i in range(num_hashes)])

    # Agrupar planetas semelhantes
    similarity_buckets = hashes_df.groupby(list(hashes_df.columns)).indices
    grouped_planets = {bucket: list(planets) for bucket, planets in similarity_buckets.items()}

    # Identificar grupos com a Terra
    groups_with_earth = [
        (bucket, planets) for bucket, planets in grouped_planets.items()
        if earth_index in planets
    ]

    # Gerar grafos apenas para os grupos com a Terra
    print("\n--- Gerando Grafos Apenas para Grupos com a Terra ---")
    for bucket, planets in groups_with_earth:
        print(f"Gerando grafo para o grupo {bucket} com planetas {planets}")
        group_data = data.iloc[planets]
        output_file = f"graph_group_with_earth_{bucket}.html"
        construct_graph_interactive(group_data, comparison_columns, tolerance=tolerance, output_html=output_file)

    print("Grafos gerados para todos os grupos contendo a Terra!")


if __name__ == "__main__":
    main_with_earth_specific_graphs()

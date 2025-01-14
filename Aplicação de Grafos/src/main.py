import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler 
from graph_construction_interactive import construct_graph_interactive
from graph_construction_interactive import construct_graph_interactive_full_connect

def generate_lsh_hashes(data, num_hashes=10, seed=42):
    np.random.seed(seed)
    dimensions = data.shape[1]
    random_vectors = np.random.randn(num_hashes, dimensions)  # Vetores aleatórios
    hashes = np.dot(data, random_vectors.T)  # Produto escalar para gerar assinaturas
    return (hashes > 0).astype(int)  # Convertendo em assinatura binária

def main_with_earth_specific_graphs():
    # Configurações
    data_file = r"C:\Users\hecla\OneDrive\Área de Trabalho\CEFET\3 periodo\AEDS\Trabalhos_AEDS\Aplicação de Grafos\databases\PS_2025.01.12_10.15.56.csv"
    comparison_columns = [
        "st_teff", "st_rad", "st_mass", "pl_insol",
        "pl_eqt", "pl_orbper", "pl_orbsmax", "pl_orbeccen"
    ]
    num_hashes = 20  # Número de hashes para LSH
    tolerance = 0.1

    # Dados da Terra e do planeta artificial
    earth_reference = { 
        "st_teff": 5778,
        "st_rad": 1.0,
        "st_mass": 1.0,
        "pl_insol": 1.0,
        "pl_eqt": 288.0,
        "pl_orbper": 365.25,
        "pl_orbsmax": 1.0,
        "pl_orbeccen": 0.0167
    }

    similar_earth_reference = {
        "st_teff": 5778,
        "st_rad": 1.0,
        "st_mass": 1.0,
        "pl_insol": 1.02,
        "pl_eqt": 290.0,
        "pl_orbper": 365.0,
        "pl_orbsmax": 1.01,
        "pl_orbeccen": 0.02
    }

    # Carregar e preparar os dados
    data = pd.read_csv(data_file, comment='#')
    data = data[comparison_columns].fillna(data[comparison_columns].median())

    # Adicionar Terra e planeta artificial
    earth_data = pd.DataFrame([earth_reference, similar_earth_reference], columns=comparison_columns)
    data = pd.concat([data, earth_data], ignore_index=True)

    # Índices fixos para Terra e planeta artificial
    earth_index = len(data) - 2
    artificial_index = len(data) - 1

    scaler = MinMaxScaler()
    normalized_data = scaler.fit_transform(data)

    # Transformação logarítmica (log(x+1))
    # data_log = data.copy()
    # for col in comparison_columns:
    #     # Adicionamos +1 antes de tirar o log para evitar erro em caso de valor zero
    #     data_log[col] = np.log(data_log[col] + 1)

    # Gerar hashes LSH usando dados transformados
    print("\n--- Gerando Hashes LSH ---")
    hashes = generate_lsh_hashes(normalized_data, num_hashes=num_hashes)
    hashes_df = pd.DataFrame(hashes, columns=[f"hash_{i}" for i in range(num_hashes)])

    # Agrupar planetas semelhantes via LSH
    similarity_buckets = hashes_df.groupby(list(hashes_df.columns)).indices
    grouped_planets = {bucket: list(planets) for bucket, planets in similarity_buckets.items()}

    # Identificar grupos que contêm a Terra
    groups_with_earth = [
        (bucket, planets) for bucket, planets in grouped_planets.items()
        if earth_index in planets
    ]

    # Rotular e imprimir os grupos
    for bucket, planets in groups_with_earth:
        print(f"Gerando grafo para o grupo {bucket} com planetas {planets}")
        group_data = data.iloc[planets]  # Podemos usar os dados originais ou data_log
        output_file = f"graph_group_with_earth_{bucket}.html"
        
        construct_graph_interactive_full_connect(
            group_data, comparison_columns, 
            output_html=output_file
        )

    print("Grafos gerados para todos os grupos contendo a Terra!")

if __name__ == "__main__":
    main_with_earth_specific_graphs()

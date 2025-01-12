def is_similar_to_earth(row, reference, tolerance=1.8):
    """
    Verifica se, para cada coluna, a diferença RELATIVA é menor que uma tolerância.
    """
    eps = 1e-9  # Para evitar divisão por zero
    for col, ref_value in reference.items():
        rel_diff = abs(row[col] - ref_value) / (abs(ref_value) + eps)
        if rel_diff > tolerance:
            return False
    return True


def filter_similar_planets(data, reference, comparison_columns):
    """
    Filtra os planetas que são semelhantes à Terra.
    """
    # Aplicar a função de semelhança
    # Copiar o DataFrame para evitar fragmentação
    data = data.copy()
    data["similar_to_earth"] = data[comparison_columns].apply(
        lambda row: is_similar_to_earth(row, reference), axis=1
)

    # Retornar apenas os planetas semelhantes
    return data[data["similar_to_earth"]]

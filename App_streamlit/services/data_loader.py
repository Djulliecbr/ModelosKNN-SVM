import pandas as pd

def load_datasets(train_path, test_path, sample_option=None, sample_size=100):
    """Carrega os datasets de treino e teste, com opção de amostragem."""
    # Carregar datasets de treino e teste
    train_data = pd.read_csv(train_path)
    test_data = pd.read_csv(test_path)

    # Se o usuário escolher uma amostra personalizada
    if sample_option == "Amostra personalizada":
        train_data = train_data.sample(n=sample_size, random_state=1)
        test_data = test_data.sample(n=sample_size, random_state=1)

    return train_data, test_data
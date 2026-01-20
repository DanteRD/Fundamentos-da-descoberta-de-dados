import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # Biblioteca para criação de gráficos

# ===============================
# Criando nosso DataFrame
# ===============================

# Gerando 20 idades aleatórias entre 20 e 90 anos
idades = np.random.randint(20, 90, 20)

# Gerando salários relacionados à idade
# (idade multiplicada por um valor aleatório entre 40 e 80)
salarios = idades * np.random.randint(40, 80, 20)

# Gerando pontuações relacionadas ao salário
# Usamos números decimais entre 0.5 e 1.5
pontuacoes = salarios * np.random.uniform(0.5, 1.5, 20)

# Lista de profissões possíveis
profissoes = [
    'Engenheiro', 'Professor', 'Médico', 'Advogado',
    'Designer', 'Analista', 'Gerente', 'Programador'
]

# ===============================
# Criando o DataFrame
# ===============================

novo_data = {
    'Idade': idades,                     # Coluna de idades
    'Salário': salarios,                 # Coluna de salários
    'Pontuação': pontuacoes.round(2)     # Pontuação arredondada para 2 casas decimais
}

# Criando o DataFrame a partir do dicionário
df = pd.DataFrame(novo_data)

# Adicionando uma coluna de profissões aleatórias
df['Profissão'] = np.random.choice(profissoes, size=len(df))

# Exibindo as primeiras 10 linhas do DataFrame
print(df.head(10))

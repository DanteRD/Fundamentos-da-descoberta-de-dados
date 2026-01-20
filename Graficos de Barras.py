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

# Nessa etapa criamos a figura da imagem que será gerada, aqui nesses valores numéricos podemos alterar o tamanho da imagem.
plt.figure(figsize=(10, 6))

# Agrupando os dados do DataFrame por profissão e calculando a média do salário para cada profissão
salario_por_profissao = df.groupby('Profissão')['Salário'].mean()

# Indicamos aqui os índices do DataFrame no eixo x e os salários no eixo y, vejam que vocês podem realizar a alteração da cor, nesse caso usamos Skyblue
plt.bar(salario_por_profissao.index, salario_por_profissao, color='skyblue')

# Aqui adicionamos um título e podemos alterar o tamanho da sua fonte no "fontsize"
plt.title('Distribuição de Salários', fontsize=16)

# Adicionando um rótulo ao eixo x com tamanho de fonte 12
plt.xlabel('Índice', fontsize=12)

# Adicionando um rótulo ao eixo y com tamanho de fonte 12
plt.ylabel('Salário', fontsize=12)

# Nessa etapa rotacionamos os rótulos do eixo x em 45 graus para melhorar a legibilidade
plt.xticks(rotation=45)

# Adicionando grades ao gráfico com estilo de linha tracejada (--)
# e com transparência de 70% (alpha=0.7) para melhorar a visualização
plt.grid(True, linestyle='--', alpha=0.7)

# Exibindo o gráfico
plt.show()

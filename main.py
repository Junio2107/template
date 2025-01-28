#!/usr/bin/env python
# coding: utf-8

# # Importação de Bibliotecas

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Importação das bases de dados

# In[1]:


# df = pd.read...


# # Objetivo da analise

# Criar um modelo de ... para previsão de ... baseado em ...
# 
# Prever o nível de gordura corporal dos pacientes da clinica baseado nas medidas corporais coletadas dos pacientes

# # Compreensão do negocio

# Dicionario de dados

# # Analise Exploratoria dos Dados

# Entender o que tem dentro da tabela.
# missing, outliers, distribuição das variaveis, simetria, assimetria, normalidade, etc.

# print(df.info())
# print(df.describe())
# print(df.isnull().sum())
# print(df.duplicated().sum())
# 
# correlation_matrix = df.corr()
# sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
# plt.title('Matriz de Correlação')
# plt.show()
# 
# for column in df.columns:
#     plt.figure(figsize=(10, 6))
#     sns.histplot(df[column], kde=True)
#     plt.title(f'Distribuição de {column}')
#     plt.show()

# # Analises Estatisticas

# Boxsplot, scatterplot

# # Analise bivariada

# Foco na multicolinearidade, VIF, correlações e escolhas de variaveis de acordo com as 
# 

# # Modelo

# In[ ]:





# # Analise de residuos

# 4 Regras;
# 1) O erro é uma variável aleatoria com media zero;
# 2) A variancia do erro, designado por sigma2, é identica para todos os valores das variaveis independentes, ou seja, a variancia e constante;
# 3) Os valores de E são independentes - não deve ter um padrão;
# 4) O erro é uma variavel aleatoria com distribuicao normal refletindo o desvio entre y e y^
# 
# Se alguma regra for quebrada, o meu modelo não funcionara e devera ser reavaliado

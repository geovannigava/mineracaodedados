
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd


# In[4]:


# Carrega o dataset a partir do scikit
from sklearn import datasets

iris = datasets.load_iris()
iris


# In[5]:


iris.data


# In[5]:


iris.target


# In[6]:


# Transforma o dataset em um DataFrame Pandas
df_iris = pd.DataFrame(iris.data)
df_iris['target'] = iris.target

df_iris.head()


# In[7]:


# Nome das colunas
df_iris.columns.tolist()


# In[27]:


# Alterando o nome das coluna
df_iris.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'type']
df_iris.head(10)


# In[9]:


# Tamanho do dataset
df_iris.shape


# In[10]:


# Acessando uma coluna
df_iris['sepal_length'].head()


# In[11]:


# Selecionando mais de uma coluna
df_iris[['sepal_length', 'petal_length']].head()


# In[12]:


# Removendo uma coluna
# Notação Pandas para os eixos (axis):
# Linhas: axis 0
# Colunas: axis 1
df_iris.drop(['type'], axis=1).head()


# In[13]:


# Tipos únicos
df_iris['type'].unique()


# In[14]:


# Associando o nome ao tipo
df_iris['type'].map({
    0: 'Setosa',
    1: 'Versicolour',
    2: 'Virginica'
})


# In[15]:


# Filtrando por tipo
df_iris[df_iris['type'] == 2].head()


# In[16]:


# Filtrando por tamanho da pétala
df_iris[df_iris['petal_length'] > 5].head()


# In[17]:


# Filtrando por tipo E tamanho da pétala
df_iris[
    (df_iris['type'] == 2) & (df_iris['petal_length'] > 5)
].head()


# In[18]:


# Tamanho mínimo, máximo e médio da largura das pétalas
print('Menor:', df_iris['petal_width'].min())
print('Maior:', df_iris['petal_width'].max())
print('Média:', df_iris['petal_width'].mean())


# In[19]:


# Tamanho médio da largura das pétalas por tipo
for i in df_iris['type'].unique():
    print('Tipo', i)
    print(df_iris[df_iris['type'] == i]['petal_width'].mean(), '\n')


# In[20]:


# Iris com maior tamanho geral (soma das dimensões das pétalas e sépalas)
df_iris[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].sum(axis=1).max()


# In[21]:


# Aplicando transformação em uma coluna (conversão para int)
df_iris['sepal_length'].apply(lambda x: int(x)).head()


# In[22]:


# Aplicando transformação com várias colunas
df_iris.apply(lambda row: row['sepal_length'] + row['petal_length'], axis=1).head()


# In[28]:


# Gráfico de dispersão comparando tamanho da pétala e sépala
import seaborn as sns
import matplotlib.pyplot as plt

sns.FacetGrid(
    df_iris, 
    hue='type',
    height=10
).map(
    plt.scatter, 'sepal_length', 'petal_length'
).add_legend()

plt.title('Relação entre sepal_length e petal_length')


# In[29]:


# Histograma
df_iris.hist(edgecolor='black', figsize=(20, 10), grid=False);


# In[30]:



# Tamanho da pétala por tipo
plt.figure(figsize=(5, 5))

sns.barplot(
    x=df_iris['type'], 
    y=df_iris['petal_width']
)

plt.xlabel('Tipo')
plt.ylabel('Tamanho da pétala')
plt.show()


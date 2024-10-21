Previsão de Preços de Imóveis - Melbourne
Este projeto tem como objetivo prever os preços de imóveis na cidade de Melbourne, Austrália, utilizando algoritmos de machine learning. O modelo principal utiliza uma Árvore de Decisão, e comparações são feitas com outros modelos como Random Forest e Gradient Boosting para garantir a melhor acurácia. A interface é desenvolvida com Streamlit, permitindo que o usuário interaja com o modelo de forma intuitiva.

Visão Geral
O projeto visa oferecer uma ferramenta fácil de usar para prever o valor de propriedades com base em características como número de quartos, banheiros, tamanho do lote, entre outras. Além disso, é possível carregar um arquivo CSV para fazer previsões em lote. O desempenho do modelo é avaliado usando o Erro Médio Absoluto (MAE) para comparar os preços previstos com os preços reais.

Funcionalidades
Previsão de preços com base em características do imóvel.
Interface web interativa para inserção manual de dados ou upload de arquivo CSV.
Comparação de modelos de machine learning (Árvore de Decisão, Random Forest, Gradient Boosting).
Exibição de métricas de desempenho (como o Erro Médio Absoluto - MAE).

Estrutura do Projeto
bash
Copiar código
machine_learning/
├── dados/                      # Contém o arquivo CSV de dados (db.csv)
├── imagem/                     # Contém imagens utilizadas no front-end
├── src/                        # Contém o arquivo app.py (aplicação Streamlit)
│   └── app.py                  # Aplicação principal que executa o Streamlit
├── melbourne_model.joblib      # Modelo de machine learning treinado
├── projeto.py                  # Script com o código do projeto principal
└── requirements.txt            # Lista de dependências do projeto

Instalação
Para rodar este projeto localmente, siga os passos abaixo:

Clone este repositório para a sua máquina local:
bash
Copiar código
git clone https://github.com/seu-usuario/machine_learning.git
cd machine_learning

Instale as dependências do projeto:
bash
Copiar código
pip install -r requirements.txt
Execute a aplicação Streamlit:
bash
Copiar código
streamlit run src/app.py
Acesse a aplicação no seu navegador, geralmente no endereço http://localhost:8501.

Como Usar
Previsão Manual: Preencha os campos fornecidos na interface com as características da propriedade (como número de quartos, banheiros, tamanho do lote) e clique no botão de previsão para obter o preço estimado.

Previsão por CSV: Faça upload de um arquivo CSV com os dados de várias propriedades. O sistema processará o arquivo e exibirá as previsões para cada propriedade.

Avaliação de Desempenho: O sistema exibe o Erro Médio Absoluto (MAE) para mostrar o quão preciso o modelo foi ao prever os preços das propriedades em comparação com os valores reais.

Exemplo de Dados
Os dados para o modelo são baseados em características dos imóveis, como:

Rooms: Número de quartos
Bathroom: Número de banheiros
Landsize: Tamanho do lote (m²)
BuildingArea: Área construída (m²)
YearBuilt: Ano de construção
Lattitude e Longitude: Localização geográfica da propriedade
Um exemplo de linha no arquivo CSV seria:

csv
Copiar código
Rooms,Bathroom,Landsize,BuildingArea,YearBuilt,Lattitude,Longitude
3,2,150,120,1990,-37.809,144.995
Comparação de Modelos
O projeto faz uso de diferentes algoritmos de machine learning para prever os preços dos imóveis:

Árvore de Decisão: Simples e interpretável, usado como modelo base.
Random Forest: Conjunto de árvores de decisão, melhora a precisão geral.
Gradient Boosting: Focado em otimizar erros e melhorar o desempenho geral.
A comparação dos modelos é feita com base na métrica MAE, e o melhor modelo é escolhido para fazer as previsões.

Melhorias Futuras
Incluir mais características dos imóveis para melhorar a precisão das previsões.
Implementar suporte a outros algoritmos de machine learning como XGBoost ou LightGBM.
Adicionar mais opções de visualização de dados para ajudar os usuários a entenderem melhor as previsões.
Dependências
As bibliotecas e ferramentas usadas neste projeto estão listadas no arquivo requirements.txt. As principais dependências incluem:

Python 3.10+
Streamlit 1.24.0
Pandas 1.5.3
Scikit-learn 1.3.0
Joblib 1.3.1
Pillow 9.5.0
Licença
Este projeto é licenciado sob a Licença MIT. Para mais detalhes, consulte o arquivo LICENSE.
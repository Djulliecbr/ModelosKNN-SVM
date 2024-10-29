# Projeto de ciclo 2 do Alpha Edtech: Classificação de Pontuação de Crédito

## Descrição do Projeto

Este projeto tem como objetivo prever a pontuação de crédito utilizando dados anonimizados da CloudWalk. O conjunto de dados contém diferentes recursos (“x_1, x_2, x_3...”) e rótulos binários (“y”), onde `1` representa um cliente que pagou o empréstimo e `0` representa um cliente que não pagou.

A análise do projeto inclui a construção de dois modelos de aprendizado de máquina com a finalidade de comparar a eficácia entre um modelo linear poderoso e um modelo baseado em proximidade:

- **Modelo 1:** SVM (Support Vector Machines) – com diferentes Kernels (linear, polinomial, RBF).
- **Modelo 2:** KNN (K-Nearest Neighbors).

### Objetivos Específicos:

- Comparar o desempenho de um modelo linear poderoso (SVM) com um modelo baseado em proximidade (KNN).
- Avaliar o impacto dos diferentes Kernels no SVM (linear, polinomial, RBF).
- Analisar o comportamento do KNN conforme o dataset cresce.
- Avaliar a sensibilidade dos modelos à normalização dos recursos.
- Avaliar problemas de overfitting e underfitting, especialmente no KNN.

## Fluxo de Trabalho do Projeto

1. **Entendimento dos Dados**
   - Exploração dos dados, identificação de variáveis, análise de correlação e distribuição do atributo alvo (`y`).
   - Análise da importância da anonimização e normalização dos dados.

2. **Pré-Processamento dos Dados**
   - Divisão dos dados em treinamento (80%) e teste (20%) de forma estratificada, garantindo que a distribuição de classes seja consistente.
   - Análise de outliers, imputação de valores faltantes e normalização dos dados.

3. **Treinamento e Avaliação dos Modelos**
   - Treinamento dos dois modelos (SVM e KNN).
   - Avaliação de métricas como:
     - **Acurácia**
     - **Precisão, Recall e F1-Score**
     - **Matriz de Confusão**
     - **Curva ROC e AUC**
     - **Log-loss ou Binary Cross-Entropy** (se aplicável)

4. **Interpretação dos Resultados**
   - Análise das variáveis mais importantes que impactam cada modelo.
   - Verificação de overfitting utilizando cross-validation.

5. **Ajuste de Hiperparâmetros**
   - Utilização de técnicas como Grid Search, Random Search, ou Bayesian Optimization para aprimorar o desempenho dos modelos.
     
## Tecnologias Utilizadas

- **Linguagem:** Python
- **Bibliotecas:** Scikit-learn, NumPy, Pandas, Matplotlib
- **Ambiente:** VSCode, Google Colab, GitHub

## Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/seuusuario/nome-do-repositorio.git
   ```
2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o notebook de treinamento no Google Colab:
   - Abra o arquivo `treinamento_modelos.ipynb` no Google Colab e execute as células conforme instruído.

## Métricas de Avaliação Utilizadas

- **Acurácia**: Medida da proporção de previsões corretas do modelo.
- **Precisão, Recall e F1-Score**: Avaliam a qualidade do modelo em termos de previsões positivas.
- **Matriz de Confusão**: Visualização das previsões corretas e incorretas.
- **Curva ROC e AUC**: Medem a habilidade do modelo em classificar corretamente.

## Considerações Finais

Este projeto busca compreender melhor a aplicabilidade de diferentes modelos de aprendizado de máquina na classificação de risco de crédito. Por meio da comparação de SVMs com diferentes Kernels e KNN, será possível determinar o modelo mais adequado e explorar a sensibilidade a diferentes técnicas de pre-processamento e ajuste.


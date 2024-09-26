#Projeto desenvolvido por:
- Fernanda Kaory Saito - RM551104
- Geovanna Silva Cunha - RM97736
- Lana Giulia Auada Leite - RM551143
- Lucas Palamartschuk de Toledo - RM97913
- Victor Camargo Maciel - RM98384

#LepArt
1. Introdução
Este projeto visa criar um sistema para registrar e avaliar sessões de treinamento de habilidades motoras, manuais e sensoriais de estudantes de medicina em uma plataforma de realidade virtual (VR). O sistema foi projetado para armazenar os dados dos estudantes e suas sessões de treinamento, calcular as pontuações baseadas no desempenho em três métricas principais (coordenação motora, habilidade manual e resposta sensorial), e fornecer uma avaliação geral do progresso do estudante ao longo do tempo.

A principal motivação deste projeto é facilitar o acompanhamento do desenvolvimento dos estudantes em habilidades práticas essenciais para a prática médica, utilizando a tecnologia de VR. O sistema permite registrar múltiplas sessões de treinamento para cada estudante e oferece uma análise das pontuações obtidas.

2. Metodologia
A implementação do sistema foi feita utilizando Python, com o objetivo de manipular uma tabela (matriz) de dados que armazena as informações dos estudantes e seus respectivos treinamentos.

- Armazenamento de dados: Os dados dos estudantes foram armazenados em uma matriz, onde cada linha representa um estudante e as colunas contêm o nome, curso e uma lista de sessões de treinamento.

Exemplo da estrutura da matriz:
[
  ["Ana Silva", "Medicina", [[9.0, 8.5, 9.2], [8.5, 9.0, 8.8]]],
  ["Carlos Souza", "Medicina", [[7.5, 7.8, 8.0]]]
]

- Funções desenvolvidas:

  - Cadastrar estudante: Registra um novo estudante na tabela com seu nome, curso e uma lista vazia de treinamentos.
  - Registrar treinamento: Adiciona uma nova sessão de treinamento para o estudante, composta por três valores (coordenação motora, habilidade manual e resposta sensorial).
  - Calcular pontuação: Calcula uma pontuação ponderada para cada sessão de treinamento, atribuindo pesos de 40% para coordenação motora, 40% para habilidade manual e 20% para resposta sensorial.
  - Avaliar estudante: Avalia todas as sessões de treinamento de um estudante e calcula a média de pontuação, fornecendo uma análise de desempenho geral.
  - Cálculo das pontuações: Cada sessão de treinamento resulta em uma pontuação total com base nas métricas fornecidas. A fórmula utilizada para o cálculo foi:
    ![image](https://github.com/user-attachments/assets/1cc52ba7-e6f1-4462-baea-fd600c3354cc)

  3. Resultados
Ao executar o código, o sistema permite que estudantes sejam cadastrados, seus treinamentos sejam registrados, e suas avaliações sejam realizadas de forma precisa. Como exemplo, ao cadastrar dois estudantes e registrar sessões de treinamento para ambos, o sistema foi capaz de calcular e imprimir as pontuações de cada sessão individual e a média geral de cada estudante.

Exemplo de saída:
Estudante Ana Silva cadastrado com sucesso.
Treinamento registrado para Ana Silva.
Treinamento registrado para Ana Silva.
Avaliação de Ana Silva:
Treinamento 1: Pontuação = 8.86
Treinamento 2: Pontuação = 8.86
Média de Pontuação de Ana Silva: 8.86

Estudante Carlos Souza cadastrado com sucesso.
Treinamento registrado para Carlos Souza.
Avaliação de Carlos Souza:
Treinamento 1: Pontuação = 7.78
Média de Pontuação de Carlos Souza: 7.78

4. Conclusão
O sistema desenvolvido cumpre seu objetivo de registrar e avaliar os desempenhos dos estudantes em treinamentos de realidade virtual voltados para a prática médica. A utilização de uma tabela (matriz) para armazenar os dados dos estudantes permitiu uma organização eficiente e clara, além de facilitar o processo de busca e avaliação. O sistema também oferece uma forma prática de acompanhar o progresso dos estudantes ao longo de múltiplas sessões de treinamento, calculando as pontuações de forma justa e ponderada.

Futuramente, este projeto pode ser expandido com a adição de uma interface gráfica e a integração com um banco de dados, permitindo uma escalabilidade maior e o suporte a um número maior de estudantes e sessões de treinamento. Além disso, a implementação de gráficos e relatórios visuais seria um grande avanço na apresentação dos resultados das avaliações.

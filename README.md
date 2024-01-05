# Análise de Sentimentos em Textos em Python
Este repositório foi desenvolvido durante o primeiro período para um trabalho ao qual o objetivo era criar alguma forma de metrificar textos por meio de um algoritmo e depois gerar um relatório .csv sobre o que foi analisado, tudo foi criado usando a minha lógica durante o primeiro período e inclusive a técnica que utilizei no código eu descobri depois que já existia que é o MapReduce.

## Sobre o Código
o algoritmo atribui nota 5 para as palavras "good", 0 para as "neutral" e -5 para as "bad", com isso ele irá reconhecer a ocorrencia das palavras nos textos apresetados e dar uma nota final a frase, se a nota ao final for positiva ele reconhece como um texto que tem um conteúdo positivo, 0 conteúdo neutro e negatia um conteúdo ruim, além disso ele funciona com uma forma primitiva de machine learning, ao rodar o código ele irá gerar uma nota para cada texto e adicionar palavras que não constava no arquivo das palavras baseado na nota final, por exemplo caso um texto tenha nota final 0, todas as palavras que ele não reconheceu ele irá adicionar no arquivo das palavras no correspondente da nota que no caso seria o "neutral".

## Conteúdo do Repositório
Dados: Aqui estão um exemplo de conjuntos de dados utilizados no algoritmo. Eles incluem uma variedade de textos que serão introduzidos no algoritmo e o outro arquivo são as palavras que vão ser utilizadas para julgar as frases.

[frases](https://github.com/rennanpo/text-based-sentiments-analysis/blob/master/frases) para criar o seu é só seguir esse arquivo, em geral é necessário apenas separar cada frase com uma quebra de linha.

[palavras](https://github.com/rennanpo/text-based-sentiments-analysis/edit/master/README.md) para criar o seu é só colocar o nome da categoria (good, neutral e bad) e colocar as palavras separadas por espaço
 
## Como usar o código
[código](https://github.com/rennanpo/text-based-sentiments-analysis/edit/master/README.md) aqui está o algoritmo que criei no primeiro periodo, para faze-lo funcionar basta informar para o algoritmo os 2 arquivos auxiliares seguindo o exemplo que dei que são o das palavras e o arquivo das frases que serão analisadas, após isso será gerado um relatório no formato .csv sobre os textos analisados e a atualização do arquivo das palavras baseado nas novas palavras que o algoritmo aprendeu.

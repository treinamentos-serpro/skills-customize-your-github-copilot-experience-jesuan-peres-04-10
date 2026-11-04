
# 📘 Assignment: Jogo da Forca

## 🎯 Objetivo

Pratique manipulação de strings, loops, condicionais e seleção aleatória em Python ao criar um jogo da Forca interativo. O jogo deve permitir que a pessoa descubra uma palavra oculta antes de esgotar as tentativas.

## 📝 Tarefas

### 🛠️ Implementar o Jogo da Forca

#### Descrição
Complete o código inicial em `starter-code.py` para implementar uma partida de Forca no terminal. Use a lista de palavras fornecida e atualize o estado do jogo a cada palpite.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista `words`.
- Exibir as letras adivinhadas nas posições corretas e representar as letras ainda não descobertas por `_`.
- Solicitar palpites de letras e atualizar o progresso quando um palpite estiver na palavra.
- Contabilizar e exibir as tentativas incorretas restantes; um palpite incorreto deve reduzir esse total.
- Encerrar a partida quando a palavra for descoberta ou quando não houver tentativas incorretas restantes.
- Informar se a pessoa venceu ou perdeu e, em caso de derrota, revelar a palavra escolhida.